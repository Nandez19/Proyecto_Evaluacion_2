import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { ButtonComponent } from 'src/app/shared/components/button/button.component';

@Component({
  selector: 'app-new-password',
  standalone: true,
  templateUrl: './new-password.component.html',
  styleUrls: ['./new-password.component.css'],
  imports: [FormsModule, CommonModule, AngularSvgIconModule, ButtonComponent],
})
export class NewPasswordComponent implements OnInit {
  password: string = '';
  confirmPassword: string = '';
  token: string = '';

  constructor(
    private route: ActivatedRoute,
    private http: HttpClient,
    private router: Router
  ) {}

  ngOnInit(): void {
    // Obtener token desde URL
    this.route.queryParams.subscribe((params) => {
      this.token = params['token'];
    });
  }

  onSubmit() {
    if (this.password !== this.confirmPassword) {
      alert('Las contraseñas no coinciden');
      return;
    }

    const data = {
      token: this.token,
      nueva_contraseña: this.password,
    };

    this.http.post('http://localhost:8000/Password/reset-password', data).subscribe({
      next: (response: any) => {
        alert('Contraseña actualizada correctamente');
        this.router.navigate(['/auth/sign-in']);
      },
      error: (err) => {
        console.error(err);
        alert('Error al actualizar la contraseña');
      },
    });
  }
}
