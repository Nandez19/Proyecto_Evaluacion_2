export interface Cliente {
  Id_Cliente: string;           // UUID
  Cedula_Cliente: string;
  Nombre: string;
  Telefono?: string;
  Correo: string;
  selected?: boolean; 
}