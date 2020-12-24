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
        <md-table-cell>Producto</md-table-cell>
        <md-table-cell>Proveedor</md-table-cell>
        <md-table-cell>Precio de Costo</md-table-cell>
        <md-table-cell>Precio de Venta</md-table-cell>
        <md-table-cell>Existencia</md-table-cell>
        <md-table-cell>Acciones</md-table-cell>
      </md-table-row>
      <md-table-row  v-for="inventario in inventarios" v-bind:key="inventario.producto">
        
        <md-table-cell>{{ inventario.producto }}</md-table-cell>
        <md-table-cell>{{ inventario.proveedor }}</md-table-cell>
        <md-table-cell>{{ inventario.precioCosto }}</md-table-cell>
        <md-table-cell>{{ inventario.precioVenta }}</md-table-cell>
        <md-table-cell>{{ inventario.existencia }}</md-table-cell>
        <md-table-cell>
          <router-link :to="{name:'InventarioEditar', params:{id:inventario.id}}">Editar</router-link>
          
         
        </md-table-cell>
         <md-table-cell>
          
          
          <a @click.prevent="eliminarEntrada(inventario.id)" href="#">Eliminar</a>
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
  name: "tabla-inventario",
  data() {
    return {
    
      inventarios: [],
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
        producto: this.search
      }
       let vue = this;
     axios.get('http://localhost:8000/api/inventario', { params }).then((res) => {
                console.log(res.data)
                this.inventarios = res.data.results
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

      
      axios.delete('http://localhost:8000/api/inventario/'+id+'/delete')
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
