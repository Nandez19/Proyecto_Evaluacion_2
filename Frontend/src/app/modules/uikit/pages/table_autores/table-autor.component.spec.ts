import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TableAutorComponent } from './table-autor.component';

describe('TableClienteComponent', () => {
  let component: TableAutorComponent;
  let fixture: ComponentFixture<TableAutorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TableAutorComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(TableAutorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

