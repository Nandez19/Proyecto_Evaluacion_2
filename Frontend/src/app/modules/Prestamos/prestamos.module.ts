import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PrestamosRoutingModule } from './prestamos-routing.module';
import { PrestamosComponent } from './prestamos.component';

@NgModule({
  imports: [
    CommonModule,
    PrestamosRoutingModule,
    PrestamosComponent   
  ]
})
export class PrestamosModule {}
