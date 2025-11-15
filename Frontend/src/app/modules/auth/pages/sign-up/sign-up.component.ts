import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { ButtonComponent } from 'src/app/shared/components/button/button.component';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css'],
  imports: [FormsModule, AngularSvgIconModule, ButtonComponent],
})
export class SignUpComponent implements OnInit {
  username: string = '';
  correo: string = '';
  telefono: string = '';
  nombre: string = '';
  password: string = '';
  confirmPassword: string = '';
  acceptTerm: boolean = false;

  passwordVisible: boolean = false;

  constructor(private http: HttpClient, private router: Router) {}

  ngOnInit(): void {}

  togglePasswordVisibility() {
    this.passwordVisible = !this.passwordVisible;
  }

  onSubmit() {
    // Validaciones básicas
    if (!this.username || !this.correo || !this.telefono || !this.nombre || !this.password || !this.confirmPassword) {
      alert('Todos los campos son obligatorios');
      return;
    }
    

    if (this.password.length < 8) {
      alert('La contraseña debe tener al menos 8 caracteres');
      return;
    }

    if (this.password !== this.confirmPassword) {
      alert('Las contraseñas no coinciden');
      return;
    }

    if (!this.acceptTerm) {
      alert('Debes aceptar los términos');
      return;
    }

    // Preparar payload según tu backend (UserCreate)
    const payload = {
      Username: this.username,
      Correo: this.correo,
      Telefono: this.telefono,
      Nombre: this.nombre,
      password: this.password,
      Rol: 'Usuario'
    };

    // POST al backend
    this.http.post('http://127.0.0.1:8000/auth/register', payload)
      .subscribe({
        next: (res) => {
          console.log('Usuario registrado:', res);
          this.router.navigate(['/dashboard']);
        },
        error: (err) => {
          console.error('Error al registrar usuario:', err);

          // Mostrar mensaje específico si el backend devuelve detalles
          if (err.error && err.error.detail) {
            alert(`Error al registrar usuario: ${err.error.detail}`);
          } else {
            alert('Error al registrar usuario');
          }
        }
      });
  }
}
