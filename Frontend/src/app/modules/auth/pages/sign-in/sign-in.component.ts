import { NgClass, NgIf } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { ButtonComponent } from '../../../../shared/components/button/button.component';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css'],
  imports: [FormsModule, ReactiveFormsModule, RouterLink, AngularSvgIconModule, NgIf, ButtonComponent, NgClass],
})
export class SignInComponent implements OnInit {
  form!: FormGroup;
  submitted = false;
  passwordTextType!: boolean;

  constructor(private readonly _formBuilder: FormBuilder, private readonly _router: Router) {}

  onClick() {
    console.log('Button clicked');
  }

  ngOnInit(): void {
    this.form = this._formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
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
    const { email, password } = this.form.value;

    if (this.form.invalid) {
      return;
    }

    this._router.navigate(['/']);
  }
}

/*import { NgClass, NgIf } from '@angular/common';
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
  imports: [FormsModule, ReactiveFormsModule, RouterLink, AngularSvgIconModule, NgIf, ButtonComponent, NgClass],
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

if (this.form.invalid) {
  alert('Por favor completa todos los campos.');
  return;
}

const { username, password } = this.form.value;
this.loading = true;

this.authService.login(username, password).subscribe({
  next: (res) => {
    this.loading = false;
    console.log('✅ Login exitoso:', res);

    // Guarda el token
    localStorage.setItem('token', res.access_token);

    alert(`Bienvenido ${res.user.Nombre}!`);
    this.router.navigate(['/dashboard']);
  },
  error: (err) => {
    this.loading = false;
    console.error('❌ Error en login:', err);
    alert(err.error?.detail || 'Credenciales incorrectas o servidor no disponible.');
  },
});


}
}*/