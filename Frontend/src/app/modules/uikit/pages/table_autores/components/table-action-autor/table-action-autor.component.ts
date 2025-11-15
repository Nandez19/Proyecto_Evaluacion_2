import { Component } from '@angular/core';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { TableFilterAutorService } from '../../services/table.filter-autor.service';

@Component({
  selector: 'app-table-action-autor',
  imports: [AngularSvgIconModule],
  templateUrl: './table-action-autor.component.html',
  styleUrl: './table-action-autor.component.css',
})
export class TableActionAutorComponent {
  constructor(public filterAutorService: TableFilterAutorService) {}

  onSearchChange(value: Event) {
    const input = value.target as HTMLInputElement;
    this.filterAutorService.searchField.set(input.value);
  }

  onStatusChange(value: Event) {
    const selectElement = value.target as HTMLSelectElement;
    this.filterAutorService.statusField.set(selectElement.value);
  }

  onOrderChange(value: Event) {
    const selectElement = value.target as HTMLSelectElement;
    this.filterAutorService.orderField.set(selectElement.value);
  }
}
