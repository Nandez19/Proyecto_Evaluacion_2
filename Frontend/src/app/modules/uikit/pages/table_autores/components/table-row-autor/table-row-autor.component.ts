import { Component, Input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { Autor } from '../../model/autor.model';

@Component({
  selector: '[app-table-row-autor]',
  imports: [FormsModule, AngularSvgIconModule],
  templateUrl: './table-row-autor.component.html',
  styleUrl: './table-row-autor.component.css',
})
export class TableRowComponent {
  @Input() autor: Autor = <Autor>{};

  constructor() {}
}
