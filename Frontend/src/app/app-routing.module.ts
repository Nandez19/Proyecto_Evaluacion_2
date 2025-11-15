import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./modules/layout/layout.module').then((m) => m.LayoutModule),
  },
  {
    path: 'auth',
    loadChildren: () => import('./modules/auth/auth.module').then((m) => m.AuthModule),
  },
  {
    path: 'errors',
    loadChildren: () => import('./modules/error/error.module').then((m) => m.ErrorModule),
  },
  { 
    path: 'libros', 
    loadChildren: () => import('./modules/libros/libros.module').then(m => m.LibrosModule) 
  },
  // ⭐ NUEVA RUTA DE AUTORES
  { 
    path: 'autores', 
    loadChildren: () => import('./modules/admin-autores/admin-autores.module').then(m => m.AdminAutoresModule) 
  },
  { path: '**', redirectTo: 'errors/404' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}