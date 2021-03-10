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
        <md-table-cell><h6>Acciones</h6></md-table-cell>
     	</md-table-row>

		 <md-table-row  v-for="prods in cart" v-bind:key="prods.id"  >
        
        
        <md-table-cell>{{ prods.details.nombreProducto }}</md-table-cell>
        <md-table-cell>{{ prods.details.precio }}</md-table-cell>
        <md-table-cell>{{ prods.cantidad }}</md-table-cell>
		<template >
        <md-table-cell><button class="material-icons" type="success"  @click='addToCart(cart.details)' size="mini">add</button>
      	<button class="material-icons" type="danger"  @click='removeFromCart(cart.details.id)' size="mini">remove</button ></md-table-cell>
         </template>
      	</md-table-row>
		</md-table>
		 
		
	</md-field>
	<md-dialog :md-active.sync="showDialog">
      <md-dialog-title>Preferences</md-dialog-title>

      <md-tabs md-dynamic-height>
        <md-tab md-label="General">
          <md-table class="center">
     	<md-table-row >
        <md-table-cell>Producto</md-table-cell>
        <md-table-cell>Precio</md-table-cell>
        <md-table-cell>Cantidad</md-table-cell>
        <md-table-cell>Acciones</md-table-cell>
     	</md-table-row>

		 <md-table-row  v-for="prods in cart" v-bind:key="prods.id"  >
        
        
        <md-table-cell>{{ prods.details.nombreProducto }}</md-table-cell>
        <md-table-cell>{{ prods.details.precio }}</md-table-cell>
        <md-table-cell>{{ prods.cantidad }}</md-table-cell>
		<template >
        <md-table-cell><button class="material-icons" type="success"  @click='addToCart(prods.details)' size="mini">add</button>
    	<button class="material-icons" type="danger"  @click='removeFromCart(prods.details.id)' size="mini">remove</button ></md-table-cell>
         </template>
      	</md-table-row>
		</md-table>
    	<p class="center"><b>Total : ${{ totalCost  }}</b></p>
        </md-tab>
		

        <md-tab md-label="Activity">
          <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam mollitia dolorum dolores quae commodi impedit possimus qui, atque at voluptates cupiditate. Neque quae culpa suscipit praesentium inventore ducimus ipsa aut.</p>
          <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam mollitia dolorum dolores quae commodi impedit possimus qui, atque at voluptates cupiditate. Neque quae culpa suscipit praesentium inventore ducimus ipsa aut.</p>
          <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam mollitia dolorum dolores quae commodi impedit possimus qui, atque at voluptates cupiditate. Neque quae culpa suscipit praesentium inventore ducimus ipsa aut.</p>
          <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam mollitia dolorum dolores quae commodi impedit possimus qui, atque at voluptates cupiditate. Neque quae culpa suscipit praesentium inventore ducimus ipsa aut.</p>
          <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam mollitia dolorum dolores quae commodi impedit possimus qui, atque at voluptates cupiditate. Neque quae culpa suscipit praesentium inventore ducimus ipsa aut.</p>
        </md-tab>

        <md-tab md-label="Account">
          <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam mollitia dolorum dolores quae commodi impedit possimus qui, atque at voluptates cupiditate. Neque quae culpa suscipit praesentium inventore ducimus ipsa aut.</p>
          <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ullam mollitia dolorum dolores quae commodi impedit possimus qui, atque at voluptates cupiditate. Neque quae culpa suscipit praesentium inventore ducimus ipsa aut.</p>
        </md-tab>
      </md-tabs>

      <md-dialog-actions>
        <md-button class="md-primary" @click="showDialog = false">Close</md-button>
        <md-button class="md-primary" @click="showDialog = false">Save</md-button>
      </md-dialog-actions>
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
		cart(){
			return Store.$data.cart
		}
		
	},
	methods: {
		methods: {
		removeFromCart(id){
			Store.removeFromCart(id)
		},
		
		addToCart(product){
			Store.addToCart(product);
		},
		onConfirm () {
        this.value = 'Agreed'
		},
		onCancel () {
			this.value = 'Disagreed'
		},
		}
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
</style>