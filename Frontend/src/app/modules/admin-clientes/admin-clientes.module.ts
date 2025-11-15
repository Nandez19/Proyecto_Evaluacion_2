import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AdminClientesRoutingModule } from './admin-clientes-routing.module';
import { AdminClientesComponent } from '../admin-clientes/admin-clientes.component';

@NgModule({
  imports: [
    CommonModule,
    AdminClientesRoutingModule,
    AdminClientesComponent // Importación del componente standalone
  ]
})
export class AdminClientesModule { }