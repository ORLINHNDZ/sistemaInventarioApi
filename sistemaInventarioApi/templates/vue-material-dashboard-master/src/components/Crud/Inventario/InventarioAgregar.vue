<template>
    <form novalidate class="md-layout" >
      <md-card class="md-layout-item md-size-50 md-small-size-100">
        <md-card-header>
          <div v-if="form.id!=''" class="md-title">Editar Registro</div>
          <div v-else class="md-title">Nuevo Inventariado</div>
          
          
        </md-card-header>

        <md-card-content>

          
         
             <div class="md-layout-item md-small-size-100">
              <md-field >
                <label for="producto">Nombre de Producto</label>
                <md-select id="producto" name="producto" v-model="form.producto">
                  <md-option v-for="producto in tipoProductos" :value="producto.id" :key="producto.id">{{producto.nombreProducto}}</md-option>
                 
                </md-select>
              </md-field>
            </div>
           
         <div class="md-layout-item md-small-size-100">
              <md-field >
                <label for="proveedor">Nombre de Proveedor</label>
                <md-select id="proveedor" name="proveedor" v-model="form.proveedor">
                  <md-option v-for="proveedor in tipoUsuarios" :value="proveedor.id" :key="proveedor.id">{{proveedor.nombreUsuario}}</md-option>
                 
                </md-select>
              </md-field>
            </div>


          <div class="md-layout md-gutter">
              <div class="md-layout-item md-small-size-100">
              <md-field >
                <label for="isv">Precio Costo</label>
                <md-input type="number" id="precioCosto" name="precioCosto" autocomplete="precioCosto" v-model="form.precioCosto" />
               
              </md-field>
            </div>

             <div class="md-layout-item md-small-size-100">
              <md-field >
                <label for="isv">Precio Venta</label>
                <md-input type="number" id="precioVenta" name="precioVenta" autocomplete="precioVenta" v-model="form.precioVenta" />
               
              </md-field>
            </div>

            

            <div class="md-layout-item md-small-size-100">
              <md-field >
                <label for="isv">Existencia</label>
                <md-input type="number" id="existencia" name="existencia" autocomplete="existencia" v-model="form.existencia" />
               
              </md-field>
            </div>
          </div>

         
        </md-card-content>

        

        <md-card-actions>
          
          <md-button  @click.prevent="guardarProducto" class="md-primary" >Guardar</md-button>
          
          
        </md-card-actions>
      </md-card>

      
    </form>
  
</template>

<script>
import axios from "axios";


export default {
  
  name: "FormValidation",

   mounted() {
     
     var id = this.$route.params.id

     if (id!=null){
       axios.get('http://localhost:8000/api/inventario/'+id+'/edit').then((res) => {
                console.log(res.data)
                this.form = res.data
                
            })
     }
     


     axios.get('http://localhost:8000/api/productos').then((res) => {
                 console.log(res.data)
                this.tipoProductos = res.data.results
            })
     axios.get('http://localhost:8000/api/usuarios').then((res) => {
                 console.log(res.data)
                this.tipoUsuarios = res.data.results
            })
},

  data() {
    
    return {
     tipoProductos:[],
     tipoUsuarios:[],
      form: {
        id: '',
        producto: '',
        proveedor: '',
        precioCosto: '',
        precioVenta: '',
        existencia: '',
      },
    };
  },
  methods: {
    guardarProducto() {
      var datos = {
        id: this.form.id,
        producto: this.form.producto,
        proveedor: this.form.proveedor,
        precioCosto: this.form.precioCosto,
        precioVenta: this.form.precioVenta,
        existencia: this.form.existencia,
      };
      var router = this.$router;
      var id = this.$route.params.id;
      //Si existe id entonces hará un put, de lo contrario baja al else y hará un post (create)
      if (this.form.id != '') {
        axios
          .put("http://localhost:8000/api/inventario/" + id + "/edit", datos)
          .then((respuesta) => {
            if (respuesta.statusText == "OK") {
              router.push("/InventarioList");
            } else {
              console.log("Error" + res.data.results);
              alert("Error al editar entrada");
            }
          });
      } else {
        axios
          .post('http://localhost:8000/api/inventario/create', datos)
          .then((res) => {
            if (res.statusText == "Created") {
              router.push("/InventarioList");
            } else {
              console.log("Error" + res.data.results);
              alert("Error al crear entrada");
            }
          });
      }
    },
  },
};
</script>
<style>
md-card-content {
  margin: 120 auto;
}
</style>