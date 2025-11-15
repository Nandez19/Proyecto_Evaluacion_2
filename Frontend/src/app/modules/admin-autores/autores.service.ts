import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

export interface AutorResponse {
  Id_Autor: string;
  Cedula_Autor: string;
  Nombre: string;
  Telefono: string;
  Edad: string;
}

export interface AutorCreate {
  Cedula_Autor: string;
  Nombre: string;
  Telefono: string;
  Edad: string;
}

@Injectable({
  providedIn: 'root'
})
export class AutoresService {
  private apiUrl = 'http://127.0.0.1:8000/autores/autores/';  // ← Agrega la / al final

  constructor(private http: HttpClient) {}

  getAutores(): Observable<AutorResponse[]> {
    return this.http.get<AutorResponse[]>(this.apiUrl).pipe(
      tap((response) => {
        console.log('🔍 Respuesta bruta del backend:', response);
        console.log('¿Es array?', Array.isArray(response));
        
        if (response && typeof response === 'object' && !Array.isArray(response)) {
          console.log('⚠️ No es array directo. Propiedades disponibles:', Object.keys(response));
        }
      })
    );
  }

  getAutor(id: string): Observable<AutorResponse> {
    return this.http.get<AutorResponse>(`${this.apiUrl}${id}`);  // ← Sin / extra
  }

  createAutor(autor: AutorCreate): Observable<AutorResponse> {
  console.log('🔵 SERVICE - Datos recibidos:', autor);
  console.log('🔵 SERVICE - URL completa:', this.apiUrl);
  console.log('🔵 SERVICE - Tipos de datos:', {
    Cedula_Autor: typeof autor.Cedula_Autor,
    Nombre: typeof autor.Nombre,
    Telefono: typeof autor.Telefono,
    Edad: typeof autor.Edad
  });
  
  return this.http.post<AutorResponse>(this.apiUrl, autor).pipe(
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
    return this.http.put<AutorResponse>(`${this.apiUrl}${id}`, autor);  // ← Sin / extra
  }

  deleteAutor(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}${id}`);  // ← Sin / extra
  }
}