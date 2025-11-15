import { MenuItem } from '../models/menu.model';

export class Menu {
  public static pages: MenuItem[] = [
    {
      group: 'Biblioteca ITM',
      separator: false,
      items: [
        {
          icon: 'assets/icons/heroicons/outline/lock-closed.svg',
          label: 'Auth',
          route: '/auth',
          roles: [], // 👈 Array vacío = visible para todos (incluso sin login)
          children: [
            { 
              label: 'Registrarse', 
              route: '/auth/sign-up',
              roles: [] // 👈 Todos pueden registrarse
            },
            { 
              label: 'Entrar', 
              route: '/auth/sign-in',
              roles: [] // 👈 Todos pueden entrar
            },
          ],
        },
        {
          icon: 'assets/icons/heroicons/outline/chart-pie.svg',
          label: 'Inicio',
          route: '/dashboard',
        },
        {
          icon: 'assets/icons/heroicons/outline/book-open.svg',
          label: 'Libros',
          route: '/dashboard/libros',
        },
          roles: ['Administrador'], // 👈 Todos los autenticados
          children: [
            { 
              label: 'Libros', 
              route: '/dashboard/nfts',
              roles: [] // 👈 Todos
            }
          ],
        },
        {
          icon: 'assets/icons/heroicons/outline/cube.svg',
          label: 'Auditoría', // 👈 Cambié el texto
          route: '/components',
          children: [
            { label: 'Gestión de Libros', route: '/dashboard/admin-libros' }, // Una sola página con tabs
            { label: 'Autores', route: '/dashboard/admin-autores' },
            { label: 'Bibliotecarios', route: '/dashboard/admin-bibliotecarios' },
            { label: 'Clientes', route: '/dashboard/admin-clientes' },
            { label: 'Usuarios', route: '/components/table' }
          roles: ['Administrador'], // 👈 Solo admin y gerente VEN este grupo
          children: [
            { 
              label: 'Usuarios', 
              route: '/components/table',
              roles: ['Administrador'] // 👈 Solo admin y gerente
            },
            { 
              label: 'Clientes', 
              route: '/components/table_cliente',
              roles: ['Administrador']// 👈 Admin, gerente y vendedor
            },
            { 
              label: 'Autores', 
              route: '/components/table_autores',
              roles: ['Administrador'] // 👈 Solo admin
            }
          ],
        },
      ],
    },
    {
      group: 'Configuraciones',
      separator: false,
      items: [
        {
          icon: 'assets/icons/heroicons/outline/cog.svg',
          label: 'Ajustes',
          route: '/settings',
        },
        {
          icon: 'assets/icons/heroicons/outline/bell.svg',
          label: 'Notificaciones',
          route: '/gift',
        },
        {
          icon: 'assets/icons/heroicons/outline/folder.svg',
          label: 'Folders',
          route: '/folders',
          children: [
            { label: 'Current Files', route: '/folders/current-files' },
            { label: 'Downloads', route: '/folders/download' },
            { label: 'Trash', route: '/folders/trash' },
          ],
        },
      ],
    },
  ];
}