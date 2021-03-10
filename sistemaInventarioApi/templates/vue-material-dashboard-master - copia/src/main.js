// =========================================================
// * Vue Material Dashboard - v1.4.0
// =========================================================
//
// * Product Page: https://www.creative-tim.com/product/vue-material-dashboard
// * Copyright 2019 Creative Tim (https://www.creative-tim.com)
// * Licensed under MIT (https://github.com/creativetimofficial/vue-material-dashboard/blob/master/LICENSE.md)
//
// * Coded by Creative Tim
//
// =========================================================
//
// * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App";
import MdModalDialog from 'vue-material-modal-dialog'


// router setup
import routes from "./routes/routes";

// Plugins
import GlobalComponents from "./globalComponents";
import GlobalDirectives from "./globalDirectives";
import Notifications from "./components/NotificationPlugin";

// MaterialDashboard plugin
import MaterialDashboard from "./material-dashboard";

import Chartist from "chartist";
import VuePaginate from 'vue-paginate';

//JWT Authentication
import axios from 'axios'
import VueAxios from 'vue-axios'
import jwt_decode from 'jwt-decode'
import Vuex from 'vuex'
import { isLoggedIn } from "@/logic/auth"

//Bootstrap

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


import NavBar from '@/components/Views/NavBar.vue'
import ProductList from '@/components/Views/ProductList.vue'
import ShoppingCart from '@/components/Views/ShoppingCart.vue'
import zingchartVue from 'zingchart-vue'; 
Vue.component('zingchart', zingchartVue);
import ZingGrid from "zinggrid";

// configure router
const router = new VueRouter({
  routes, // short for routes: routes
  linkExactActiveClass: "nav-item active"
});

Vue.prototype.$Chartist = Chartist;

Vue.use(VueRouter);
Vue.use(MaterialDashboard);
Vue.use(GlobalComponents);
Vue.use(GlobalDirectives);
Vue.use(Notifications);
Vue.use(VuePaginate);
Vue.use(Vuex);
Vue.use(VueAxios, axios);
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.component('NavBar', NavBar)
Vue.component('ProductList', ProductList)
Vue.component('ShoppingCart', ShoppingCart)
Vue.use(MdModalDialog)

// Filters
Vue.filter('currency', function (value) {
    return '$' + parseFloat(value/100).toFixed(2);
});

//AUTH 
router.beforeEach((to, from, next) => {
  if (to.name == 'login' && isLoggedIn()) {
    next({ path: '/' })
  }
  else if (!to.meta.allowAnonymous && !isLoggedIn()) {
      next({
          path: '/login',
          query: { redirect: to.fullPath }
      })
  }
  else {
      next()
  }
})

/* eslint-disable no-new */
new Vue({
  el: "#app",
  render: h => h(App),
  router,
  data: {
    Chartist: Chartist
  }
});
