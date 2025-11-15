import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

// Interfaz para crear/editar libro
export interface LibroCreate {
  Codigo_Libro: string;
  Titulo: string;
  Año?: string | null;
  Precio?: number | null;
  Id_Autor: string;
  Id_Editorial: string;
}

// Interfaz para la respuesta del backend
export interface LibroResponse extends LibroCreate {
  Id_Libro: string;
  Id_usuario_creacion?: string | null;
  Id_usuario_actualizacion?: string | null;
  Fecha_creacion?: string | null;
  Fecha_actualizacion?: string | null;
}

@Injectable({
  providedIn: 'root'
})
export class LibrosService {
  private apiUrl = 'http://127.0.0.1:8000/libros/libros';

  constructor(private http: HttpClient) {}

  getLibros(): Observable<LibroResponse[]> {
    return this.http.get<LibroResponse[]>(this.apiUrl).pipe(
      tap((response) => {
        console.log('🔍 Respuesta bruta del backend:', response);
        console.log('¿Es array?', Array.isArray(response));
        
        // Si no es un array, posiblemente está dentro de una propiedad
        if (response && typeof response === 'object' && !Array.isArray(response)) {
          console.log('⚠️ No es array directo. Propiedades disponibles:', Object.keys(response));
        }
      })
    );
  }

  getLibro(id: string): Observable<LibroResponse> {
    return this.http.get<LibroResponse>(`${this.apiUrl}/${id}`);
  }

  createLibro(libro: LibroCreate): Observable<LibroResponse> {
    return this.http.post<LibroResponse>(this.apiUrl, libro);
  }

  updateLibro(id: string, libro: LibroCreate): Observable<LibroResponse> {
    return this.http.put<LibroResponse>(`${this.apiUrl}/${id}`, libro);
  }

  deleteLibro(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }
}