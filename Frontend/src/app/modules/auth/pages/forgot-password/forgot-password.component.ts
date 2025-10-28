import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { ButtonComponent } from 'src/app/shared/components/button/button.component';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.css'],
  imports: [FormsModule, RouterLink, HttpClientModule, ButtonComponent],
})
export class ForgotPasswordComponent implements OnInit {
  correo: string = '';

  constructor(private http: HttpClient, private router: Router) {}

  ngOnInit(): void {}

  onSubmit() {
    if (!this.correo) {
      alert('Por favor ingresa tu correo.');
      return;
    }

    this.http
      .post('http://localhost:8000/Password/forgot-password', { correo: this.correo })
      .subscribe({
        next: (response) => {
          alert('Correo de recuperación enviado. Revisa tu bandeja.');
          console.log(response);
        },
        error: (error) => {
          console.error('Error:', error);
          alert('No se pudo enviar el correo. Verifica la dirección o intenta más tarde.');
        },
      });
  }
}
