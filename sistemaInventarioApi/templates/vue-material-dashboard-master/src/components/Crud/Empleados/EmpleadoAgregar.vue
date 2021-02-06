<template >
<div class="centera">
    <form novalidate class="md-layout">
      <div class="center">
      <md-card class="md-layout-item md-size-50 md-small-size-100">
        <md-card-header>
          <div v-if="form.id!=''" class="md-title">Editar Usuario</div>
          <div v-else class="md-title">Nuevo Usuario</div>
          
          
        </md-card-header>

        <md-card-content>

          
          <div class="md-layout md-gutter">
            
            <div class="md-layout-item md-small-size-100">
              <md-field>
                <label for="nombreUsuario">Nombre Usuario</label>
                <md-input name="nombreUsuario" id="nombreUsuario" autocomplete="family-name" v-model="form.nombreUsuario"  />
               
              </md-field>
            </div>

             <div class="md-layout-item md-small-size-100">
              <md-checkbox v-model="form.isActive">Usuario Activo</md-checkbox>
            </div>
          </div>

          <div class="md-layout md-gutter">
             <div class="md-layout-item md-small-size-100">
              <md-field>
                <label for="identidad">Identidad</label>
                <md-input name="identidad" id="identidad" autocomplete="family-name" v-model="form.identidad"  />
               
              </md-field>
            </div>

             <div class="md-layout-item md-small-size-100">
              
            
                <md-checkbox v-model="form.isAdmin">Admin</md-checkbox>
              
            
            </div>

              

      
          </div>

             <md-field >
                <label for="primerNombre">Primer Nombre</label>
                <md-input name="primerNombre" id="primerNombre" autocomplete="primerNombre" v-model="form.primerNombre"  />
                
              </md-field>

              <md-field >
                <label for="apellido">Apellido</label>
                <md-input name="apellido" id="apellido" autocomplete="apellidoo" v-model="form.apellido" />
                
              </md-field>
              <div>
                 <label for="fechaNacimiento">Fecha de Nacimiento</label>
                <md-datepicker name="fechaNacimiento" id="fechaNacimiento" v-model="form.fechaNacimiento"  md-immediately />
              </div>
                            
              
               
              
               <md-field >
                <label for="roles">Roles</label>
                <md-select id="" name="" v-model="form.roles">
                  <md-option v-for="roles in tipoRoles" v-bind:value="roles.id" :key="roles.id">{{roles.id}}</md-option>
                 
                </md-select>
              </md-field>
               <md-field >
                <label for="correo">Correo</label>
                <md-input name="correo" id="correo" autocomplete="correo" v-model="form.correo" />
                
              </md-field>
               <md-field >
                <label for="telefono">Telefono</label>
                <md-input name="telefono" id="telefono" autocomplete="telefono" v-model="form.telefono" />
                
              </md-field>
              
             
               <div>
                <md-radio v-model="form.genero" value="M">Masculino </md-radio>
                <md-radio v-model="form.genero" value="F" class="md-primary">Femenino</md-radio>
               </div>
            
                
              

               <md-field >
                <label for="rtn">RTN</label>
                <md-input name="rtn" id="rtn" autocomplete="rtn" v-model="form.rtn" />
                
              </md-field>

               <md-field >
                <label for="direccion">Dirección</label>
                <md-input name="direccion" id="direccion" autocomplete="direccion" v-model="form.direccion" />
                
              </md-field>
        </md-card-content>

        

        <md-card-actions>
          
          <md-button  @click.prevent="guardarProducto" class="md-primary" >Guardar Usuario</md-button>
          
          
        </md-card-actions>
      </md-card>
      </div>
      
    </form>
    </div>
  
</template>

<script>
import axios from "axios";
import DatePicker from 'vue-md-date-picker';

export default {
  
  name: "FormValidation",

   mounted() {
     
     var id = this.$route.params.id

     if (id!=null){
       axios.get('http://localhost:8000/api/usuarios/'+id+'/edit').then((res) => {
                console.log(res.data)
                this.form = res.data
                
            })
     }
     


     axios.get('http://localhost:8000/api/roles').then((res) => {
                 console.log(res.data)
                this.tipoRoles = res.data.results
            })
},

  data() {
    
    return {
     tipoRoles:[],
      form: {
        id: '',
        nombreUsuario: '',
        isActive: false,
        isAdmin: false,
        identidad: '',
        primerNombre: '',
        apellido: '',
        fechaNacimiento: null,
        genero: '',
        roles: '',
        correo: '',
        telefono: '',
        rtn: '',
        direccion: '',
      },
    };
  },
  methods: {
    guardarProducto() {
      var datos = {
        id: this.form.id,
        nombreUsuario: this.form.nombreUsuario,
        isActive: this.form.isActive,
        isAdmin: this.form.isAdmin,
        identidad: this.form.identidad,
        primerNombre: this.form.primerNombre,
        apellido: this.form.apellido,
        fechaNacimiento: this.form.fechaNacimiento,
        genero: this.form.genero,
        roles: this.form.roles,
        correo: this.form.correo,
        telefono: this.form.telefono,
        rtn: this.form.rtn,
        direccion: this.form.direccion,
      };
      var router = this.$router;
      var id = this.$route.params.id;
      //Si existe id entonces hará un put, de lo contrario baja al else y hará un post (create)
      if (this.form.id != '') {
        axios
          .put("http://localhost:8000/api/usuarios/" + id + "/edit", datos)
          .then((respuesta) => {
            if (respuesta.statusText == "OK") {
              router.push("/empleadosList");
            } else {
              console.log("Error" + res.data.results);
              alert("Error al editar entrada");
            }
          });
      } else {
        axios
          .post('http://localhost:8000/api/usuarios/create', datos)
          .then((res) => {
            if (res.statusText == "Created") {
              router.push("/empleadosList");
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

.center {
  margin: center;
  width: 95%; 
  padding: 10px;
  text-align: center;
}
.centera {
  margin: center;
  width: 95%; 
  padding: 10px;
  text-align: center;
}
a.b {
  font-size: large;
  
}
</style>