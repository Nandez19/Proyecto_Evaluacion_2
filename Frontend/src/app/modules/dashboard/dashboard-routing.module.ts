import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard.component';
import { LibrosComponent } from '../libros/libros.component';
import { AdminLibrosComponent } from '../libros/pages/admin-libros/admin-libros.component'; // <- Importar
import { AdminAutoresComponent } from '../admin-autores/admin-autores.component';
import { PrestamosComponent } from '../Prestamos/prestamos.component';
import { UsuariosComponent } from '../Usuarios/usuarios.component';

const routes: Routes = [
  {
    path: '',
    component: DashboardComponent,
    children: [
      { path: '', redirectTo: 'libros', pathMatch: 'full' },
      { path: 'libros', component: LibrosComponent },
      { path: 'admin-libros', component: AdminLibrosComponent }, // <- Agregar esta línea
      {path: 'admin-autores', component: AdminAutoresComponent },
      {path: 'Prestamos', component: PrestamosComponent },
      {path: 'Usuarios', component:UsuariosComponent},
      
      { path: '**', redirectTo: 'errors/404' },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DashboardRoutingModule {}