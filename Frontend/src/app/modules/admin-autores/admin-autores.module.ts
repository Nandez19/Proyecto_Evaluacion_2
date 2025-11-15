import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AdminAutoresRoutingModule } from './admin-autores-routing.module';
import { AdminAutoresComponent } from '../admin-autores/admin-autores.component';

@NgModule({
  imports: [
    CommonModule,
    AdminAutoresRoutingModule,
    AdminAutoresComponent
  ]
})
export class AdminAutoresModule { }