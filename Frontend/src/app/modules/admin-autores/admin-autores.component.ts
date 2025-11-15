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
    this.autorActual = this.getEmptyAutor();
    this.showModal = true;
  }

  abrirModalEditar(autor: AutorResponse): void {
    this.isEditMode = true;
    this.autorActual = {
      Cedula_Autor: autor.Cedula_Autor,
      Nombre: autor.Nombre,
      Telefono: autor.Telefono,
      Edad: String(autor.Edad)  // ← Asegurar que sea string
    };
    this.showModal = true;
  }
  cerrarModal(): void {
    this.showModal = false;
    this.autorActual = this.getEmptyAutor();
  }

  guardarAutor(): void {
  console.log('💾 Guardando autor:', this.autorActual);
  
  // ✅ Asegurar que Edad sea string
  const autorParaGuardar: AutorCreate = {
    Cedula_Autor: this.autorActual.Cedula_Autor.trim(),
    Nombre: this.autorActual.Nombre.trim(),
    Telefono: this.autorActual.Telefono.trim(),
    Edad: String(this.autorActual.Edad || '')  // ← Convertir a string
  };
  
  console.log('📤 Autor transformado:', autorParaGuardar);
  
  if (this.isEditMode) {
    const autor = this.autores.find(a => a.Cedula_Autor === this.autorActual.Cedula_Autor);
    if (autor) {
      this.autoresService.updateAutor(autor.Id_Autor, autorParaGuardar).subscribe({
        next: () => {
          alert('Autor actualizado exitosamente');
          this.cargarAutores();
          this.cerrarModal();
        },
        error: (err) => {
          console.error('Error al actualizar:', err);
          alert('Error al actualizar el autor: ' + (err.error?.detail || err.message));
        }
      });
    }
  } else {
    this.autoresService.createAutor(autorParaGuardar).subscribe({
      next: () => {
        alert('Autor creado exitosamente');
        this.cargarAutores();
        this.cerrarModal();
      },
      error: (err) => {
        console.error('Error al crear:', err);
        alert('Error al crear el autor: ' + (err.error?.detail || err.message));
      }
    });
  }
}
  eliminarAutor(autor: AutorResponse): void {
    // Obtener el ID dinámicamente del objeto
    const id = autor['Id_Autor'];
    
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
          alert('Error al eliminar el autor');
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