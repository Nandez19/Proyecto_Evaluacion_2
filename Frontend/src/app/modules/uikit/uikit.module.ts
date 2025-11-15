import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UikitRoutingModule } from './uikit-routing.module';

// 👇 importa los componentes
import { UikitComponent } from './uikit.component';
import { TableComponent } from './pages/table/table.component';
import { TableClienteComponent } from './pages/table_cliente/table-cliente.component';

@NgModule({
  imports: [
    CommonModule,
    UikitRoutingModule,
    UikitComponent,
    TableComponent,
    TableClienteComponent
  ],
})
export class UikitModule {}
