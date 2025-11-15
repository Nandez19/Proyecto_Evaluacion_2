import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AdminBibliotecariosRoutingModule } from './admin-bibliotecarios-routing.module';
import { AdminBibliotecariosComponent } from './admin-bibliotecarios.component';

@NgModule({
  imports: [
    CommonModule,
    AdminBibliotecariosRoutingModule,
    AdminBibliotecariosComponent
  ]
})
export class AdminBibliotecariosModule { }