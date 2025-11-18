import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UsuariosRoutingModule } from './usuarios-routing.module';
import { UsuariosComponent } from '../Usuarios/usuarios.component';

@NgModule({
  imports: [
    CommonModule,
    UsuariosRoutingModule,
    UsuariosComponent
  ]
})
export class UsuariosModule { }
