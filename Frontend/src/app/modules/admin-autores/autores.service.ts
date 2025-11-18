import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

export interface AutorResponse {
  Id_Autor: string;
  Cedula_Autor: string;
  Nombre: string;
  Telefono: string;
  Edad: string;  // ← Todo es string
}

export interface AutorCreate {
  Cedula_Autor: string;
  Nombre: string;
  Telefono: string;
  Edad: string;  // Se mantiene como string para el formulario
}

@Injectable({
  providedIn: 'root'
})
export class AutoresService {
  private apiUrl = 'http://127.0.0.1:8000/autores/autores';  // ← Sin / al final

  constructor(private http: HttpClient) {}

  getAutores(): Observable<AutorResponse[]> {
    return this.http.get<AutorResponse[]>(`${this.apiUrl}/`).pipe(
      tap((response) => {
        console.log('🔍 Respuesta bruta del backend:', response);
        console.log('¿Es array?', Array.isArray(response));
      })
    );
  }

  getAutor(id: string): Observable<AutorResponse> {
    return this.http.get<AutorResponse>(`${this.apiUrl}/${id}/`);
  }

  createAutor(autor: AutorCreate): Observable<AutorResponse> {
    console.log('🔵 SERVICE - Creando autor:', autor);
    
    const payload = {
      Cedula_Autor: autor.Cedula_Autor,
      Nombre: autor.Nombre,
      Telefono: autor.Telefono,
      Edad: autor.Edad  // ← Mantener como string
    };
    
    console.log('📤 SERVICE - Payload transformado:', payload);
    
    return this.http.post<AutorResponse>(`${this.apiUrl}/`, payload).pipe(
      tap(response => console.log('✅ Respuesta exitosa:', response)),
      tap({
        error: err => {
          console.error('❌ Error en POST:', err);
          console.error('❌ Status:', err.status);
          console.error('❌ Body:', err.error);
        }
      })
    );
  }

  updateAutor(id: string, autor: AutorCreate): Observable<AutorResponse> {
    console.log('🟡 SERVICE - Actualizando autor:', { id, autor });
    
    const payload = {
      Cedula_Autor: autor.Cedula_Autor,
      Nombre: autor.Nombre,
      Telefono: autor.Telefono,
      Edad: autor.Edad  // ← Mantener como string
    };
    
    console.log('📤 SERVICE - URL:', `${this.apiUrl}/${id}/`);
    console.log('📤 SERVICE - Payload:', payload);
    
    return this.http.put<AutorResponse>(`${this.apiUrl}/${id}/`, payload).pipe(
      tap(response => console.log('✅ Update exitoso:', response)),
      tap({
        error: err => {
          console.error('❌ Error en PUT:', err);
          console.error('❌ Status:', err.status);
          console.error('❌ Body:', err.error);
          console.error('❌ Detail completo:', JSON.stringify(err.error, null, 2));
        }
      })
    );
  }

  deleteAutor(id: string): Observable<any> {
    console.log('🔴 SERVICE - Eliminando autor ID:', id);
    return this.http.delete(`${this.apiUrl}/${id}/`).pipe(
      tap(() => console.log('✅ Eliminación exitosa')),
      tap({
        error: err => console.error('❌ Error en DELETE:', err)
      })
    );
  }
}