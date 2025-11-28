"""
Pruebas para los endpoints de la API de clientes
Con autenticación JWT real - Sin modificar el backend
"""
import pytest
from fastapi import status
from uuid import uuid4

class TestClienteAPI:
    """Pruebas para los endpoints de clientes"""
    
    def test_obtener_clientes_sin_token_falla(self, client):
        """Prueba que obtener clientes sin token falla"""
        # Act
        response = client.get("/clientes/")
        
        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_obtener_clientes_vacio(self, client, headers_usuario):
        """Prueba obtener lista de clientes cuando está vacía"""
        # Act
        response = client.get("/clientes/", headers=headers_usuario)
        
        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "no hay clientes registrados" in response.json()["detail"].lower()
    
    def test_crear_cliente_sin_token_falla(self, client):
        """Prueba que crear cliente sin token falla"""
        # Arrange
        cliente_data = {
            "Cedula_Cliente": "1234567890",
            "Nombre": "Juan Pérez",
            "Telefono": "3001234567",
            "Correo": "juan@example.com"
        }
        
        # Act
        response = client.post("/clientes/", json=cliente_data)
        
        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_crear_cliente_via_api(self, client, headers_usuario):
        """Prueba crear un cliente a través de la API con token"""
        # Arrange
        cliente_data = {
            "Cedula_Cliente": "1234567890",
            "Nombre": "Juan Pérez",
            "Telefono": "3001234567",
            "Correo": "juan@example.com"
        }
        
        # Act
        response = client.post(
            "/clientes/", 
            json=cliente_data, 
            headers=headers_usuario
        )
        
        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert "cliente creado correctamente" in data["detail"].lower()
        assert data["data"]["Cedula_Cliente"] == "1234567890"
        assert data["data"]["Nombre"] == "Juan Pérez"
        assert data["data"]["Telefono"] == "3001234567"
        assert data["data"]["Correo"] == "juan@example.com"
    
    def test_crear_cliente_falla_sin_datos_requeridos(self, client, headers_usuario):
        """Prueba que crear cliente sin datos requeridos falla"""
        # Arrange
        cliente_data_incompleto = {
            "Nombre": "Juan Pérez"
            # Falta Cedula_Cliente que es requerido
        }
        
        # Act
        response = client.post(
            "/clientes/", 
            json=cliente_data_incompleto,
            headers=headers_usuario
        )
        
        # Assert
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_crear_cliente_falla_con_cedula_duplicada(self, client, headers_usuario):
        """Prueba que crear cliente con cédula duplicada falla"""
        # Arrange
        cliente_data = {
            "Cedula_Cliente": "1234567890",
            "Nombre": "Juan Pérez",
            "Telefono": "3001234567",
            "Correo": "juan@example.com"
        }
        
        # Crear el primer cliente
        client.post("/clientes/", json=cliente_data, headers=headers_usuario)
        
        # Intentar crear otro cliente con la misma cédula
        cliente_data_duplicado = {
            "Cedula_Cliente": "1234567890",
            "Nombre": "Otro Cliente",
            "Telefono": "3009876543",
            "Correo": "otro@example.com"
        }
        
        # Act
        response = client.post(
            "/clientes/", 
            json=cliente_data_duplicado,
            headers=headers_usuario
        )
        
        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_crear_cliente_falla_con_correo_duplicado(self, client, headers_usuario):
        """Prueba que crear cliente con correo duplicado falla"""
        # Arrange
        cliente_data = {
            "Cedula_Cliente": "1234567890",
            "Nombre": "Juan Pérez",
            "Telefono": "3001234567",
            "Correo": "juan@example.com"
        }
        
        # Crear el primer cliente
        client.post("/clientes/", json=cliente_data, headers=headers_usuario)
        
        # Intentar crear otro cliente con el mismo correo
        cliente_data_duplicado = {
            "Cedula_Cliente": "0987654321",
            "Nombre": "Otro Cliente",
            "Telefono": "3009876543",
            "Correo": "juan@example.com"
        }
        
        # Act
        response = client.post(
            "/clientes/", 
            json=cliente_data_duplicado,
            headers=headers_usuario
        )
        
        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_obtener_cliente_por_id(self, client, headers_usuario, cliente_ejemplo):
        """Prueba obtener un cliente por ID"""
        # Arrange
        cliente_id = str(cliente_ejemplo.Id_Cliente)
        
        # Act
        response = client.get(
            f"/clientes/{cliente_id}",
            headers=headers_usuario
        )
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "cliente encontrado" in data["detail"].lower()
        assert data["data"]["Nombre"] == cliente_ejemplo.Nombre
        assert data["data"]["Cedula_Cliente"] == cliente_ejemplo.Cedula_Cliente
    
    def test_obtener_cliente_por_id_sin_token_falla(self, client, cliente_ejemplo):
        """Prueba que obtener cliente sin token falla"""
        # Arrange
        cliente_id = str(cliente_ejemplo.Id_Cliente)
        
        # Act
        response = client.get(f"/clientes/{cliente_id}")
        
        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_obtener_cliente_por_id_no_existente(self, client, headers_usuario):
        """Prueba obtener un cliente con ID inexistente"""
        # Arrange
        cliente_id_inexistente = str(uuid4())
        
        # Act
        response = client.get(
            f"/clientes/{cliente_id_inexistente}",
            headers=headers_usuario
        )
        
        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "cliente no encontrado" in response.json()["detail"].lower()
    
    def test_actualizar_cliente_via_api(self, client, headers_usuario, cliente_ejemplo):
        """Prueba actualizar un cliente a través de la API"""
        # Arrange
        cliente_id = str(cliente_ejemplo.Id_Cliente)
        
        # Datos de actualización
        update_data = {
            "Cedula_Cliente": cliente_ejemplo.Cedula_Cliente,
            "Nombre": "Juan Pérez Actualizado",
            "Telefono": "3009876543",
            "Correo": "juan_actualizado@example.com"
        }
        
        # Act
        response = client.put(
            f"/clientes/{cliente_id}", 
            json=update_data,
            headers=headers_usuario
        )
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "cliente actualizado correctamente" in data["detail"].lower()
        assert data["data"]["Nombre"] == "Juan Pérez Actualizado"
        assert data["data"]["Correo"] == "juan_actualizado@example.com"
    
    def test_actualizar_cliente_sin_token_falla(self, client, cliente_ejemplo):
        """Prueba que actualizar cliente sin token falla"""
        # Arrange
        cliente_id = str(cliente_ejemplo.Id_Cliente)
        update_data = {
            "Cedula_Cliente": "1234567890",
            "Nombre": "Nuevo Nombre",
            "Telefono": "3001234567",
            "Correo": "nuevo@example.com"
        }
        
        # Act
        response = client.put(f"/clientes/{cliente_id}", json=update_data)
        
        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_actualizar_cliente_no_existente(self, client, headers_usuario):
        """Prueba actualizar un cliente que no existe"""
        # Arrange
        cliente_id_inexistente = str(uuid4())
        
        update_data = {
            "Cedula_Cliente": "1234567890",
            "Nombre": "Cliente Inexistente",
            "Telefono": "3001234567",
            "Correo": "inexistente@example.com"
        }
        
        # Act
        response = client.put(
            f"/clientes/{cliente_id_inexistente}", 
            json=update_data,
            headers=headers_usuario
        )
        
        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "cliente no encontrado" in response.json()["detail"].lower()
    
    def test_eliminar_cliente_via_api(self, client, headers_usuario, cliente_ejemplo):
        """Prueba eliminar un cliente a través de la API"""
        # Arrange
        cliente_id = str(cliente_ejemplo.Id_Cliente)
        
        # Act
        response = client.delete(
            f"/clientes/{cliente_id}",
            headers=headers_usuario
        )
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "cliente eliminado correctamente" in data["detail"].lower()
        
        # Verificar que el cliente ya no existe
        get_response = client.get(
            f"/clientes/{cliente_id}",
            headers=headers_usuario
        )
        assert get_response.status_code == status.HTTP_404_NOT_FOUND
    
    def test_eliminar_cliente_sin_token_falla(self, client, cliente_ejemplo):
        """Prueba que eliminar cliente sin token falla"""
        # Arrange
        cliente_id = str(cliente_ejemplo.Id_Cliente)
        
        # Act
        response = client.delete(f"/clientes/{cliente_id}")
        
        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_eliminar_cliente_no_existente(self, client, headers_usuario):
        """Prueba eliminar un cliente que no existe"""
        # Arrange
        cliente_id_inexistente = str(uuid4())
        
        # Act
        response = client.delete(
            f"/clientes/{cliente_id_inexistente}",
            headers=headers_usuario
        )
        
        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "cliente no encontrado" in response.json()["detail"].lower()
    
    def test_obtener_todos_los_clientes(self, client, headers_usuario):
        """Prueba obtener todos los clientes registrados"""
        # Arrange: Crear varios clientes
        clientes_data = [
            {
                "Cedula_Cliente": "1234567890",
                "Nombre": "Juan Pérez",
                "Telefono": "3001234567",
                "Correo": "juan@example.com"
            },
            {
                "Cedula_Cliente": "0987654321",
                "Nombre": "María López",
                "Telefono": "3009876543",
                "Correo": "maria@example.com"
            },
            {
                "Cedula_Cliente": "1122334455",
                "Nombre": "Carlos Ruiz",
                "Telefono": "3005551234",
                "Correo": "carlos@example.com"
            }
        ]
        
        for cliente_data in clientes_data:
            client.post("/clientes/", json=cliente_data, headers=headers_usuario)
        
        # Act
        response = client.get("/clientes/", headers=headers_usuario)
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        clientes = response.json()
        assert len(clientes) == 3
        
        # Verificar que todos los nombres están presentes
        nombres = [cliente["Nombre"] for cliente in clientes]
        assert "Juan Pérez" in nombres
        assert "María López" in nombres
        assert "Carlos Ruiz" in nombres
    
    def test_token_invalido_falla(self, client):
        """Prueba que un token inválido falla"""
        # Arrange
        headers_invalidos = {"Authorization": "Bearer token_falso_123"}
        cliente_data = {
            "Cedula_Cliente": "1234567890",
            "Nombre": "Juan Pérez",
            "Telefono": "3001234567",
            "Correo": "juan@example.com"
        }
        
        # Act
        response = client.post(
            "/clientes/", 
            json=cliente_data,
            headers=headers_invalidos
        )
        
        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED