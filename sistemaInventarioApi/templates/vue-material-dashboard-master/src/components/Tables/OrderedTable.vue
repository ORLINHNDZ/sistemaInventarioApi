<template>
  <div>
    <div class="tabla-productos">
      <h1>Listado de Productos</h1>
      <table>
        <tr>
          <td>Tipo Producto</td>
          <td>TP</td>
          <td>TP</td>
          <td>TP</td>
          <td>TP</td>
          <td>TP</td>
          <td>TP</td>
        </tr>
        <tr v-for="producto in productos" v-bind:key="producto">
          <h1 v-if="producto">{{ producto.tipoProducto }}</h1>

          <td v-if="producto">{{ producto.tipoProducto }}</td>
          <td v-if="producto">{{ producto.nombreProducto }}</td>
          <td v-if="producto">{{ producto.imagen }}</td>
          <td v-if="producto">{{ producto.marca }}</td>
          <td v-if="producto">{{ producto.isv }}</td>
          <td v-if="producto">{{ producto.nombrePopular }}</td>
          <td v-if="producto">{{ producto.descripcionProducto }}</td>


        </tr>
      </table>


    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
export default {
  name: "tabla-productos",
  data() {
    return {
      productos: []

    }
  },
  mounted() {
    let vue = this;
    axios.get('http://localhost:8000/api/productos')
        .then(function (response) {
          vue.productos = response.data;
        })
  }
}

</script>
