// src/app/modules/editoriales/editoriales.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface EditorialResponse {
  Id_Editorial: string;
  Nombre: string;
  Pais: string;
  Contacto: string;
}

export interface EditorialCreate {
  Nombre: string;
  Pais: string;
  Contacto: string;
}

@Injectable({
  providedIn: 'root'
})
export class EditorialesService {
  private apiUrl = 'http://127.0.0.1:8000/editoriales/editoriales';

  constructor(private http: HttpClient) {}

  getEditoriales(): Observable<EditorialResponse[]> {
    return this.http.get<EditorialResponse[]>(this.apiUrl);
  }

  getEditorial(id: string): Observable<EditorialResponse> {
    return this.http.get<EditorialResponse>(`${this.apiUrl}/${id}`);
  }

  createEditorial(editorial: EditorialCreate): Observable<any> {
    return this.http.post(this.apiUrl, editorial);
  }

  updateEditorial(id: string, editorial: EditorialCreate): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}`, editorial);
  }

  deleteEditorial(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }
}