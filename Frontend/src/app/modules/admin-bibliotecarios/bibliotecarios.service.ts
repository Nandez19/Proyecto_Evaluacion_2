import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

export interface BibliotecarioResponse {
  Id_Bibliotecario: string;
  Cedula_Bibliotecario: string;
  Nombre: string;
  Telefono: string;
  Edad: string;
}

export interface BibliotecarioCreate {
  Cedula_Bibliotecario: string;
  Nombre: string;
  Telefono: string;
  Edad: string;
}

@Injectable({
  providedIn: 'root'
})
export class BibliotecariosService {
  // ⚠️ Importante: Cambia 'autores' por 'bibliotecarios' en la URL
  private apiUrl = 'http://127.0.0.1:8000/bibliotecarios/bibliotecarios/';

  constructor(private http: HttpClient) {}

  getBibliotecarios(): Observable<BibliotecarioResponse[]> {
    return this.http.get<BibliotecarioResponse[]>(this.apiUrl).pipe(
      tap((response) => {
        console.log('🔍 Respuesta bruta del backend:', response);
        console.log('¿Es array?', Array.isArray(response));
        
        if (response && typeof response === 'object' && !Array.isArray(response)) {
          console.log('⚠️ No es array directo. Propiedades disponibles:', Object.keys(response));
        }
      })
    );
  }

  getBibliotecario(id: string): Observable<BibliotecarioResponse> {
    return this.http.get<BibliotecarioResponse>(`${this.apiUrl}${id}`);
  }

  createBibliotecario(bibliotecario: BibliotecarioCreate): Observable<BibliotecarioResponse> {
  console.log('🔵 SERVICE - Datos recibidos:', bibliotecario);
  console.log('🔵 SERVICE - URL completa:', this.apiUrl);
  console.log('🔵 SERVICE - Tipos de datos:', {
    Cedula_Bibliotecario: typeof bibliotecario.Cedula_Bibliotecario,
    Nombre: typeof bibliotecario.Nombre,
    Telefono: typeof bibliotecario.Telefono,
    Edad: typeof bibliotecario.Edad
  });
  
  return this.http.post<BibliotecarioResponse>(this.apiUrl, bibliotecario).pipe(
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

  updateBibliotecario(id: string, bibliotecario: BibliotecarioCreate): Observable<BibliotecarioResponse> {
    return this.http.put<BibliotecarioResponse>(`${this.apiUrl}${id}`, bibliotecario);
  }

  deleteBibliotecario(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}${id}`);
  }
}