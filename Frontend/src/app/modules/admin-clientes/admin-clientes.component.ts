import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ClientesService, ClienteResponse, ClienteCreate } from 'src/app/modules/admin-clientes/clientes.service';

@Component({
  selector: 'app-admin-clientes',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './admin-clientes.component.html',
  styleUrls: ['./admin-clientes.component.css']
})
export class AdminClientesComponent implements OnInit {
  clientes: ClienteResponse[] = [];
  loading = false;
  error: string | null = null;
  
  showModal = false;
  isEditMode = false;
  clienteActual: ClienteCreate = this.getEmptyCliente();

  constructor(
    private clientesService: ClientesService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.cargarClientes();
  }

  cargarClientes(): void {
    this.loading = true;
    this.error = null;
    
    this.clientesService.getClientes().subscribe({
      next: (data) => {
        if (Array.isArray(data)) {
          this.clientes = data;
        } else {
          this.clientes = [];
        }
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: (err) => {
        this.error = 'No se pudieron cargar los clientes';
        this.loading = false;
        this.cdr.detectChanges();
      }
    });
  }

  abrirModalCrear(): void {
    this.isEditMode = false;
    this.clienteActual = this.getEmptyCliente();
    this.showModal = true;
  }

  abrirModalEditar(cliente: ClienteResponse): void {
    this.isEditMode = true;
    this.clienteActual = {
      Cedula_Cliente: cliente.Cedula_Cliente,
      Nombre: cliente.Nombre,
      Telefono: cliente.Telefono,
      Correo: cliente.Correo
    };
    this.showModal = true;
  }
  
  cerrarModal(): void {
    this.showModal = false;
    this.clienteActual = this.getEmptyCliente();
  }

  guardarCliente(): void {
    const clienteParaGuardar: ClienteCreate = {
      Cedula_Cliente: this.clienteActual.Cedula_Cliente.trim(),
      Nombre: this.clienteActual.Nombre.trim(),
      Telefono: this.clienteActual.Telefono.trim(),
      Correo: this.clienteActual.Correo.trim()
    };
    
    if (this.isEditMode) {
      const cliente = this.clientes.find(a => a.Cedula_Cliente === this.clienteActual.Cedula_Cliente);
      if (cliente) {
        this.clientesService.updateCliente(cliente.Id_Cliente, clienteParaGuardar).subscribe({
          next: () => {
            alert('Cliente actualizado exitosamente');
            this.cargarClientes();
            this.cerrarModal();
          },
          error: (err) => {
            console.error('Error al actualizar:', err);
            alert('Error al actualizar el cliente: ' + (err.error?.detail || err.message));
          }
        });
      }
    } else {
      this.clientesService.createCliente(clienteParaGuardar).subscribe({
        next: () => {
          alert('Cliente creado exitosamente');
          this.cargarClientes();
          this.cerrarModal();
        },
        error: (err) => {
          console.error('Error al crear:', err);
          alert('Error al crear el cliente: ' + (err.error?.detail || err.message));
        }
      });
    }
  }
  
  eliminarCliente(cliente: ClienteResponse): void {
    const id = cliente['Id_Cliente'];
    
    if (!id) {
      alert('Error: No se puede identificar el cliente');
      return;
    }
    
    if (confirm(`¿Estás seguro de eliminar al cliente "${cliente.Nombre}"?`)) {
      this.clientesService.deleteCliente(id).subscribe({
        next: () => {
          alert('Cliente eliminado exitosamente');
          this.cargarClientes();
        },
        error: (err) => {
          alert('Error al eliminar el cliente');
        }
      });
    }
  }

  private getEmptyCliente(): ClienteCreate {
    return {
      Cedula_Cliente: '',
      Nombre: '',
      Telefono: '',
      Correo: ''
    };
  }
}