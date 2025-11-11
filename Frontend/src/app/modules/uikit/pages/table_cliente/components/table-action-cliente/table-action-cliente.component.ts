import { Component } from '@angular/core';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { TableFilterClienteService } from '../../services/table.filter-cliente.service';

@Component({
  selector: 'app-table-action-cliente',
  imports: [AngularSvgIconModule],
  templateUrl: './table-action-cliente.component.html',
  styleUrl: './table-action-cliente.component.css',
})
export class TableActionClienteComponent {
  constructor(public filterClienteService: TableFilterClienteService) {}

  onSearchChange(value: Event) {
    const input = value.target as HTMLInputElement;
    this.filterClienteService.searchField.set(input.value);
  }

  onStatusChange(value: Event) {
    const selectElement = value.target as HTMLSelectElement;
    this.filterClienteService.statusField.set(selectElement.value);
  }

  onOrderChange(value: Event) {
    const selectElement = value.target as HTMLSelectElement;
    this.filterClienteService.orderField.set(selectElement.value);
  }
}
