"""
Pruebas para los endpoints de Autenticación
Con autenticación JWT real - Sin modificar el backend
"""

import pytest
from fastapi import status


class TestAuthAPI:
    """Pruebas para los endpoints de autenticación"""

    # ============================
    # REGISTER
    # ============================

    def test_register_usuario(self, client):
        """Debe permitir registrar un usuario nuevo"""

        # Arrange
        user_data = {
            "Username": "usuario_test",
            "Correo": "test@example.com",
            "Telefono": "3000000000",
            "Nombre": "Usuario Test",
            "Password": "123456",
            "Rol": "USER",
        }

        # Act
        response = client.post("/auth/register", json=user_data)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["Username"] == user_data["Username"]
        assert data["Correo"] == user_data["Correo"]
        assert "Id_Usuario" in data

    def test_register_falla_sin_datos(self, client):
        """Debe fallar si faltan campos obligatorios"""

        # Arrange
        user_data = {
            "Username": "incompleto"
        }

        # Act
        response = client.post("/auth/register", json=user_data)

        # Assert
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # ============================
    # LOGIN
    # ============================

    def test_login_correcto(self, client, usuario_ejemplo):
        """Debe permitir login correcto devolviendo token"""

        # Act
        response = client.post(
            "/auth/login",
            data={
                "username": usuario_ejemplo.Username,
                "password": "123456"
            },
        )

        # Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert data["user"]["Username"] == usuario_ejemplo.Username

    def test_login_incorrecto(self, client):
        """Debe fallar con credenciales erróneas"""

        # Act
        response = client.post(
            "/auth/login",
            data={"username": "no_existe", "password": "incorrecta"},
        )

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "credenciales" in response.json()["detail"].lower()

    def test_login_sin_form_falla(self, client):
        """Debe fallar si no se envían datos del form"""

        # Act
        response = client.post("/auth/login", json={})

        # Assert
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # ============================
    # /auth/me
    # ============================

    def test_obtener_usuario_actual_con_token(self, client, headers_usuario, usuario_ejemplo):
        """Debe devolver la información del usuario autenticado"""

        # Act
        response = client.get("/auth/me", headers=headers_usuario)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data["Username"] == usuario_ejemplo.Username
        assert data["Correo"] == usuario_ejemplo.Correo

    def test_obtener_usuario_actual_sin_token_falla(self, client):
        """Debe fallar si no se envía token"""

        response = client.get("/auth/me")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_obtener_usuario_actual_token_invalido_falla(self, client):
        """Debe fallar si el token es inválido"""

        headers_invalidos = {"Authorization": "Bearer token_invalido_123"}

        response = client.get("/auth/me", headers=headers_invalidos)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
