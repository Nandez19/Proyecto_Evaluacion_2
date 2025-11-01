import { enableProdMode, importProvidersFrom } from '@angular/core';
import { BrowserModule, bootstrapApplication } from '@angular/platform-browser';
import { provideAnimations } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app/app-routing.module';
import { AppComponent } from './app/app.component';
import { environment } from './environments/environment';
import { provideZonelessChangeDetection } from '@angular/core';
import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { AuthInterceptor } from './app/core/interceptor/auth.interceptor'; // 👈 asegúrate que la carpeta sea plural "interceptors"

if (environment.production) {
  enableProdMode();
  if (window) selfXSSWarning();
}

bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(BrowserModule, AppRoutingModule),
    provideAnimations(),
    provideZonelessChangeDetection(),

    // ✅ Registrar interceptor globalmente (no necesitas withInterceptorsFromDi)
    provideHttpClient(
      withInterceptors([AuthInterceptor])
    ),
  ],
}).catch((err) => console.error(err));

function selfXSSWarning() {
  setTimeout(() => {
    console.log(
      '%c** STOP **',
      'font-weight:bold; font: 2.5em Arial; color: white; background-color: #e11d48; padding: 5px 15px; border-radius: 25px;',
    );
    console.log(
      `%cThis is a browser feature intended for developers. Using this console may allow attackers to impersonate you and steal your information. Do not paste code you don't understand.`,
      'font-weight:bold; font: 1.5em Arial; color: #e11d48;',
    );
  });
}
