import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TableClienteComponent } from './table-cliente.component';

describe('TableClienteComponent', () => {
  let component: TableClienteComponent;
  let fixture: ComponentFixture<TableClienteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TableClienteComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(TableClienteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

