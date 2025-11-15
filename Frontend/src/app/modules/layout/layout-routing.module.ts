import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LayoutComponent } from './layout.component';

const routes: Routes = [
  {
    path: 'dashboard',
    component: LayoutComponent,
    children: [
      {
        path: '',
        loadChildren: () => import('../dashboard/dashboard.module').then((m) => m.DashboardModule),
      },
      {
        path: 'admin-autores',
        loadChildren: () => import('../admin-autores/admin-autores.module')
          .then(m => m.AdminAutoresModule)
      },
      {
        path: 'admin-bibliotecarios',
        loadChildren: () => import('../admin-bibliotecarios/admin-bibliotecarios.module')
          .then(m => m.AdminBibliotecariosModule)
      },
      {
        path: 'admin-clientes',
        loadChildren: () => import('../admin-clientes/admin-clientes.module')
          .then(m => m.AdminClientesModule)
      },
      
      
    ]
  },
  {
    path: 'components',
    component: LayoutComponent,
    loadChildren: () => import('../uikit/uikit.module').then((m) => m.UikitModule),
  },
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  { path: '**', redirectTo: 'error/404' },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class LayoutRoutingModule {}
