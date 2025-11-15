import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { BibliotecariosService, BibliotecarioResponse, BibliotecarioCreate } from './bibliotecarios.service';

@Component({
  selector: 'app-admin-bibliotecarios',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './admin-bibliotecarios.component.html',
  styleUrls: ['./admin-bibliotecarios.component.css']
})
export class AdminBibliotecariosComponent implements OnInit {
  bibliotecarios: BibliotecarioResponse[] = [];
  loading = false;
  error: string | null = null;
  
  showModal = false;
  isEditMode = false;
  bibliotecarioActual: BibliotecarioCreate = this.getEmptyBibliotecario();

  constructor(
    private bibliotecariosService: BibliotecariosService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.cargarBibliotecarios();
  }

  cargarBibliotecarios(): void {
    this.loading = true;
    this.error = null;
    
    this.bibliotecariosService.getBibliotecarios().subscribe({
      next: (data) => {
        if (Array.isArray(data)) {
          this.bibliotecarios = data;
        } else {
          this.bibliotecarios = [];
        }
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: (err) => {
        this.error = 'No se pudieron cargar los bibliotecarios';
        this.loading = false;
        this.cdr.detectChanges();
      }
    });
  }

  abrirModalCrear(): void {
    this.isEditMode = false;
    this.bibliotecarioActual = this.getEmptyBibliotecario();
    this.showModal = true;
  }

  abrirModalEditar(bibliotecario: BibliotecarioResponse): void {
    this.isEditMode = true;
    this.bibliotecarioActual = {
      Cedula_Bibliotecario: bibliotecario.Cedula_Bibliotecario,
      Nombre: bibliotecario.Nombre,
      Telefono: bibliotecario.Telefono,
      Edad: String(bibliotecario.Edad)
    };
    this.showModal = true;
  }
  
  cerrarModal(): void {
    this.showModal = false;
    this.bibliotecarioActual = this.getEmptyBibliotecario();
  }

  guardarBibliotecario(): void {
  console.log('💾 Guardando bibliotecario:', this.bibliotecarioActual);
  
  // ✅ Asegurar que Edad sea string y se recorten espacios
  const bibliotecarioParaGuardar: BibliotecarioCreate = {
    Cedula_Bibliotecario: this.bibliotecarioActual.Cedula_Bibliotecario.trim(),
    Nombre: this.bibliotecarioActual.Nombre.trim(),
    Telefono: this.bibliotecarioActual.Telefono.trim(),
    Edad: String(this.bibliotecarioActual.Edad || '')
  };
  
  console.log('📤 Bibliotecario transformado:', bibliotecarioParaGuardar);
  
  if (this.isEditMode) {
    const bibliotecario = this.bibliotecarios.find(a => a.Cedula_Bibliotecario === this.bibliotecarioActual.Cedula_Bibliotecario);
    if (bibliotecario) {
      this.bibliotecariosService.updateBibliotecario(bibliotecario.Id_Bibliotecario, bibliotecarioParaGuardar).subscribe({
        next: () => {
          alert('Bibliotecario actualizado exitosamente');
          this.cargarBibliotecarios();
          this.cerrarModal();
        },
        error: (err) => {
          console.error('Error al actualizar:', err);
          alert('Error al actualizar el bibliotecario: ' + (err.error?.detail || err.message));
        }
      });
    }
  } else {
    this.bibliotecariosService.createBibliotecario(bibliotecarioParaGuardar).subscribe({
      next: () => {
        alert('Bibliotecario creado exitosamente');
        this.cargarBibliotecarios();
        this.cerrarModal();
      },
      error: (err) => {
        console.error('Error al crear:', err);
        alert('Error al crear el bibliotecario: ' + (err.error?.detail || err.message));
      }
    });
  }
}
  eliminarBibliotecario(bibliotecario: BibliotecarioResponse): void {
    // Obtener el ID dinámicamente del objeto
    const id = bibliotecario['Id_Bibliotecario'];
    
    if (!id) {
      alert('Error: No se puede identificar el bibliotecario');
      return;
    }
    
    if (confirm(`¿Estás seguro de eliminar al bibliotecario "${bibliotecario.Nombre}"?`)) {
      this.bibliotecariosService.deleteBibliotecario(id).subscribe({
        next: () => {
          alert('Bibliotecario eliminado exitosamente');
          this.cargarBibliotecarios();
        },
        error: (err) => {
          alert('Error al eliminar el bibliotecario');
        }
      });
    }
  }

  private getEmptyBibliotecario(): BibliotecarioCreate {
    return {
      Cedula_Bibliotecario: '',
      Nombre: '',
      Telefono: '',
      Edad: ''
    };
  }
}