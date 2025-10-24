import { Component, OnInit, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-inicio',
  templateUrl: './inicio.html',
  styleUrls: ['./inicio.scss']
})
export class InicioComponent implements OnInit, OnDestroy {
  
  // Lista de todas las rutas de tus slides
  slides = [
    { id: 0, url: 'assets/img/fondo-carrusel.jpg', link: '/catalogo' },
    { id: 1, url: 'assets/img/slide2.png', link: '/contacto' },
    { id: 2, url: 'assets/img/slide3.jpg', link: '/acerca-de' }
  ];

  currentSlideIndex = 0;
  intervalId: any;

  constructor() { }

  ngOnInit(): void {
    // 1. Inicia el carrusel cuando el componente se carga
    this.startCarousel();
  }

  startCarousel() {
    // 2. Cambia de slide cada 5 segundos (5000 milisegundos)
    this.intervalId = setInterval(() => {
      this.nextSlide();
    }, 5000); 
  }

  nextSlide() {
    // 3. Calcula el índice del próximo slide
    this.currentSlideIndex = (this.currentSlideIndex + 1) % this.slides.length;
  }

  ngOnDestroy(): void {
    // 4. Limpia el intervalo cuando el componente se destruye para evitar fugas de memoria
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }
}