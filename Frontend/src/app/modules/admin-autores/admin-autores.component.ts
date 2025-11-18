import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AutoresService, AutorResponse, AutorCreate } from 'src/app/modules/admin-autores/autores.service';

@Component({
  selector: 'app-admin-autores',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './admin-autores.component.html',
  styleUrls: ['./admin-autores.component.css']
})
export class AdminAutoresComponent implements OnInit {
  autores: AutorResponse[] = [];
  loading = false;
  error: string | null = null;
  
  showModal = false;
  isEditMode = false;
  autorActual: AutorCreate = this.getEmptyAutor();
  idEditando: string | null = null; // ← Solo necesitamos esto

  constructor(
    private autoresService: AutoresService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.cargarAutores();
  }

  cargarAutores(): void {
    this.loading = true;
    this.error = null;
    
    this.autoresService.getAutores().subscribe({
      next: (data) => {
        if (Array.isArray(data)) {
          this.autores = data;
        } else {
          this.autores = [];
        }
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: (err) => {
        this.error = 'No se pudieron cargar los autores';
        this.loading = false;
        this.cdr.detectChanges();
      }
    });
  }

  abrirModalCrear(): void {
    this.isEditMode = false;
    this.idEditando = null;
    this.autorActual = this.getEmptyAutor();
    this.showModal = true;
  }

  abrirModalEditar(autor: AutorResponse): void {
    console.log('✏️ Editando autor:', autor);
    this.isEditMode = true;
    this.idEditando = autor.Id_Autor; // ← Guardamos solo el ID
    
    // autorActual solo contiene los campos editables
    this.autorActual = {
      Cedula_Autor: autor.Cedula_Autor,
      Nombre: autor.Nombre,
      Telefono: autor.Telefono,
      Edad: String(autor.Edad)
    };
    
    this.showModal = true;
  }

  cerrarModal(): void {
    this.showModal = false;
    this.autorActual = this.getEmptyAutor();
    this.idEditando = null;
  }

  guardarAutor(): void {
    console.log('💾 Guardando autor:', this.autorActual);
    
    // Validación básica
    if (!this.autorActual.Cedula_Autor.trim() || 
        !this.autorActual.Nombre.trim() || 
        !this.autorActual.Telefono.trim() || 
        !this.autorActual.Edad) {
      alert('Por favor complete todos los campos');
      return;
    }
    
    const autorParaGuardar: AutorCreate = {
      Cedula_Autor: this.autorActual.Cedula_Autor.trim(),
      Nombre: this.autorActual.Nombre.trim(),
      Telefono: this.autorActual.Telefono.trim(),
      Edad: String(this.autorActual.Edad || '')
    };
    
    console.log('📤 Autor transformado:', autorParaGuardar);
    
    if (this.isEditMode && this.idEditando) {
      // ✅ Usar el ID guardado en lugar de buscar por Cedula_Autor
      console.log('🔄 Actualizando autor con ID:', this.idEditando);
      
      this.autoresService.updateAutor(this.idEditando, autorParaGuardar).subscribe({
        next: () => {
          console.log('✅ Autor actualizado');
          alert('Autor actualizado exitosamente');
          this.cargarAutores();
          this.cerrarModal();
        },
        error: (err) => {
          console.error('❌ Error al actualizar:', err);
          alert('Error al actualizar el autor: ' + (err.error?.detail || err.message));
        }
      });
    } else {
      console.log('➕ Creando nuevo autor');
      
      this.autoresService.createAutor(autorParaGuardar).subscribe({
        next: () => {
          console.log('✅ Autor creado');
          alert('Autor creado exitosamente');
          this.cargarAutores();
          this.cerrarModal();
        },
        error: (err) => {
          console.error('❌ Error al crear:', err);
          alert('Error al crear el autor: ' + (err.error?.detail || err.message));
        }
      });
    }
  }

  eliminarAutor(autor: AutorResponse): void {
    const id = autor.Id_Autor;
    
    if (!id) {
      alert('Error: No se puede identificar el autor');
      return;
    }
    
    if (confirm(`¿Estás seguro de eliminar al autor "${autor.Nombre}"?`)) {
      this.autoresService.deleteAutor(id).subscribe({
        next: () => {
          alert('Autor eliminado exitosamente');
          this.cargarAutores();
        },
        error: (err) => {
          alert('Error al eliminar el autor: ' + (err.error?.detail || err.message));
        }
      });
    }
  }

  private getEmptyAutor(): AutorCreate {
    return {
      Cedula_Autor: '',
      Nombre: '',
      Telefono: '',
      Edad: ''
    };
  }
}