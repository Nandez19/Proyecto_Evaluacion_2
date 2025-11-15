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
          children: [
            { label: 'Registrarse', route: '/auth/sign-up' },
            { label: 'Entrar', route: '/auth/sign-in' },
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
        {
          icon: 'assets/icons/heroicons/outline/cube.svg',
          label: 'Auditoria (Solo admin)',
          route: '/components',
          children: [
            { label: 'Usuarios', route: '/components/table' },
            { label: 'Clientes', route: '/components/table_cliente' },
            { label: 'Gestión de Libros', route: '/dashboard/admin-libros' }, // Una sola página con tabs
            { label: 'Gestión de Autores', route: '/dashboard/admin-autores' },
            { label: 'Gestión de Préstamos', route: '/dashboard/Prestamos' },
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