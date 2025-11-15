import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminEditorialesComponent } from './admin-editoriales.component';

describe('AdminAutoresComponent', () => {
  let component: AdminEditorialesComponent;
  let fixture: ComponentFixture<AdminEditorialesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminEditorialesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AdminEditorialesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
