"""
Pruebas para los endpoints de la API de autores
"""
import pytest
from fastapi import status


class TestAutorAPI:
    """Pruebas para los endpoints de autores"""
    
    def test_obtener_autores_vacio(self, client):
        """Prueba obtener lista de autores cuando está vacía"""
        # Act
        response = client.get("/autores/")
        
        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "no hay autores registrados" in response.json()["detail"].lower()
    
    def test_crear_autor_via_api(self, client):
        """Prueba crear un autor a través de la API"""
        # Arrange
        autor_data = {
            "Cedula_Autor": "1234567890",
            "Nombre": "Gabriel García Márquez",
            "Telefono": "3001234567",
            "Edad": "95"
        }
        
        # Act
        response = client.post("/autores/autores/", json=autor_data)
        
        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert "autor creado correctamente" in data["detail"].lower()
        assert data["Cuerpo de la respuesta"]["Cédula"] == "1234567890"
        assert data["Cuerpo de la respuesta"]["Nombre"] == "Gabriel García Márquez"
        assert data["Cuerpo de la respuesta"]["Teléfono"] == "3001234567"
        assert data["Cuerpo de la respuesta"]["Edad"] == "95"
    
    def test_crear_autor_falla_sin_datos_requeridos(self, client):
        """Prueba que crear autor sin datos requeridos falla"""
        # Arrange
        autor_data_incompleto = {
            "Nombre": "Gabriel García Márquez"
            # Falta Cedula_Autor que es requerido
        }
        
        # Act
        response = client.post("/autores/autores/", json=autor_data_incompleto)
        
        # Assert
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_crear_autor_falla_con_cedula_duplicada(self, client):
        """Prueba que crear autor con cédula duplicada falla"""
        # Arrange
        autor_data = {
            "Cedula_Autor": "1234567890",
            "Nombre": "Gabriel García Márquez",
            "Telefono": "3001234567",
            "Edad": "95"
        }
        
        # Crear el primer autor
        client.post("/autores/autores/", json=autor_data)
        
        # Intentar crear otro autor con la misma cédula
        autor_data_duplicado = {
            "Cedula_Autor": "1234567890",  # Cédula duplicada
            "Nombre": "Otro Autor",
            "Telefono": "3009876543",
            "Edad": "50"
        }
        
        # Act
        response = client.post("/autores/autores/", json=autor_data_duplicado)
        
        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_obtener_autor_por_id(self, client, autor_ejemplo):
        """Prueba obtener un autor por ID"""
        # Arrange
        autor_id = str(autor_ejemplo.Id_Autor)
        
        # Act
        response = client.get(f"/autores/autores/{autor_id}")
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "autor encontrado" in data["detail"].lower()
        assert data["data"]["ID del Autor"] == autor_id
        assert data["data"]["Nombre"] == autor_ejemplo.Nombre
    
    def test_obtener_autor_por_id_no_existente(self, client):
        """Prueba obtener un autor con ID inexistente"""
        # Arrange
        from uuid import uuid4
        autor_id_inexistente = str(uuid4())
        
        # Act
        response = client.get(f"/autores/autores/{autor_id_inexistente}")
        
        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "autor no encontrado" in response.json()["detail"].lower()
    
    def test_actualizar_autor_via_api(self, client, autor_ejemplo):
        """Prueba actualizar un autor a través de la API"""
        # Arrange
        autor_id = str(autor_ejemplo.Id_Autor)
        
        # Datos de actualización
        update_data = {
            "Cedula_Autor": autor_ejemplo.Cedula_Autor,  # Debe mantenerse igual
            "Nombre": "Gabriel José de la Concordia García Márquez",
            "Telefono": "3009876543",
            "Edad": "95"
        }
        
        # Act
        response = client.put(f"/autores/autores/{autor_id}", json=update_data)
        
        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert "autor actualizado correctamente" in data["detail"].lower()
        assert data["data"]["Nombre"] == "Gabriel José de la Concordia García Márquez"
        assert data["data"]["Teléfono"] == "3009876543"
    
    def test_actualizar_autor_no_existente(self, client):
        """Prueba actualizar un autor que no existe"""
        # Arrange
        from uuid import uuid4
        autor_id_inexistente = str(uuid4())
        
        update_data = {
            "Cedula_Autor": "1234567890",
            "Nombre": "Autor Inexistente",
            "Telefono": "3001234567",
            "Edad": "50"
        }
        
        # Act
        response = client.put(f"/autores/autores/{autor_id_inexistente}", json=update_data)
        
        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "autor no encontrado" in response.json()["detail"].lower()
    
    def test_eliminar_autor_via_api(self, client, autor_ejemplo):
        """Prueba eliminar un autor a través de la API"""
        # Arrange
        autor_id = str(autor_ejemplo.Id_Autor)
        
        # Act
        response = client.delete(f"/autores/autores/{autor_id}")
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "autor eliminado correctamente" in data["detail"].lower()
        assert data["data"]["ID del Autor"] == autor_id
        
        # Verificar que el autor ya no existe
        get_response = client.get(f"/autores/autores/{autor_id}")
        assert get_response.status_code == status.HTTP_404_NOT_FOUND
    
    def test_eliminar_autor_no_existente(self, client):
        """Prueba eliminar un autor que no existe"""
        # Arrange
        from uuid import uuid4
        autor_id_inexistente = str(uuid4())
        
        # Act
        response = client.delete(f"/autores/autores/{autor_id_inexistente}")
        
        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "autor no encontrado" in response.json()["detail"].lower()
    
    def test_obtener_todos_los_autores(self, client):
        """Prueba obtener todos los autores registrados"""
        # Arrange: Crear varios autores
        autores_data = [
            {
                "Cedula_Autor": "1234567890",
                "Nombre": "Gabriel García Márquez",
                "Telefono": "3001234567",
                "Edad": "95"
            },
            {
                "Cedula_Autor": "0987654321",
                "Nombre": "Jorge Luis Borges",
                "Telefono": "3009876543",
                "Edad": "86"
            },
            {
                "Cedula_Autor": "1122334455",
                "Nombre": "Pablo Neruda",
                "Telefono": "3005551234",
                "Edad": "69"
            }
        ]
        
        for autor_data in autores_data:
            client.post("/autores/autores/", json=autor_data)
        
        # Act
        response = client.get("/autores/autores/")
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        autores = response.json()
        assert len(autores) == 3
        
        # Verificar que todos los nombres están presentes
        nombres = [autor["Nombre"] for autor in autores]
        assert "Gabriel García Márquez" in nombres
        assert "Jorge Luis Borges" in nombres
        assert "Pablo Neruda" in nombres
    
    def test_validacion_campos_autor(self, client):
        """Prueba validación de campos del autor"""
        # Arrange: Datos con campos inválidos
        autor_data_invalido = {
            "Cedula_Autor": "",  # Cédula vacía
            "Nombre": "",  # Nombre vacío
            "Telefono": "3001234567",
            "Edad": "95"
        }
        
        # Act
        response = client.post("/autores/autores/", json=autor_data_invalido)
        
        # Assert
        # Debería fallar por validación (400 o 422)
        assert response.status_code in [
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        ]