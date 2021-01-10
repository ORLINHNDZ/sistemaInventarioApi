<template>

  <div>
    
    <div class="field has-addons is-pulled-right">
      <div class="control">
        <md-field>
        <label>Search</label>
        <md-input v-model="search" type="text" v-on:keyup.enter="searchData"></md-input>
        <md-button class="md-dense md-raised md-primary" v-on:click="searchData">Buscar</md-button>
        </md-field>
      </div>
    </div>
    <md-table>
      <md-table-row >
        <md-table-cell>Tipo de Producto</md-table-cell>
        <md-table-cell>Nombre</md-table-cell>
        <md-table-cell>Imagen</md-table-cell>
        <md-table-cell>Marca</md-table-cell>
        <md-table-cell>ISV</md-table-cell>
        <md-table-cell>Nombre Popular</md-table-cell>
        <md-table-cell>Descripción</md-table-cell>
        <md-table-cell>Descuento</md-table-cell>
        <md-table-cell>Precio</md-table-cell>
        <md-table-cell>Acciones</md-table-cell>
      </md-table-row>
      <md-table-row  v-for="producto in productos" v-bind:key="producto.nombreProducto"  >
        
        <md-table-cell>{{ producto.tipoProducto }}</md-table-cell>
        <md-table-cell>{{ producto.nombreProducto }}</md-table-cell>
        <md-table-cell>{{ producto.imagen }}</md-table-cell>
        <md-table-cell>{{ producto.marca }}</md-table-cell>
        <md-table-cell>{{ producto.isv }}</md-table-cell>
        <md-table-cell>{{ producto.nombrePopular }}</md-table-cell>
        <md-table-cell>{{ producto.descripcionProducto }}</md-table-cell>
        <md-table-cell>{{ producto.descuento }}</md-table-cell>
        <md-table-cell>{{ producto.precio }}</md-table-cell>
        <md-table-cell>
          <router-link :to="{name:'ProductoEditar', params:{id:producto.id}}">Editar</router-link>
          
         
        </md-table-cell>
         <md-table-cell>
          
          
          <a @click.prevent="eliminarEntrada(producto.id)" href="#">Eliminar</a>
        </md-table-cell>
      </md-table-row>
    </md-table>
    <div class="center" >
    <nav class="pagination" role="navegation" aria-label="pagination">
      <md-button  class="pagination-previous" v-on:click="changePage( page - 1 )">Anterior</md-button>
          <a class="b"> {{page}} </a>
      <md-button  class="pagination-next" v-on:click="changePage( page + 1 )" >Siguiente</md-button>
    </nav>
    </div>
  </div>
  
</template>

<script>
import axios from 'axios'
export default {
  name: "tabla-productos",
  data() {
    return {
    
      productos: [],
      page: 1,
      pages: 1,
      search: ""

    }
  },
  mounted() {
   this.cargarEntrada()
},
  methods:{


    cargarEntrada(){
      const params = {
        page: this.page,
        nombreProducto: this.search
      }
       let vue = this;
     axios.get('http://localhost:8000/api/productos', { params }).then((res) => {
                console.log(res.data)
                this.productos = res.data.results
                this.pages = res.data.pages
            });
    },
    changePage (page){
      this.page = (page <= 0 || page > this.pages) ? this.pages : page
      this.cargarEntrada()
    },
    searchData(){
      this.page = 1;
      this.cargarEntrada();
    },
    eliminarEntrada(id){

      var op = window.confirm("¿Desea eliminar el registro permanentemente?")
      if (op){

      
      axios.delete('http://localhost:8000/api/productos/'+id+'/delete')
      .then((respuesta)=>{
        console.log(respuesta)
        this.cargarEntrada()
      })
      }
    }
  }
}
</script>
<style>
.center {
  margin: center;
  width: 95%; 
  padding: 10px;
  text-align: center;
}
a.b {
  font-size: large;
  
}
</style>