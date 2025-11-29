"""
Pruebas para los endpoints de Editoriales
Con autenticación JWT real - Sin modificar el backend
"""
import pytest
from fastapi import status
from uuid import uuid4, UUID


class TestEditorialAPI:
    """Pruebas para los endpoints de editoriales"""

    # ============================
    # LISTAR EDITORIALES
    # ============================

    def test_obtener_editoriales_sin_token_falla(self, client):
        response = client.get("/editoriales/editoriales/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_obtener_editoriales_vacio(self, client, headers_usuario):
        response = client.get("/editoriales/editoriales/", headers=headers_usuario)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "no hay editoriales registradas" in response.json()["detail"].lower()

    # ============================
    # CREAR
    # ============================

    def test_crear_editorial_sin_token_falla(self, client):
        editorial_data = {
            "Nombre": "Planeta",
            "Pais": "España",
            "Contacto": "info@planeta.com",
        }

        response = client.post("/editoriales/editoriales/", json=editorial_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_crear_editorial_via_api(self, client, headers_usuario):
        editorial_data = {
            "Nombre": "Planeta",
            "Pais": "España",
            "Contacto": "info@planeta.com",
        }

        response = client.post(
            "/editoriales/editoriales/",
            json=editorial_data,
            headers=headers_usuario,
        )

        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert "editorial creada correctamente" in data["detail"].lower()

    def test_crear_editorial_falla_sin_datos_requeridos(self, client, headers_usuario):
        editorial_data_incompleto = {"Pais": "Colombia"}  # Falta Nombre

        response = client.post(
            "/editoriales/editoriales/",
            json=editorial_data_incompleto,
            headers=headers_usuario,
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # ============================
    # OBTENER POR ID
    # ============================

    def test_obtener_editorial_por_id(self, client, headers_usuario, editorial_ejemplo):
        editorial_id = editorial_ejemplo.Id_Editorial  # UUID real

        response = client.get(
            f"/editoriales/editoriales/{editorial_id}",
            headers=headers_usuario,
        )

        assert response.status_code == status.HTTP_200_OK
        assert "editorial encontrada" in response.json()["detail"].lower()

    def test_obtener_editorial_por_id_sin_token_falla(self, client, editorial_ejemplo):
        editorial_id = editorial_ejemplo.Id_Editorial

        response = client.get(f"/editoriales/editoriales/{editorial_id}")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_obtener_editorial_por_id_no_existente(self, client, headers_usuario):
        editorial_id_inexistente = uuid4()  # UUID real, NO str()

        response = client.get(
            f"/editoriales/editoriales/{editorial_id_inexistente}",
            headers=headers_usuario,
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "editorial no encontrada" in response.json()["detail"].lower()

    # ============================
    # ACTUALIZAR
    # ============================

    def test_actualizar_editorial_via_api(self, client, headers_usuario, editorial_ejemplo):
        editorial_id = editorial_ejemplo.Id_Editorial

        update_data = {
            "Nombre": "Planeta Actualizada",
            "Pais": "México",
            "Contacto": "contacto@planeta.mx",
        }

        response = client.put(
            f"/editoriales/editoriales/{editorial_id}",
            json=update_data,
            headers=headers_usuario,
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "editorial actualizada correctamente" in data["detail"].lower()
        assert data["data"]["Nombre"] == "Planeta Actualizada"

    def test_actualizar_editorial_sin_token_falla(self, client, editorial_ejemplo):
        editorial_id = editorial_ejemplo.Id_Editorial

        update_data = {
            "Nombre": "Nueva Editorial",
            "Pais": "Chile",
            "Contacto": "hola@editorial.cl",
        }

        response = client.put(
            f"/editoriales/editoriales/{editorial_id}",
            json=update_data,
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_actualizar_editorial_no_existente(self, client, headers_usuario):
        editorial_id_inexistente = uuid4()

        update_data = {
            "Nombre": "Editorial Fantasma",
            "Pais": "Perú",
            "Contacto": "fantasma@editorial.pe",
        }

        response = client.put(
            f"/editoriales/editoriales/{editorial_id_inexistente}",
            json=update_data,
            headers=headers_usuario,
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "editorial no encontrada" in response.json()["detail"].lower()

    # ============================
    # ELIMINAR
    # ============================

    def test_eliminar_editorial_via_api(self, client, headers_usuario, editorial_ejemplo):
        editorial_id = editorial_ejemplo.Id_Editorial

        response = client.delete(
            f"/editoriales/editoriales/{editorial_id}",
            headers=headers_usuario,
        )

        assert response.status_code == status.HTTP_200_OK
        assert "editorial eliminada correctamente" in response.json()["detail"].lower()

    def test_eliminar_editorial_sin_token_falla(self, client, editorial_ejemplo):
        editorial_id = editorial_ejemplo.Id_Editorial

        response = client.delete(f"/editoriales/editoriales/{editorial_id}")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_eliminar_editorial_no_existente(self, client, headers_usuario):
        editorial_id_inexistente = uuid4()

        response = client.delete(
            f"/editoriales/editoriales/{editorial_id_inexistente}",
            headers=headers_usuario,
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "editorial no encontrada" in response.json()["detail"].lower()

    # ============================
    # OBTENER TODAS
    # ============================

    def test_obtener_todas_las_editoriales(self, client, headers_usuario):
        editoriales_data = [
            {
                "Nombre": "Planeta",
                "Pais": "España",
                "Contacto": "info@planeta.com",
            },
            {
                "Nombre": "Alfaguara",
                "Pais": "México",
                "Contacto": "contacto@alfaguara.mx",
            },
        ]

        for ed in editoriales_data:
            client.post(
                "/editoriales/editoriales/",
                json=ed,
                headers=headers_usuario,
            )

        response = client.get("/editoriales/editoriales/", headers=headers_usuario)
        assert response.status_code == status.HTTP_200_OK

        editoriales = response.json()
        assert len(editoriales) == 2

        nombres = [e["Nombre"] for e in editoriales]
        assert "Planeta" in nombres
        assert "Alfaguara" in nombres

    # ============================
    # TOKEN INVÁLIDO
    # ============================

    def test_token_invalido_falla(self, client):
        headers_invalidos = {"Authorization": "Bearer token_falso_123"}

        editorial_data = {
            "Nombre": "Planeta",
            "Pais": "España",
            "Contacto": "info@planeta.com",
        }

        response = client.post(
            "/editoriales/editoriales/",
            json=editorial_data,
            headers=headers_invalidos,
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
