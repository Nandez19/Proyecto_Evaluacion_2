import { HttpClient } from '@angular/common/http';
import { Component, OnInit, computed, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { toast } from 'ngx-sonner';
import { TableActionClienteComponent } from './components/table-action-cliente/table-action-cliente.component';
import { TableFooterComponent } from './components/table-footer-cliente/table-footer.component';
import { TableHeaderComponent } from './components/table-header-cliente/table-header-cliente.component';
import { TableRowComponent } from './components/table-row-cliente/table-row-cliente.component';
import { Cliente } from './model/cliente.model';
import { TableFilterClienteService } from './services/table.filter-cliente.service';

@Component({
  selector: 'app-table-cliente',
  standalone: true,
  imports: [
    AngularSvgIconModule,
    FormsModule,
    TableHeaderComponent,
    TableFooterComponent,
    TableRowComponent,
    TableActionClienteComponent,
  ],
  templateUrl: './table-cliente.component.html',
  styleUrls: ['./table-cliente.component.css'],
})
export class TableClienteComponent implements OnInit {
  clientes = signal<Cliente[]>([]);

  constructor(
    private http: HttpClient,
    private filterService: TableFilterClienteService
  ) {}

  ngOnInit(): void {
    this.loadClientes();
  }

  /** Cargar lista de clientes desde la API */
  private loadClientes(): void {
    this.http
      .get<Cliente[]>('http://127.0.0.1:8000/clientes/')
      .subscribe({
        next: (data) => this.clientes.set(data),
        error: (error) => {
          this.clientes.set([]); // carga vacía si hay error
          this.handleRequestError(error);
        },
      });
  }

  /** Seleccionar o deseleccionar todos los clientes */
  public toggleClientes(checked: boolean): void {
    this.clientes.update((clientes) =>
      clientes.map((cliente) => ({ ...cliente, selected: checked }))
    );
  }

  /** Mostrar error con notificación */
  private handleRequestError(error: any): void {
    toast.error('Error al obtener clientes.', {
      position: 'bottom-right',
      description:
        error?.message ||
        'Ocurrió un error al cargar los clientes. Por favor, inténtalo más tarde.',
      action: {
        label: 'Reintentar',
        onClick: () => this.loadClientes(),
      },
      actionButtonStyle: 'background-color:#DC2626; color:white;',
    });
  }

  /** Filtro y ordenamiento de clientes */
  filteredClientes = computed(() => {
    const search = this.filterService.searchField().toLowerCase();
    const order = this.filterService.orderField();

    return this.clientes()
      .filter(
        (cliente) =>
          cliente.Nombre.toLowerCase().includes(search) ||
          cliente.Correo.toLowerCase().includes(search) ||
          cliente.Cedula_Cliente.toLowerCase().includes(search) ||
          (cliente.Telefono?.includes(search) ?? false)
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