<template>
<div>
  <md-field>
        <label>Search</label>
        <md-input v-model="search" type="text" v-on:keyup.enter="searchData"></md-input>
        <md-button class="md-dense md-raised md-primary" v-on:click="searchData">Buscar</md-button>
        </md-field>
	<md-table class="center">
    
        
      <md-table-row >
        <md-table-cell><h6>Producto</h6></md-table-cell>
        <md-table-cell><h6>Precio</h6></md-table-cell>
        <md-table-cell><h6>Acciones</h6></md-table-cell>
     	</md-table-row>
	  <md-table-row :span="12" v-for="(product) in productos" :key="product.id">
	    
	    
	         <md-table-cell>{{ product.nombreProducto }}</md-table-cell>
	         <md-table-cell>${{ product.precio  }}</md-table-cell>
          <md-table-cell> 
	         <div class="bottom clearfix">
	        	<md-button  class="color" type="info" @click='addToCart(product)'>Add to cart</md-button>
	         </div>
          </md-table-cell>
	
	  </md-table-row>
    
	</md-table>
  <div class="centerPagi">
    
      <md-button  class="pagination-previous" v-on:click="changePage( page - 1 )">Anterior</md-button>
          <a class="b"> {{page}} </a>
      <md-button  class="pagination-next" v-on:click="changePage( page + 1 )" >Siguiente</md-button>
   
    </div>
  </div>
  
  
</template>

<script>
import axios from 'axios'
import {Store} from '@/store/store'

export default {
  data() {
    return {
      productos: [],
       page: 1,
      pages: 1,
      search: ""
    };
  },
  mounted() {
   this.cargarEntrada()
  },
  methods: {
  	addToCart(product){
  		Store.addToCart(product)
    },
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
	
  }
}
</script>
<style>
    .color{
        color: blue;
    }
  .image {
    width: 10%;
    display: block;
  } 
  .center {
  margin: center;
  width: 101%; 
  padding: 10px;
  text-align: center;
}
.centerPagi {
  margin: center;
  width: 95%; 
  padding: 10px;
  text-align: center;
}
</style> 

