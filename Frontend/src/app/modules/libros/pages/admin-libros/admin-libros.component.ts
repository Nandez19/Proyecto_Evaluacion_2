import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { LibrosService, LibroResponse, LibroCreate } from '../../libros.service';

@Component({
  selector: 'app-admin-libros',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './admin-libros.component.html',
  styleUrls: ['./admin-libros.component.css']
})
export class AdminLibrosComponent implements OnInit {
  libros: LibroResponse[] = [];
  loading = false;
  error: string | null = null;
  
  showModal = false;
  isEditMode = false;
  libroActual: LibroCreate = this.getEmptyLibro();

  constructor(
    private librosService: LibrosService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.cargarLibros();
  }

  cargarLibros(): void {
    this.loading = true;
    this.error = null;
    console.log('🔄 Cargando libros en admin...');
    
    this.librosService.getLibros().subscribe({
      next: (data) => {
        console.log('✅ Datos recibidos en admin:', data);
        
        // Asegurarse de que sea un array
        if (Array.isArray(data)) {
          this.libros = data;
        } else {
          console.error('⚠️ La respuesta no es un array:', data);
          this.libros = [];
        }
        
        this.loading = false;
        console.log('📚 Libros asignados:', this.libros.length);
        
        // Forzar detección de cambios
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error('❌ Error al cargar libros:', err);
        this.error = 'No se pudieron cargar los libros: ' + (err.message || 'Error desconocido');
        this.loading = false;
        this.cdr.detectChanges();
      },
      complete: () => {
        console.log('✔️ Carga completada');
      }
    });
  }

  abrirModalCrear(): void {
    this.isEditMode = false;
    this.libroActual = this.getEmptyLibro();
    this.showModal = true;
  }

  abrirModalEditar(libro: LibroResponse): void {
    this.isEditMode = true;
    this.libroActual = {
      Codigo_Libro: libro.Codigo_Libro,
      Titulo: libro.Titulo,
      Año: libro['Año'],
      Precio: libro.Precio,
      Id_Autor: libro.Id_Autor,
      Id_Editorial: libro.Id_Editorial
    };
    this.showModal = true;
  }

  cerrarModal(): void {
    this.showModal = false;
    this.libroActual = this.getEmptyLibro();
  }

  guardarLibro(): void {
    console.log('💾 Guardando libro:', this.libroActual);
    
    if (this.isEditMode) {
      const libro = this.libros.find(l => l.Codigo_Libro === this.libroActual.Codigo_Libro);
      if (libro) {
        this.librosService.updateLibro(libro.Id_Libro, this.libroActual).subscribe({
          next: () => {
            alert('Libro actualizado exitosamente');
            this.cargarLibros();
            this.cerrarModal();
          },
          error: (err) => {
            console.error('Error al actualizar:', err);
            alert('Error al actualizar el libro: ' + (err.error?.detail || err.message));
          }
        });
      }
    } else {
      this.librosService.createLibro(this.libroActual).subscribe({
        next: () => {
          alert('Libro creado exitosamente');
          this.cargarLibros();
          this.cerrarModal();
        },
        error: (err) => {
          console.error('Error al crear:', err);
          alert('Error al crear el libro: ' + (err.error?.detail || err.message));
        }
      });
    }
  }

  eliminarLibro(libro: LibroResponse): void {
    if (confirm(`¿Estás seguro de eliminar el libro "${libro.Titulo}"?`)) {
      this.librosService.deleteLibro(libro.Id_Libro).subscribe({
        next: () => {
          alert('Libro eliminado exitosamente');
          this.cargarLibros();
        },
        error: (err) => {
          console.error('Error al eliminar:', err);
          alert('Error al eliminar el libro: ' + (err.error?.detail || err.message));
        }
      });
    }
  }

  private getEmptyLibro(): LibroCreate {
    return {
      Codigo_Libro: '',
      Titulo: '',
      Año: null,
      Precio: null,
      Id_Autor: '',
      Id_Editorial: ''
    };
  }
}