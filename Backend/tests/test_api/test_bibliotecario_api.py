"""
Pruebas para los endpoints de la API de bibliotecarios
Con autenticación JWT real - Sin modificar el backend
"""
import pytest
from fastapi import status
from uuid import uuid4

class TestBibliotecarioAPI:
    """Pruebas para los endpoints de bibliotecarios"""
    
    def test_obtener_bibliotecarios_sin_token_falla(self, client):
        
        # Act
        response = client.get("/bibliotecarios/bibliotecarios/")

        # Assert 
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_obtener_bibliotecarios_vacio(self, client, headers_usuario):
       
        #Act
        response = client.get("/bibliotecarios/bibliotecarios/", headers=headers_usuario)

        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "no hay bibliotecarios registrados" in response.json()["detail"].lower()
    
    def test_crear_bibliotecario_sin_token_falla(self, client):
        
        #Arrange
        biblio_data = {
            "Cedula_Bibliotecario": "1234567890",
            "Nombre": "Juan Pérez",
            "Telefono": "3001234567",
            "Edad": "30"
        }

        #Act
        response = client.post("/bibliotecarios/bibliotecarios/", json=biblio_data)

        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_crear_bibliotecario_via_api(self, client, headers_usuario):
        
        #Arrange
        biblio_data = {
            "Cedula_Bibliotecario": "1234567890",
            "Nombre": "Juan Pérez",
            "Telefono": "3001234567",
            "Edad": "30"
        }

        #Act
        response = client.post(
            "/bibliotecarios/bibliotecarios/", 
            json=biblio_data, 
            headers=headers_usuario
        )

        #Assert
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert "bibliotecario creado correctamente" in data["detail"].lower()

    
    def test_crear_bibliotecario_falla_sin_datos_requeridos(self, client, headers_usuario):

        #Arrange
        biblio_data_incompleto = {
            "Nombre": "Juan Pérez"
            # Falta Cedula_Bibliotecario
        }

        #Act
        response = client.post(
            "/bibliotecarios/bibliotecarios/", 
            json=biblio_data_incompleto,
            headers=headers_usuario
        )

        #Assert
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_crear_bibliotecario_falla_con_cedula_duplicada(self, client, headers_usuario):
        
        #Arrange
        biblio_data = {
            "Cedula_Bibliotecario": "1234567890",
            "Nombre": "Juan Pérez",
            "Telefono": "3001234567",
            "Edad": "30"
        }
        
        #Act
        client.post("/bibliotecarios/bibliotecarios/", json=biblio_data, headers=headers_usuario)
        
        # Intentar crear otro con la misma cédula
        biblio_data_duplicado = {
            "Cedula_Bibliotecario": "1234567890",
            "Nombre": "Otro Bibliotecario",
            "Telefono": "3009876543",
            "Edad": "40"
        }
        response = client.post(
            "/bibliotecarios/bibliotecarios/", 
            json=biblio_data_duplicado,
            headers=headers_usuario
        )
        # Si no manejas IntegrityError, esto fallará con 500; ajusta el endpoint para devolver 400
        assert response.status_code == status.HTTP_400_BAD_REQUEST  # O 500 si no se corrige
    
    def test_obtener_bibliotecario_por_id(self, client, headers_usuario, bibliotecario_ejemplo):
        
        #Arrange
        biblio_id = str(bibliotecario_ejemplo.Id_Bibliotecario)  # Convierte UUID a string
        
        #Act
        response = client.get(
            f"/bibliotecarios/bibliotecarios/{biblio_id}",
            headers=headers_usuario
        )

        #Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "bibliotecario encontrado" in data["detail"].lower()
        
    
    def test_obtener_bibliotecario_por_id_sin_token_falla(self, client, bibliotecario_ejemplo):
        
        #Arrange
        biblio_id = str(bibliotecario_ejemplo.Id_Bibliotecario)

        #Act
        response = client.get(f"/bibliotecarios/bibliotecarios/{biblio_id}")

        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_obtener_bibliotecario_por_id_no_existente(self, client, headers_usuario):
        
        #Arrange
        biblio_id_inexistente = str(uuid4())

        #Act
        response = client.get(
            f"/bibliotecarios/bibliotecarios/{biblio_id_inexistente}",
            headers=headers_usuario
        )

        #Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "bibliotecario no encontrado" in response.json()["detail"].lower()
    
    def test_actualizar_bibliotecario_via_api(self, client, headers_usuario, bibliotecario_ejemplo):
        
        #Arrange
        biblio_id = str(bibliotecario_ejemplo.Id_Bibliotecario)
        update_data = {
            "Cedula_Bibliotecario": bibliotecario_ejemplo.Cedula_Bibliotecario,
            "Nombre": "Juan Pérez Actualizado",
            "Telefono": "3009876543",
            "Edad": "35"
        }

        #Act
        response = client.put(
            f"/bibliotecarios/bibliotecarios/{biblio_id}", 
            json=update_data,
            headers=headers_usuario
        )

        #Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "bibliotecario actualizado correctamente" in data["detail"].lower()
        assert data["data"]["Nombre"] == "Juan Pérez Actualizado"
    
    def test_actualizar_bibliotecario_sin_token_falla(self, client, bibliotecario_ejemplo):
        
        #Arrange
        biblio_id = str(bibliotecario_ejemplo.Id_Bibliotecario)
        update_data = {
            "Cedula_Bibliotecario": "1234567890",
            "Nombre": "Nuevo Nombre",
            "Telefono": "3001234567",
            "Edad": "40"
        }

        #Act
        response = client.put(f"/bibliotecarios/bibliotecarios/{biblio_id}", json=update_data)

        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_actualizar_bibliotecario_no_existente(self, client, headers_usuario):
        
        #Arrrange
        biblio_id_inexistente = str(uuid4())
        update_data = {
            "Cedula_Bibliotecario": "1234567890",
            "Nombre": "Bibliotecario Inexistente",
            "Telefono": "3001234567",
            "Edad": "40"
        }

        #Act
        response = client.put(
            f"/bibliotecarios/bibliotecarios/{biblio_id_inexistente}", 
            json=update_data,
            headers=headers_usuario
        )

        #Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "bibliotecario no encontrado" in response.json()["detail"].lower()
    
    def test_eliminar_bibliotecario_via_api(self, client, headers_usuario, bibliotecario_ejemplo):
        
        #Arrange
        biblio_id = str(bibliotecario_ejemplo.Id_Bibliotecario)
        
        
        #Act
        response = client.delete(
            f"/bibliotecarios/bibliotecarios/{biblio_id}",
            headers=headers_usuario
        )

        #Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "bibliotecario eliminado correctamente" in data["detail"].lower()
    
    def test_eliminar_bibliotecario_sin_token_falla(self, client, bibliotecario_ejemplo):
        
        #Arrange
        biblio_id = str(bibliotecario_ejemplo.Id_Bibliotecario)

        #Act
        response = client.delete(f"/bibliotecarios/bibliotecarios/{biblio_id}")
        
        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_eliminar_bibliotecario_no_existente(self, client, headers_usuario):
        
        #Arrange
        biblio_id_inexistente = str(uuid4())

        #Act
        response = client.delete(
            f"/bibliotecarios/bibliotecarios/{biblio_id_inexistente}",
            headers=headers_usuario
        )

        #Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "bibliotecario no encontrado" in response.json()["detail"].lower()
    
    def test_obtener_todos_los_bibliotecarios(self, client, headers_usuario):
        
        #Arrange
        biblios_data = [
            {
                "Cedula_Bibliotecario": "1234567890",
                "Nombre": "Juan Pérez",
                "Telefono": "3001234567",
                "Edad": "30"
            },
            {
                "Cedula_Bibliotecario": "0987654321",
                "Nombre": "María López",
                "Telefono": "3009876543",
                "Edad": "25"
            }
        ]
        for biblio_data in biblios_data:
            client.post("/bibliotecarios/bibliotecarios/", json=biblio_data, headers=headers_usuario)
        
        response = client.get("/bibliotecarios/bibliotecarios/", headers=headers_usuario)
        assert response.status_code == status.HTTP_200_OK
        biblios = response.json()
        assert len(biblios) == 2
        nombres = [b["Nombre"] for b in biblios]
        assert "Juan Pérez" in nombres
        assert "María López" in nombres
    
    def test_token_invalido_falla(self, client):
        
        #Arrange
        headers_invalidos = {"Authorization": "Bearer token_falso_123"}
        biblio_data = {
            "Cedula_Bibliotecario": "1234567890",
            "Nombre": "Juan Pérez",
            "Telefono": "3001234567",
            "Edad": "30"
        }

        #Act
        response = client.post(
            "/bibliotecarios/bibliotecarios/", 
            json=biblio_data,
            headers=headers_invalidos
        )

        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED