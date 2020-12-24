<template>
    <form novalidate class="md-layout" >
      <md-card class="md-layout-item md-size-50 md-small-size-100">
        <md-card-header>
          <div v-if="form.id!=''" class="md-title">Editar Producto</div>
          <div v-else class="md-title">Nuevo Producto</div>
          
          
        </md-card-header>

        <md-card-content>

          
          <div class="md-layout md-gutter">
             <div class="md-layout-item md-small-size-100">
              <md-field >
                <label for="tipoProductos">Tipo de Producto</label>
                <md-select id="tipoProductos" name="tipoProductos" v-model="form.tipoProductos">
                  <md-option v-for="tipoProductos in tipoPro" :value="tipoProductos.id" :key="tipoProductos.id">{{tipoProductos.tipoProducto}}</md-option>
                 
                </md-select>
              </md-field>
            </div>
           

            <div class="md-layout-item md-small-size-100">
              <md-field>
                <label for="nombreProducto">Nombre</label>
                <md-input name="nombreProducto" id="nombreProducto" autocomplete="family-name" v-model="form.nombreProducto"  />
               
              </md-field>
            </div>
          </div>

          <div class="md-layout md-gutter">
             <div class="md-layout-item md-small-size-100">
              <md-field >
                <label for="imagen">Imagen</label>
                <md-input name="imagen" id="imagen" autocomplete="given-name" v-model="form.imagen"  />
                
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field >
                <label for="marca">Marca</label>
                <md-input name="marca" id="marca" autocomplete="given-name" v-model="form.marca" />
              
              </md-field>
            </div>

            

            <div class="md-layout-item md-small-size-100">
              <md-field >
                <label for="isv">ISV%</label>
                <md-input type="number" id="isv" name="isv" autocomplete="isv" v-model="form.isv" />
               
              </md-field>
            </div>
          </div>

          <md-field >
                <label for="nombrePopular">Nombre Popular</label>
                <md-input name="nombrePopular" id="nombrePopular" autocomplete="nombrePopular" v-model="form.nombrePopular"  />
                
              </md-field>

              <md-field >
                <label for="descripcionProducto">Descripción</label>
                <md-input name="descripcionProducto" id="descripcionProducto" autocomplete="descripcionProducto" v-model="form.descripcionProducto" />
                
              </md-field>

            <p>Seleccion:{{form.tipoProductos}}</p>
        </md-card-content>

        

        <md-card-actions>
          
          <md-button  @click.prevent="guardarProducto" class="md-primary" >Editar Producto</md-button>
          
          
        </md-card-actions>
      </md-card>

      
    </form>
  
</template>

<script>
import axios from 'axios'

export default {
  name: 'FormValidation',

    mounted() {
     
     var id = this.$route.params.id

     if (id!=null){
       axios.get('http://localhost:8000/api/productos/'+id+'/edit').then((res) => {
                console.log(res.data)
                this.form = res.data
                
            })
     }
     


     axios.get('http://localhost:8000/api/tipoProductos').then((res) => {
                 console.log(res.data)
                this.tipoPro = res.data.results
            })
},
  
    data() {
      return {
         tipoPro : [],
         form: {
          id: '',
          tipoProductos : '',
          nombreProducto: '',
          imagen: null,
          marca: '',
          isv: '',
          nombrePopular: '',
          descripcionProducto: ''
      }
      }
    },
    methods: {
      guardarProducto(){
        var datos ={
          id:this.form.id,
          tipoProducto:this.form.tipoProductos,
          nombreProducto:this.form.nombreProducto,
          imagen:this.form.imagen,
          marca:this.form.marca,
          isv:this.form.isv,
          nombrePopular:this.form.nombrePopular,
          descripcionProducto:this.form.descripcionProducto
        }
        var router = this.$router
        var id = this.$route.params.id
        //Si existe id entonces hará un put, de lo contrario baja al else y hará un post (create)
         if(this.form.id!=''){
             axios.put('http://localhost:8000/api/productos/'+id+'/edit', datos)
            .then((respuesta) => {
               if(respuesta.statusText=='OK'){
                          router.push('/table')
                          console.log(datos)
                        }else{
                          console.log('Error'+res.data.results)
                          alert('Error al editar entrada')
                        }
              
         })
         }else{
            axios.post('http://localhost:8000/api/productos/create', datos)
                      .then((res) => {
                        if(res.statusText=='Created'){
                          
                          router.push('/table')
                        }else{
                          console.log('Error'+res.data.results)
                  
                          alert('Error al crear entrada')
                        }
                        
                    })
         }

       
        }
         
      },
    }

</script>