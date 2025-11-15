import { NgClass, NgIf } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { ButtonComponent } from '../../../../shared/components/button/button.component';
import { AuthService } from '../sign-in/services/auth.service';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css'],
  imports: [
    FormsModule,
    ReactiveFormsModule,
    RouterLink,
    AngularSvgIconModule,
    NgIf,
    ButtonComponent,
    NgClass,
  ],
})
export class SignInComponent implements OnInit {
  form!: FormGroup;
  submitted = false;
  loading = false;
  passwordTextType = false;

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.form = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  get f() {
    return this.form.controls;
  }

  togglePasswordTextType() {
    this.passwordTextType = !this.passwordTextType;
  }

  onSubmit() {
    this.submitted = true;

    // Validar formulario antes de enviar
    if (this.form.invalid) {
      alert('Por favor completa todos los campos.');
      return;
    }

    const { username, password } = this.form.value;
    this.loading = true;

    // Llamada al servicio de autenticación
    this.authService.login(username, password).subscribe({
      next: (res) => {
        this.loading = false;
        console.log('Respuesta del backend:', res);

        // Verifica si el token llega correctamente
        if (res && res.access_token) {
          localStorage.setItem('token', res.access_token);
          console.log('Token guardado en localStorage:', res.access_token);

          // Mensaje de bienvenida
          alert(`Bienvenido ${res.user?.Nombre || username}!`);

          // Redirige al dashboard
          this.router.navigate(['/dashboard']);
        } else {
          console.warn('No se recibió un token en la respuesta del backend');
          alert('No se recibió token. Revisa el backend o la estructura de la respuesta.');
        }
      },
      error: (err) => {
        this.loading = false;
        console.error('Error en login:', err);

        // Mensaje de error amigable
        const mensaje =
          err.error?.detail ||
          'Credenciales incorrectas o servidor no disponible.';
        alert(mensaje);
      },
    });
  }
}
