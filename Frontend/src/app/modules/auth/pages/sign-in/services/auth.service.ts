import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private API_URL = 'http://127.0.0.1:8000/auth'; // Ajusta si tu ruta base es distinta

  constructor(private http: HttpClient) {}

  // 🔹 Llamada al backend para hacer login
  login(username: string, password: string): Observable<any> {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    return this.http.post(`${this.API_URL}/login`, formData).pipe(
      tap((res: any) => {
        console.log('📦 Respuesta del backend:', res);

        // ✅ Guarda el token si existe
        if (res && res.access_token) {
          localStorage.setItem('token', res.access_token);
          console.log('✅ Token guardado en localStorage');
        } else {
          console.warn('⚠️ No se recibió token en la respuesta del backend');
        }
      })
    );
  }

  // 🔹 Obtener token almacenado
  getToken(): string | null {
    return localStorage.getItem('token');
  }

  // 🔹 Eliminar token (logout)
  logout(): void {
    localStorage.removeItem('token');
  }
}
