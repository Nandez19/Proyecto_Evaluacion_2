import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private API_URL = 'http://127.0.0.1:8000/auth';
  private currentUser: any = null;

  constructor(private http: HttpClient) {}

  // Método de login
  login(username: string, password: string): Observable<any> {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    return this.http.post(`${this.API_URL}/login`, formData).pipe(
      tap((res: any) => {
        if (res?.access_token) {
          localStorage.setItem('token', res.access_token);
        }
        // También podemos guardar al usuario si la respuesta lo trae
        if (res?.user) {
          this.currentUser = res.user;
        }
      })
    );
  }

  // Obtener token desde el localStorage
  getToken(): string | null {
    return localStorage.getItem('token');
  }

  // Obtener el usuario desde el servicio
  getUser(): any {
    return this.currentUser;
  }

  // Obtener el usuario desde el token JWT (decodificado manualmente)
  getUserFromToken(): any {
    const token = this.getToken();
    if (token) {
      try {
        const decodedToken = this.decodeToken(token);
        return decodedToken?.user || null;
      } catch (error) {
        console.error('Error al decodificar el token', error);
      }
    }
    return null;
  }

  // Logout: eliminar el token y resetear el usuario
  logout(): void {
    localStorage.removeItem('token');
    this.currentUser = null;
  }

  // -----------------------
  // Decodificar el token JWT manualmente
  // -----------------------
  private decodeToken(token: string): any {
    // El JWT está dividido en tres partes: header, payload y signature
    const parts = token.split('.');
    if (parts.length !== 3) {
      throw new Error('El token JWT no es válido');
    }

    const payload = parts[1];
    const decoded = atob(payload); // Decodifica la parte "payload" del JWT
    return JSON.parse(decoded); // Convierte el payload decodificado a un objeto JSON
  }

  // Cargar usuario desde el localStorage al cargar la app
  loadUserFromLocalStorage(): void {
    const token = this.getToken();
    if (token) {
      this.currentUser = this.getUserFromToken();
    }
  }
}








/*import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private API_URL = 'http://127.0.0.1:8000/auth'; 

  constructor(private http: HttpClient) {}

  // Llamada al backend para hacer login
  login(username: string, password: string): Observable<any> {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    return this.http.post(`${this.API_URL}/login`, formData).pipe(
      tap((res: any) => {
        console.log('📦 Respuesta del backend:', res);

        // Guarda el token si existe
        if (res && res.access_token) {
          localStorage.setItem('token', res.access_token);
          console.log('Token guardado en localStorage');
        } else {
          console.warn('No se recibió token en la respuesta del backend');
        }
      })
    );
  }

  // Obtener token almacenado
  getToken(): string | null {
    return localStorage.getItem('token');
  }

  // Eliminar token (logout)
  logout(): void {
    localStorage.removeItem('token');
  }
}*/