<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
    <notifications></notifications>

    <side-bar
      :sidebar-item-color="sidebarBackground"
      :sidebar-background-image="sidebarBackgroundImage"
    >
      <mobile-menu slot="content"></mobile-menu>
      <sidebar-link to="/dashboard">
        <md-icon>analytics</md-icon>
        <p>Reportes</p>
      </sidebar-link>
      <sidebar-link to="/empleadosList">
        <md-icon>person</md-icon>
        <p>Usuarios</p>
      </sidebar-link>
      <sidebar-link to="/checkout">
        <md-icon>add_shopping_cart</md-icon>
        <p>Ventas</p>
      </sidebar-link>
      <sidebar-link to="/chart">
        <md-icon>library_books</md-icon>
        <p>Recibos</p>
      </sidebar-link>
      <sidebar-link to="/table">
        <md-icon>fact_check</md-icon>
        <p>Productos</p>
      </sidebar-link>
      <sidebar-link to="/InventarioList">
        <md-icon>inventory_2</md-icon>
        <p>Inventario</p>
      </sidebar-link>
      <sidebar-link to="/upgrade" class="active-pro">
        <md-icon>unarchive</md-icon>
        <p>Acerca</p>
      </sidebar-link>
    </side-bar>

    <div class="main-panel">
      <top-navbar></top-navbar>

      <fixed-plugin
        :color.sync="sidebarBackground"
        :image.sync="sidebarBackgroundImage"
      >
      </fixed-plugin>

      <dashboard-content> </dashboard-content>

      <content-footer v-if="!$route.meta.hideFooter"></content-footer>
    </div>
  </div>
</template>

<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "@/pages/Layout/MobileMenu.vue";
import FixedPlugin from "./Extra/FixedPlugin.vue";

export default {
  components: {
    TopNavbar,
    DashboardContent,
    ContentFooter,
    MobileMenu,
    FixedPlugin
  },
  data() {
    return {
      sidebarBackground: "green",
      sidebarBackgroundImage: require("@/assets/img/sidebar-2.jpg")
    };
  }
};
</script>
