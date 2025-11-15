import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminBibliotecariosComponent } from './admin-bibliotecarios.component';

describe('AdminBibliotecariosComponent', () => {
  let component: AdminBibliotecariosComponent;
  let fixture: ComponentFixture<AdminBibliotecariosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminBibliotecariosComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AdminBibliotecariosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});