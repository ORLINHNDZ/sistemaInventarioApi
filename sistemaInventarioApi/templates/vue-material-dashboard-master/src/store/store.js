import Vue from 'vue';
import products from '../products'

export const Store = new Vue({
	data() {
	    return {
	    	products,
	    	cart: []
	    };
	},
	computed: {
		totalCost(){
			return this.cart.reduce((accum, product) => {	
				return accum + product.details.precio * product.cantidad
			}, 0)
		},

		totalIsv(){
			return this.cart.reduce((accum, product) => {	
				return accum + (product.details.precio * product.details.isv) 
			}, 0)
		},
		

	},
	methods: {
		addToCart(product){
			const locationInCart = this.cart.findIndex(p => {
				return p.details.id === product.id
			})

		    if (locationInCart === -1) {
		        this.cart.push({
		          details: product,
		          cantidad: 1,
		        })
		    } else {
				this.cart[locationInCart].cantidad++
				
		    }
		},
		removeFromCart(id){
			const locationInCart = this.cart.findIndex(p => {
				return p.details.id === id
			})

			if(this.cart[locationInCart].cantidad <= 1){
				this.cart.splice(locationInCart, 1)
			} else {
				this.cart[locationInCart].cantidad--
			}
	
		}
	}
});