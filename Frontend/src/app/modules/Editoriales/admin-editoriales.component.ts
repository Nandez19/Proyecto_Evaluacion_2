import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { EditorialesService, EditorialResponse, EditorialCreate } from './editoriales.service';

@Component({
  selector: 'app-admin-editoriales',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './admin-editoriales.component.html',
  styleUrls: ['./admin-editoriales.component.css']
})
export class AdminEditorialesComponent implements OnInit {
  editoriales: EditorialResponse[] = [];
  loading = false;
  error: string | null = null;
  
  showModal = false;
  isEditMode = false;
  editorialActual: EditorialCreate = this.getEmptyEditorial();
  editorialIdActual: string | null = null; // ✅ AGREGADO: Para guardar el ID

  constructor(
    private editorialesService: EditorialesService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.cargarEditoriales();
  }

  cargarEditoriales(): void {
    this.loading = true;
    this.error = null;
    
    this.editorialesService.getEditoriales().subscribe({
      next: (data) => {
        if (Array.isArray(data)) {
          this.editoriales = data;
        } else {
          this.editoriales = [];
        }
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: (err) => {
        this.error = 'No se pudieron cargar las editoriales';
        this.loading = false;
        this.cdr.detectChanges();
      }
    });
  }

  abrirModalCrear(): void {
    this.isEditMode = false;
    this.editorialActual = this.getEmptyEditorial();
    this.editorialIdActual = null; // ✅ Limpiar el ID
    this.showModal = true;
  }

  abrirModalEditar(editorial: EditorialResponse): void {
    this.isEditMode = true;
    this.editorialIdActual = editorial.Id_Editorial; // ✅ GUARDAR EL ID
    this.editorialActual = {
      Nombre: editorial.Nombre,
      Pais: editorial.Pais,
      Contacto: editorial.Contacto
    };
    this.showModal = true;
  }

  cerrarModal(): void {
    this.showModal = false;
    this.editorialActual = this.getEmptyEditorial();
    this.editorialIdActual = null; // ✅ Limpiar el ID
  }

  guardarEditorial(): void {
    console.log('💾 Guardando editorial:', this.editorialActual);
    
    // Asegurar que los datos estén limpios
    const editorialParaGuardar: EditorialCreate = {
      Nombre: this.editorialActual.Nombre.trim(),
      Pais: this.editorialActual.Pais.trim(),
      Contacto: this.editorialActual.Contacto.trim()
    };
    
    console.log('📤 Editorial transformada:', editorialParaGuardar);
    
    if (this.isEditMode) {
      // ✅ CORREGIDO: Usar el ID guardado directamente
      if (this.editorialIdActual) {
        console.log('📝 Actualizando editorial con ID:', this.editorialIdActual);
        this.editorialesService.updateEditorial(this.editorialIdActual, editorialParaGuardar).subscribe({
          next: () => {
            alert('Editorial actualizada exitosamente');
            this.cargarEditoriales();
            this.cerrarModal();
          },
          error: (err) => {
            console.error('Error al actualizar:', err);
            alert('Error al actualizar la editorial: ' + (err.error?.detail || err.message));
          }
        });
      } else {
        alert('Error: No se puede identificar la editorial a editar');
      }
    } else {
      this.editorialesService.createEditorial(editorialParaGuardar).subscribe({
        next: () => {
          alert('Editorial creada exitosamente');
          this.cargarEditoriales();
          this.cerrarModal();
        },
        error: (err) => {
          console.error('Error al crear:', err);
          alert('Error al crear la editorial: ' + (err.error?.detail || err.message));
        }
      });
    }
  }

  eliminarEditorial(editorial: EditorialResponse): void {
    const id = editorial.Id_Editorial;
    
    if (!id) {
      alert('Error: No se puede identificar la editorial');
      return;
    }
    
    if (confirm(`¿Estás seguro de eliminar la editorial "${editorial.Nombre}"?`)) {
      this.editorialesService.deleteEditorial(id).subscribe({
        next: () => {
          alert('Editorial eliminada exitosamente');
          this.cargarEditoriales();
        },
        error: (err) => {
          alert('Error al eliminar la editorial');
        }
      });
    }
  }

  private getEmptyEditorial(): EditorialCreate {
    return {
      Nombre: '',
      Pais: '',
      Contacto: ''
    };
  }
}