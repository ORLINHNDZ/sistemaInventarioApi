<template>
  <div>
    
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
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "tabla-inventario",
  data() {
    return {
    
      inventarios: []

    }
  },
  mounted() {
   this.cargarEntrada()
},
  methods:{

    cargarEntrada(){
       let vue = this;
     axios.get('http://localhost:8000/api/inventario').then((res) => {
                console.log(res.data)
                this.inventarios = res.data.results
            });
            
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
