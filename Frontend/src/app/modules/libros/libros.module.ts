import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

import { LibrosRoutingModule } from './libros-routing.module';
import { LibrosComponent } from './libros.component';


@NgModule({
  declarations: [
    
  ],
  imports: [
    CommonModule,
    LibrosRoutingModule,
    HttpClientModule,
    LibrosComponent
  ]
})
export class LibrosModule { }
