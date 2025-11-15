import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminBibliotecariosComponent } from './admin-bibliotecarios.component';

const routes: Routes = [
  {
    path: '',
    component: AdminBibliotecariosComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminBibliotecariosRoutingModule { }