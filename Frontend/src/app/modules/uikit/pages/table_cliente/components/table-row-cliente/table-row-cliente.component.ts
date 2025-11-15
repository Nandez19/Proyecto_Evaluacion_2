import { Component, Input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { Cliente } from '../../model/cliente.model';

@Component({
  selector: '[app-table-row-cliente]',
  imports: [FormsModule, AngularSvgIconModule],
  templateUrl: './table-row-cliente.component.html',
  styleUrl: './table-row-cliente.component.css',
})
export class TableRowComponent {
  @Input() cliente: Cliente = <Cliente>{};

  constructor() {}
}
