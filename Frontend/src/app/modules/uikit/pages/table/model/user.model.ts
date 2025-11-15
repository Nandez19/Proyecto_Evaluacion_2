/*export interface User {
  id: number;
  name: string;
  age: number;
  username: string;
  email: string;
  phone: string;
  website: string;
  occupation: string;
  hobbies: string[];
  selected: boolean;
  status: number;
  created_at: string;
}*/


export interface User {
  Id_Usuario: string;            // UUID (string en JSON)
  Username: string;
  Correo: string;
  Telefono?: string;
  Nombre: string;
  Password_Hash: string;
  Rol: string;
  Activo: boolean;
  Id_usuario_creacion?: string;
  Id_usuario_actualizacion?: string;
  Fecha_creacion: string;        // se maneja como string ISO
  Fecha_actualizacion?: string;  // opcional
  selected?: boolean;            // campo adicional para tu frontend (checkboxes)
}
  
