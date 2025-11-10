import { animate, state, style, transition, trigger } from '@angular/animations';
import { NgClass } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AngularSvgIconModule } from 'angular-svg-icon';
import { ThemeService } from '../../../../../core/services/theme.service';
import { ClickOutsideDirective } from '../../../../../shared/directives/click-outside.directive';
import { AuthService } from 'src/app/modules/auth/pages/sign-in/services/auth.service';

@Component({
  selector: 'app-profile-menu',
  templateUrl: './profile-menu.component.html',
  styleUrls: ['./profile-menu.component.css'],
  imports: [ClickOutsideDirective, NgClass, RouterLink, AngularSvgIconModule],
  animations: [
    trigger('openClose', [
      state(
        'open',
        style({
          opacity: 1,
          transform: 'translateY(0)',
          visibility: 'visible',
        })
      ),
      state(
        'closed',
        style({
          opacity: 0,
          transform: 'translateY(-20px)',
          visibility: 'hidden',
        })
      ),
      transition('open => closed', [animate('0.2s')]),
      transition('closed => open', [animate('0.2s')]),
    ]),
  ],
})
export class ProfileMenuComponent implements OnInit {
  public isOpen = false;
  public user: any = null;

  public profileMenu = [
    { title: 'Your Profile', icon: './assets/icons/heroicons/outline/user-circle.svg', link: '/profile' },
    { title: 'Settings', icon: './assets/icons/heroicons/outline/cog-6-tooth.svg', link: '/settings' },
    { title: 'Log out', icon: './assets/icons/heroicons/outline/logout.svg', link: '/auth' },
  ];

  public themeMode = ['light', 'dark'];
  public themeDirection = ['ltr', 'rtl'];

  constructor(public themeService: ThemeService, public authService: AuthService) {}

  ngOnInit(): void {
    this.loadUser();
  }

  // -------------------------
  // Cargar usuario
  // -------------------------
  private loadUser(): void {
    // Primero intenta desde el servicio (que puede traer usuario desde login o localStorage)
    this.user = this.authService.getUser();

    if (!this.user) {
      // Si no hay usuario guardado, intenta parsear el token JWT
      this.user = this.authService.getUserFromToken();
    }

    // Si sigue sin usuario, usar valores por defecto
    if (!this.user) {
      this.user = {
        Nombre: 'Usuario',
        Correo: 'correo@ejemplo.com',
        avatar: 'https://avatars.githubusercontent.com/u/12519008?v=4',
      };
    }
  }

  toggleMenu(): void {
    this.isOpen = !this.isOpen;
  }

  toggleThemeMode() {
    this.themeService.theme.update((theme) => {
      const mode = !this.themeService.isDark ? 'dark' : 'light';
      return { ...theme, mode };
    });
  }

  toggleThemeColor(color: string) {
    this.themeService.theme.update((theme) => ({ ...theme, color }));
  }

  setDirection(value: string) {
    this.themeService.theme.update((theme) => ({ ...theme, direction: value }));
  }

  logout(): void {
    this.authService.logout(); // Llamada al logout del AuthService
  }
}
