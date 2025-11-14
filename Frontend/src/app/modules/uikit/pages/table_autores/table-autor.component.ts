import { HttpClient } from '@angular/common/http';
import { Component, OnInit, computed, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { toast } from 'ngx-sonner';
import { TableActionAutorComponent } from './components/table-action-autor/table-action-autor.component';
import { TableFooterComponent } from './components/table-footer-autor/table-footer.component';
import { TableHeaderComponent } from './components/table-header-autor/table-header-autor.component';
import { TableRowComponent } from './components/table-row-autor/table-row-autor.component';
import { Autor } from './model/autor.model';
import { TableFilterAutorService } from './services/table.filter-autor.service';

@Component({
  selector: 'app-table-autor',
  standalone: true,
  imports: [
    AngularSvgIconModule,
    FormsModule,
    TableHeaderComponent,
    TableFooterComponent,
    TableRowComponent,
    TableActionAutorComponent,
  ],
  templateUrl: './table-autor.component.html',
  styleUrls: ['./table-autor.component.css'],
})
export class TableAutorComponent implements OnInit {
  autores = signal<Autor[]>([]);

  constructor(
    private http: HttpClient,
    private filterService: TableFilterAutorService
  ) {}

  ngOnInit(): void {
    this.loadAutores();
  }

  /** Cargar lista de clientes desde la API */
private loadAutores(): void {
  const token = localStorage.getItem('token');
  console.log('🔑 Token encontrado:', token ? 'SÍ ✅' : 'NO ❌');

  const headers = {
    'Authorization': `Bearer ${token}`
  };

  console.log('📤 Haciendo petición a:', 'http://127.0.0.1:8000/autores/autores');
  console.log('📤 Headers:', headers);

  this.http
    .get<Autor[]>('http://127.0.0.1:8000/autores/autores', { headers })
    .subscribe({
      next: (data) => {
        console.log("✅ ÉXITO - Datos recibidos:", data);
        console.log("📊 Cantidad de autores:", data.length);
        this.autores.set(data);
      },
      error: (error) => {
        console.log("❌ ERROR COMPLETO:", error);
        console.log("❌ Status:", error.status);
        console.log("❌ StatusText:", error.statusText);
        console.log("❌ Error message:", error.error);
        console.log("❌ URL que falló:", error.url);
        
        // Si es 401, el token expiró o es inválido
        if (error.status === 401) {
          console.log("🚨 TOKEN INVÁLIDO O EXPIRADO");
          toast.error('Sesión expirada', {
            position: 'bottom-right',
            description: 'Tu sesión ha expirado. Por favor, inicia sesión nuevamente.',
          });
        }
        
        this.autores.set([]);
        this.handleRequestError(error);
      },
    });
}

  /** Seleccionar o deseleccionar todos los clientes */
  public toggleAutores(checked: boolean): void {
    this.autores.update((autores) =>
      autores.map((autores) => ({ ...autores, selected: checked }))
    );
  }

  /** Mostrar error con notificación */
  private handleRequestError(error: any): void {
    toast.error('Error al obtener autores.', {
      position: 'bottom-right',
      description:
        error?.message ||
        'Ocurrió un error al cargar los autores. Por favor, inténtalo más tarde.',
      action: {
        label: 'Reintentar',
        onClick: () => this.loadAutores(),
      },
      actionButtonStyle: 'background-color:#DC2626; color:white;',
    });
  }

  /** Filtro y ordenamiento de clientes */
  filteredAutores = computed(() => {
    const search = this.filterService.searchField().toLowerCase();
    const order = this.filterService.orderField();

    return this.autores()
      .filter(
        (autor) =>
          autor.Nombre.toLowerCase().includes(search) ||
          autor.Cedula_Autor.toLowerCase().includes(search) ||
          (autor.Telefono?.includes(search) ?? false)
      )
      .sort((a, b) => {
        const defaultNewest = !order || order === '1';
        if (defaultNewest) {
          // No hay campo de fecha en Cliente, pero se podría usar Fecha_creacion si lo agregas luego
          return 0;
        } else if (order === '2') {
          return 0;
        }
        return 0;
      });
  });
}