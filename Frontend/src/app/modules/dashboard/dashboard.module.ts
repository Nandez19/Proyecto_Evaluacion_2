import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashboardRoutingModule } from './dashboard-routing.module';
import { DashboardComponent } from './dashboard.component';
import { LibrosComponent } from '../libros/libros.component';
import { AdminLibrosComponent } from '../libros/pages/admin-libros/admin-libros.component'; // <- Importar

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    DashboardRoutingModule,
    DashboardComponent,
    LibrosComponent,
    AdminLibrosComponent, // <- Agregar
  ]
})
export class DashboardModule { }