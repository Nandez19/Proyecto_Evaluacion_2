import { Component, EventEmitter, Output } from '@angular/core';
import { AngularSvgIconModule } from 'angular-svg-icon';

@Component({
  selector: '[app-table-header-autor]',
  imports: [AngularSvgIconModule],
  templateUrl: './table-header-autor.component.html',
  styleUrl: './table-header-autor.component.css',
})
export class TableHeaderComponent {
  @Output() onCheck = new EventEmitter<boolean>();

  public toggle(event: Event) {
    const value = (event.target as HTMLInputElement).checked;
    this.onCheck.emit(value);
  }
}
