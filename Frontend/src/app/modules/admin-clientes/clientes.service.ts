import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

export interface ClienteResponse {
  Id_Cliente: string;
  Cedula_Cliente: string;
  Nombre: string;
  Telefono: string;
  Correo: string; // Adaptado para Correo
}

export interface ClienteCreate {
  Cedula_Cliente: string;
  Nombre: string;
  Telefono: string;
  Correo: string; // Adaptado para Correo
}

@Injectable({
  providedIn: 'root'
})
export class ClientesService {
  // ⚠️ Importante: Cambia 'bibliotecarios' por 'clientes' en la URL
  private apiUrl = 'http://127.0.0.1:8000/clientes/';

  constructor(private http: HttpClient) {}

  getClientes(): Observable<ClienteResponse[]> {
    return this.http.get<ClienteResponse[]>(this.apiUrl).pipe(
      tap((response) => {
        console.log('🔍 Respuesta bruta del backend:', response);
        if (response && typeof response === 'object' && !Array.isArray(response)) {
          console.log('⚠️ No es array directo. Propiedades disponibles:', Object.keys(response));
        }
      })
    );
  }

  getCliente(id: string): Observable<ClienteResponse> {
    return this.http.get<ClienteResponse>(`${this.apiUrl}${id}`);
  }

  createCliente(cliente: ClienteCreate): Observable<ClienteResponse> {
    console.log('🔵 SERVICE - Datos recibidos:', cliente);
    return this.http.post<ClienteResponse>(this.apiUrl, cliente).pipe(
      tap(response => console.log('✅ Respuesta exitosa:', response)),
      tap({
        error: err => {
          console.error('❌ Error en POST:', err);
        }
      })
    );
  }

  updateCliente(id: string, cliente: ClienteCreate): Observable<ClienteResponse> {
    return this.http.put<ClienteResponse>(`${this.apiUrl}${id}`, cliente);
  }

  deleteCliente(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}${id}`);
  }
}