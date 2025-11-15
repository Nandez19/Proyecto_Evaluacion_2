import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { PrestamosService, PrestamoResponse, PrestamoCreate } from './prestamos.service';

@Component({
  selector: 'app-prestamos',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './prestamos.component.html',
  styleUrls: ['./prestamos.component.css']
})
export class PrestamosComponent implements OnInit {

  prestamos: PrestamoResponse[] = [];
  loading = false;
  error: string | null = null;

  showModal = false;
  isEditMode = false;
  prestamoActual: PrestamoCreate = this.getEmptyPrestamo();
  idEditando: string | null = null;

  constructor(
    private prestamosService: PrestamosService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.cargarPrestamos();
  }

  cargarPrestamos(): void {
    this.loading = true;
    this.error = null;

    console.log('🔄 Cargando préstamos...');

    this.prestamosService.getPrestamos().subscribe({
      next: (data) => {
        console.log('✅ Datos recibidos:', data);

        if (Array.isArray(data)) {
          this.prestamos = data;
        } else {
          console.error('⚠ La respuesta no es un array:', data);
          this.prestamos = [];
        }

        this.loading = false;
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error('❌ Error al cargar préstamos:', err);
        this.error = 'No se pudieron cargar los préstamos: ' + (err.message || 'Error desconocido');
        this.loading = false;
        this.cdr.detectChanges();
      },
      complete: () => console.log('✔ Carga completada')
    });
  }

  abrirModalCrear(): void {
    this.isEditMode = false;
    this.idEditando = null;
    this.prestamoActual = this.getEmptyPrestamo();
    this.showModal = true;
  }

  abrirModalEditar(prestamo: PrestamoResponse): void {
    this.isEditMode = true;
    this.idEditando = prestamo.Id_Prestamo;

    this.prestamoActual = {
      Fecha_Prestamo: prestamo.Fecha_Prestamo,
      Fecha_Devolucion: prestamo.Fecha_Devolucion,
      Estado: prestamo.Estado,
      Id_Bibliotecario: prestamo.Id_Bibliotecario,
      Id_Cliente: prestamo.Id_Cliente,
      Id_Libro: prestamo.Id_Libro
    };

    this.showModal = true;
  }

  cerrarModal(): void {
    this.showModal = false;
    this.prestamoActual = this.getEmptyPrestamo();
    this.idEditando = null;
  }

  guardarPrestamo(): void {
    const prestamoParaGuardar: PrestamoCreate = {
      Fecha_Prestamo: new Date(this.prestamoActual.Fecha_Prestamo),
      Fecha_Devolucion: this.prestamoActual.Fecha_Devolucion
        ? new Date(this.prestamoActual.Fecha_Devolucion)
        : null,
      Estado: this.prestamoActual.Estado.trim(),
      Id_Bibliotecario: this.prestamoActual.Id_Bibliotecario,
      Id_Cliente: this.prestamoActual.Id_Cliente,
      Id_Libro: this.prestamoActual.Id_Libro,
    };

    if (this.isEditMode && this.idEditando) {
      this.prestamosService.updatePrestamo(this.idEditando, prestamoParaGuardar).subscribe({
        next: () => {
          alert('Préstamo actualizado exitosamente');
          this.cargarPrestamos();
          this.cerrarModal();
        },
        error: (err) => {
          alert('Error al actualizar: ' + (err.error?.detail || err.message));
        }
      });
    } else {
      this.prestamosService.createPrestamo(prestamoParaGuardar).subscribe({
        next: () => {
          alert('Préstamo creado exitosamente');
          this.cargarPrestamos();
          this.cerrarModal();
        },
        error: (err) => {
          alert('Error al crear: ' + (err.error?.detail || err.message));
        }
      });
    }
  }

  eliminarPrestamo(prestamo: PrestamoResponse): void {
    const id = prestamo.Id_Prestamo;

    if (!id) {
      alert('Error: ID no encontrado');
      return;
    }

    if (confirm('¿Seguro deseas eliminar este préstamo?')) {
      this.prestamosService.deletePrestamo(id).subscribe({
        next: () => {
          alert('Préstamo eliminado');
          this.cargarPrestamos();
        },
        error: () => {
          alert('Error al eliminar préstamo');
        }
      });
    }
  }

  private getEmptyPrestamo(): PrestamoCreate {
    return {
      Fecha_Prestamo: new Date().toISOString(),
      Fecha_Devolucion: null,
      Estado: '',
      Id_Bibliotecario: '',
      Id_Cliente: '',
      Id_Libro: ''
    };
  }
}
