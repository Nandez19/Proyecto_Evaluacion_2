import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LibrosService, LibroResponse } from './libros.service';

@Component({
  selector: 'app-libros',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './libros.component.html',
  styleUrls: ['./libros.component.css']
})
export class LibrosComponent implements OnInit {
  libros: LibroResponse[] = [];
  loading = true; // Cambiar a true inicialmente
  error: string | null = null;

  constructor(
    private librosService: LibrosService,
    private cdr: ChangeDetectorRef // Añadir esto
  ) {}

  ngOnInit(): void {
    this.cargarLibros();
  }

  cargarLibros(): void {
    this.loading = true;
    this.error = null;
    console.log('🔄 Iniciando carga...');
    
    this.librosService.getLibros().subscribe({
      next: (data) => {
        console.log('✅ Datos recibidos:', data);
        
        this.libros = Array.isArray(data) ? data : [];
        this.loading = false;
        
        console.log('📚 Libros asignados:', this.libros);
        console.log('🔢 Cantidad:', this.libros.length);
        console.log('⚡ Loading:', this.loading);
        
        // Forzar detección de cambios
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error('❌ Error:', err);
        this.error = 'No se pudieron cargar los libros.';
        this.loading = false;
        this.libros = [];
        this.cdr.detectChanges();
      },
      complete: () => {
        console.log('✔️ Observable completado');
      }
    });
  }
}