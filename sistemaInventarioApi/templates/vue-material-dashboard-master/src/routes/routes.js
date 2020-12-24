import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";

import Dashboard from "@/pages/Dashboard.vue";
import UserProfile from "@/pages/UserProfile.vue";
import TableList from "@/pages/TableList.vue";
import EmpleadosList from "@/pages/EmpleadosList.vue";
import InventarioList from "@/pages/InventarioList.vue";
import Typography from "@/pages/Typography.vue";
import List from "@/components/List";
import Icons from "@/pages/Icons.vue";
import Maps from "@/pages/Maps.vue";
import Notifications from "@/pages/Notifications.vue";
import UpgradeToPRO from "@/pages/UpgradeToPRO.vue";
import ProductoAgregar from "@/components/Crud/Productos/ProductoAgregar.vue";
import EmpleadoAgregar from "@/components/Crud/Empleados/EmpleadoAgregar.vue";
import InventarioAgregar from "@/components/Crud/Inventario/InventarioAgregar.vue";


const routes = [
    {
        path: "/",
        component: DashboardLayout,
        redirect: "/dashboard",
        children: [
            {
                path: "dashboard",
                name: "Dashboard",
                component: Dashboard
            },
            {
                path: "user",
                name: "User Profile",
                component: UserProfile
            },
            {
                path: "table",
                name: "Lista de Productos",
                component: TableList
            },

            {
                path: "icons",
                name: "Icons",
                component: Icons
            },
            {
                path: "maps",
                name: "Maps",
                meta: {
                    hideFooter: true
                },
                component: Maps
            },
            {
                path: "notifications",
                name: "Notifications",
                component: Notifications
            },
            {
                path: "upgrade",
                name: "Upgrade to PRO",
                component: UpgradeToPRO
            },
            //Productos
            {
                path: "/producto/agregar",
                name: "ProductoAgregar",
                component: ProductoAgregar
            },
            {
                path: "/producto/:id/editar",
                name: "ProductoEditar",
                component: ProductoAgregar
            },
            //Empleados
            {
                path: "empleadosList",
                name: "Lista de Empleados",
                component: EmpleadosList
            },
 
            {
                path: "/empleado/agregar",
                name: "EmpleadoAgregar",
                component: EmpleadoAgregar
            },
            
            {
                path: "/empleado/:id/editar",
                name: "EmpleadoEditar",
                component: EmpleadoAgregar
            }, 
            //Inventario
            
            {
                path: "InventarioList",
                name: "Lista de inventario",
                component: InventarioList
            },

            {
                path: "/inventario/agregar",
                name: "InventarioAgregar",
                component: InventarioAgregar
            },
            
            
            {
                path: "/inventario/:id/editar",
                name: "InventarioEditar",
                component: InventarioAgregar
            }, 
            // Ventas 
            /*
            {
                path: "InventarioList",
                name: "Lista de inventario",
                component: InventarioList
            },

            {
                path: "/inventario/agregar",
                name: "InventarioAgregar",
                component: InventarioAgregar
            },
            
            
            {
                path: "/inventario/:id/editar",
                name: "InventarioEditar",
                component: InventarioAgregar
            }, 
           */
           
        ]
    }
];

export default routes;
