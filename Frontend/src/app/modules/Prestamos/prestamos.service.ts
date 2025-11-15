import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

export interface PrestamoBase {
  Fecha_Prestamo: string | Date;
  Fecha_Devolucion?: string | Date | null;
  Estado: string;
  Id_Bibliotecario: string;
  Id_Cliente: string;
  Id_Libro: string;
}

export interface PrestamoCreate extends PrestamoBase {}

export interface PrestamoResponse extends PrestamoBase {
  Id_Prestamo: string;
  Id_usuario_creacion?: string | null;
  Id_usuario_actualizacion?: string | null;
  Fecha_creacion?: string | Date | null;
  Fecha_actualizacion?: string | Date | null;
}

@Injectable({
  providedIn: 'root'
})
export class PrestamosService {

  private apiUrl = 'http://127.0.0.1:8000/prestamos/prestamos/';

  constructor(private http: HttpClient) {}

  /* ---------- GET TODOS ---------- */
  getPrestamos(): Observable<{ data: PrestamoResponse[], detail: string }> {
    return this.http.get<{ data: PrestamoResponse[], detail: string }>(this.apiUrl)
      .pipe(tap(resp => console.log('📄 Listado de préstamos:', resp)));
  }

  /* ---------- GET UNO ---------- */
  getPrestamo(id: string): Observable<PrestamoResponse> {
    return this.http.get<PrestamoResponse>(`${this.apiUrl}${id}/`);
  }

  /* ---------- CREATE ---------- */
  createPrestamo(prestamo: PrestamoCreate): Observable<PrestamoResponse> {
    console.log('📦 Enviando POST:', prestamo);
    return this.http.post<PrestamoResponse>(this.apiUrl, prestamo)
      .pipe(tap(response => console.log('✅ Préstamo creado:', response)));
  }

  /* ---------- UPDATE ---------- */
  updatePrestamo(id: string, prestamo: PrestamoCreate): Observable<PrestamoResponse> {
    return this.http.put<PrestamoResponse>(`${this.apiUrl}${id}/`, prestamo);
  }

  /* ---------- DELETE ---------- */
  deletePrestamo(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}${id}/`);
  }
}
