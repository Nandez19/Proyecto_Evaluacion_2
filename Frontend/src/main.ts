import { enableProdMode, importProvidersFrom } from '@angular/core';
import { BrowserModule, bootstrapApplication } from '@angular/platform-browser';
import { provideAnimations } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app/app-routing.module';
import { AppComponent } from './app/app.component';
import { environment } from './environments/environment';
import { provideZonelessChangeDetection } from '@angular/core';
import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { AuthInterceptor } from './app/core/interceptor/auth.interceptor';

// ✅ Habilitar modo producción si aplica
if (environment.production) {
  enableProdMode();
  if (typeof window !== 'undefined') selfXSSWarning();
}

// ✅ Bootstrap principal con providers
bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(
      BrowserModule,
      AppRoutingModule
    ),
    provideAnimations(),
    provideZonelessChangeDetection(),
    provideHttpClient(withInterceptors([AuthInterceptor])),
  ],
}).catch((err) => console.error(err));

// ⚠️ Mensaje de advertencia en consola
function selfXSSWarning() {
  setTimeout(() => {
    console.log(
      '%c⚠️ STOP!',
      'font-weight:bold; font: 2.5em Arial; color: white; background-color: #e11d48; padding: 5px 15px; border-radius: 25px;'
    );
    console.log(
      `%cThis console is intended for developers. Pasting code here can give attackers access to your data.`,
      'font-weight:bold; font: 1.2em Arial; color: #e11d48;'
    );
  });
}
