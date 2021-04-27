<template>
<div>
	<md-field
    :data="cart"
    stripe
    style="width: 100%">
	
        
		<md-table class="center">
     	<md-table-row >
        <md-table-cell><h6>Producto</h6></md-table-cell>
        <md-table-cell><h6>Precio</h6></md-table-cell>
        <md-table-cell><h6>Cantidad</h6></md-table-cell>
        <md-table-cell><h6>ISV</h6></md-table-cell>
        <md-table-cell><h6>Acciones</h6></md-table-cell>
     	</md-table-row>

		 <md-table-row  v-for="prods in cart" v-bind:key="prods.id"  >
        
        
        <md-table-cell>{{ prods.details.nombreProducto }}</md-table-cell>
        <md-table-cell>{{ prods.details.precio }}</md-table-cell>
        <md-table-cell>{{ prods.cantidad }}</md-table-cell>
        <md-table-cell>{{ prods.details.isv }}</md-table-cell>
		<template >
        <md-table-cell><button class="material-icons" type="success"    @click="cantidadMas" size="mini">add</button>
      	<button class="material-icons" type="danger"  @click='removeFromCart(cart.details.id)' size="mini">remove</button ></md-table-cell>
         </template>
      	</md-table-row>
		</md-table>
		 
		
	</md-field>
  
	<md-dialog :md-active.sync="showDialog" class="factura">
      <div class="center">
      <p>Fecha y hora <br> RTN: 020302938273929</p>
      <md-dialog-title>CONVENIENCIAS TROCHEZ</md-dialog-title>
      <p>La Masica, Atlántida <br> Calle principal una cuadra antes de Bodega Mangys Store<br>frente a Sazón y Antojos</p>
      <p>TEL (+504) 9641-2997<br>leutroche20@gmail.com</p>
      <h6>Datos del Comprador</h6>
      <p>Fecha de reimpresión:<br>Nombre: CONSUMIDOR FINAL<br>RTN:0000000000000000</p>
      <h6>---Descripción de la Factura---</h6>
      <p></p>
      </div>
        
          <md-table class="center">
     	<md-table-row >
        <md-table-cell>Producto</md-table-cell>
        <md-table-cell>Precio</md-table-cell>
        <md-table-cell>Cantidad</md-table-cell>
        <md-table-cell>ISV</md-table-cell>

        
     	</md-table-row>

		 <md-table-row  v-for="prods in cart" v-bind:key="prods.id"  >
        
        
        <md-table-cell>{{ prods.details.nombreProducto }}</md-table-cell>
        <md-table-cell>{{ prods.details.precio }}</md-table-cell>
        <md-table-cell>{{ prods.cantidad }}</md-table-cell>
        <md-table-cell>{{ prods.details.isv }}</md-table-cell>
		
      	</md-table-row>
		</md-table>
      <p class="center"><b>Total ISV : ${{ totalIsv  }}</b></p>
    	<p class="center"><b>Total : ${{ totalCost + totalIsv }}</b></p>
       <div class="center">
        
        <md-button class="md-primary" @click="onConfirm">Confirmar</md-button>
        </div>
    
    </md-dialog>
    
    <div class="centerB">
    <md-button class="md-primary md-raised" @click="showDialog = true">Pagar</md-button>
  </div>
</div>
</template>

<script>
import {Store} from '@/store/store'
import axios from 'axios'
export default {
	name: 'DialogConfirm',
	data: () => ({
	  active: false,
	  value: null,
	  showDialog: false,
    }),
	computed: {
		
		totalCost(){
     		 return Store.totalCost
   		 },
    totalIsv(){
     		 return Store.totalIsv
   		 },
    cantidadMas(){
     		 return Store.cantidadMas
   		 },    
		cart(){
			return Store.$data.cart
		}
		
	},
	methods: {
    
		removeFromCart(id){
			Store.removeFromCart(id)
		},
		
		addToCart(product){
  		Store.addToCart(product)
    },
    
		onConfirm () {
         this.value = 'Agreed'
         var router = this.$router;
         this.$router.go(0);
		},
		onCancel () {
			this.value = 'Disagreed'
		},
		}
	}

</script>
<style lang="scss" scoped>
  .md-dialog  .md-dialog-container {
    max-width: 768px;
  }
  .center {
  margin: center;
  width: 100%; 
  padding: 10px;
  text-align: center;
}
.centerB {
  margin: center;
  width: 95%; 
  padding: 10px;
  text-align: center;
}
.factura {
 
  height: 868px;
  max-width: 768px;
  max-height: 768px;
  padding: 10px;
  text-align: center;
}
</style>