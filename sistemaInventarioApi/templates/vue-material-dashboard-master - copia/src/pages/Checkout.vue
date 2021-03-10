<template>

  
      
    <div :gutter="20">

        <h1 class="center">Lista de Productos</h1>

        
        <product-list></product-list>
     
        <h1 class="center">Productos a Pagar</h1>
        <shopping-cart></shopping-cart>
        <p class="center"><b>Total Cost: ${{ totalCost }}</b></p>
     
    </div>
    
</template>



<script>
import axios from 'axios'
import ProductList from "@/components/Views/ProductList.vue";
import NavBar from "@/components/Views/NavBar.vue";
import ShoppingCart from "@/components/Views/ShoppingCart.vue";
import {Store} from '@/store/store'

export default {
  name: 'DialogConfirm',
  
	data() {
    return {
    productos: [],
	  active: false,
    value: null,
    showDialog: false,
    search: ""
    
    }},
     mounted() {
    this.cargarEntrada()
  },
  components: {
    ProductList,
    ShoppingCart
  },
  computed: {
    totalCost(){
      return Store.totalCost
    },
    cart(){
			return Store.$data.cart
    },
    
  }
  
};
</script>

<style lang="scss" scoped>
  .center {
  margin: center;
  width: 95%; 
  padding: 10px;
  text-align: center;
}
.right {
    padding-bottom: -10px;
    text-align: right;
  }
</style>
