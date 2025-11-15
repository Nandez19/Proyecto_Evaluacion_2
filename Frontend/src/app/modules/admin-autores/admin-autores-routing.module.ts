import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminAutoresComponent } from '../admin-autores/admin-autores.component';

const routes: Routes = [
  {
    path: '',
    component: AdminAutoresComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminAutoresRoutingModule { }