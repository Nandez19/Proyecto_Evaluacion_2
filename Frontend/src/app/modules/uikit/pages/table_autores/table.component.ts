import { HttpClient } from '@angular/common/http';
import { Component, OnInit, computed, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { toast } from 'ngx-sonner';
import { TableActionComponent } from './components/table-action/table-action.component';
import { TableFooterComponent } from './components/table-footer/table-footer.component';
import { TableHeaderComponent } from './components/table-header/table-header.component';
import { TableRowComponent } from './components/table-row/table-row.component';
import { User } from './model/user.model';
import { TableFilterService } from './services/table-filter.service';

@Component({
selector: 'app-table',
standalone: true,
imports: [
AngularSvgIconModule,
FormsModule,
TableHeaderComponent,
TableFooterComponent,
TableRowComponent,
TableActionComponent,
],
templateUrl: './table.component.html',
styleUrls: ['./table.component.css'],
})
export class TableComponent implements OnInit {
users = signal<User[]>([]);

constructor(
private http: HttpClient,
private filterService: TableFilterService
) {}

ngOnInit(): void {
this.loadUsers();
}

private loadUsers(): void {
this.http.get<User[]>('http://127.0.0.1:8000/autores/autores').subscribe({

next: (data) => this.users.set(data),
error: (error) => {
this.users.set([]); // carga vacía si hay error
this.handleRequestError(error);
},
});
}

public toggleUsers(checked: boolean): void {
this.users.update((users) =>
users.map((user) => ({ ...user, selected: checked }))
);
}

private handleRequestError(error: any): void {
toast.error('Error al obtener usuarios.', {
position: 'bottom-right',
description:
error?.message ||
'Ocurrió un error al cargar los usuarios. Por favor, inténtalo más tarde.',
action: {
label: 'Reintentar',
onClick: () => this.loadUsers(),
},
actionButtonStyle: 'background-color:#DC2626; color:white;',
});
}

filteredUsers = computed(() => {
const search = this.filterService.searchField().toLowerCase();
const status = this.filterService.statusField();
const order = this.filterService.orderField();

   /*return this.users()
  .filter(
    (user) =>
      user.Nombre.toLowerCase().includes(search) ||
      user.Username.toLowerCase().includes(search) ||
      user.Correo.toLowerCase().includes(search) ||
      (user.Telefono?.includes(search) ?? false)
  )
  .filter((user) => {
    if (!status) return true;
    switch (status) {
      case '1':
        return user.Activo === true;
      case '2':
        return user.Activo === false;
      default:
        return true;
    }
  })
  .sort((a, b) => {
    const defaultNewest = !order || order === '1';
    if (defaultNewest) {
      return (
        new Date(b.Fecha_creacion).getTime() -
        new Date(a.Fecha_creacion).getTime()
      );
    } else if (order === '2') {
      return (
        new Date(a.Fecha_creacion).getTime() -
        new Date(b.Fecha_creacion).getTime()
      );
    }
    return 0;
  });
});
}*/
