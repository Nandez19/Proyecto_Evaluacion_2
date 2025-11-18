import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { UsuariosService, UserResponse, UserCreate } from './usuarios.service';

@Component({
  selector: 'app-usuarios',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './usuarios.component.html',
  styleUrls: ['./usuarios.component.css'],
})
export class UsuariosComponent implements OnInit {

  usuarios: UserResponse[] = [];

  loading = false;
  error: string | null = null;

  
  showModal = false;

  usuarioActual = this.getEmptyUsuario();

  constructor(
    private usuariosService: UsuariosService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.cargarUsuarios();
  }

 
  cargarUsuarios(): void {
    this.loading = true;
    this.error = null;

    this.usuariosService.getUsuarios().subscribe({
      next: (data) => {
        this.usuarios = data;
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: () => {
        this.loading = false;
        this.error = "Error al cargar usuarios";
      },
    });
  }

 
  abrirModalCrear() {
    this.usuarioActual = this.getEmptyUsuario();
    this.showModal = true;
  }

  cerrarModal() {
    this.showModal = false;
    this.usuarioActual = this.getEmptyUsuario();
  }

 
  guardarUsuario(): void {
    const data: UserCreate = {
      Username: this.usuarioActual.Username,
      Nombre: this.usuarioActual.Nombre,
      Correo: this.usuarioActual.Correo,
      Telefono: this.usuarioActual.Telefono,
      Rol: this.usuarioActual.Rol,
      password: this.usuarioActual.password
    };

    this.usuariosService.createUsuario(data).subscribe({
      next: (nuevo) => {
        alert("Usuario creado correctamente");
        this.usuarios.push(nuevo);
        this.cerrarModal();
      },
      error: () => {
        alert("Error al crear usuario");
      },
    });
  }


  private getEmptyUsuario() {
    return {
      Username: "",
      Nombre: "",
      Correo: "",
      Telefono: "",
      Rol: "Usuario",
      password: "",
    };
  }
}
