import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

export interface UserResponse {
  Id_Usuario: string;
  Username: string;
  Nombre: string;
  Correo: string;
  Telefono: string;
  Rol: string;
  Activo: boolean;
  Fecha_creacion?: string;
  Fecha_actualizacion?: string;
}

export interface UserCreate {
  Username: string;
  Nombre: string;
  Correo: string;
  Telefono: string;
  Rol: string;
  password: string;
}

@Injectable({
  providedIn: 'root'
})
export class UsuariosService {

  private registerUrl = 'http://127.0.0.1:8000/auth/register';
  private meUrl = 'http://127.0.0.1:8000/auth/me';
  private usuariosUrl = 'http://127.0.0.1:8000/usuarios/usuarios';

  constructor(private http: HttpClient) {}


  createUsuario(usuario: UserCreate): Observable<UserResponse> {
    return this.http.post<UserResponse>(this.registerUrl, usuario).pipe(
      tap({
        next: res => console.log('✅ Usuario creado:', res),
        error: err => console.error('❌ Error al crear usuario:', err.error)
      })
    );
  }

 
  getUsuario(): Observable<UserResponse> {
    return this.http.get<UserResponse>(this.meUrl).pipe(
      tap({
        next: res => console.log('🔍 Usuario logeado:', res),
        error: err => console.error('❌ Error al obtener usuario:', err.error)
      })
    );
  }

  
  getUsuarios(): Observable<UserResponse[]> {
    return this.http.get<UserResponse[]>(this.usuariosUrl).pipe(
      tap({
        next: res => console.log('📌 Usuarios cargados:', res),
        error: err => console.error('❌ Error al obtener usuarios:', err.error)
      })
    );
  }
}
