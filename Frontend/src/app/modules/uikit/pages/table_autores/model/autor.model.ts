export interface Autor {
  Id_Autor: string;           // UUID
  Cedula_Autor: string;
  Nombre: string;
  Telefono?: string;
  Edad?: string;
  selected?: boolean; 
}