<template>
  <div>
    
    <md-table>
      <md-table-row >
        <md-table-cell>Nombre de Usuario</md-table-cell>
        <md-table-cell>Estado</md-table-cell>
        <md-table-cell>Admin</md-table-cell>
        <md-table-cell>Identidad</md-table-cell>
        <md-table-cell>Primer Nombre</md-table-cell>
        <md-table-cell>Apellido</md-table-cell>
        <md-table-cell>Fecha de Nacimiento</md-table-cell>
        <md-table-cell>Genero</md-table-cell>
        <md-table-cell>Rol</md-table-cell>
        <md-table-cell>Email</md-table-cell>
        <md-table-cell>Telefono</md-table-cell>
        <md-table-cell>Rtn</md-table-cell>
        <md-table-cell>Dirección</md-table-cell>
        <md-table-cell>Acciones</md-table-cell>
      </md-table-row>
      <md-table-row  v-for="usuario in usuarios" v-bind:key="usuario.nombreUsuario"  >
        
        <md-table-cell>{{ usuario.nombreUsuario }}</md-table-cell>
        <md-table-cell>{{ usuario.isActive }}</md-table-cell>
        <md-table-cell>{{ usuario.isAdmin }}</md-table-cell>
        <md-table-cell>{{ usuario.identidad }}</md-table-cell>
        <md-table-cell>{{ usuario.primerNombre }}</md-table-cell>
        <md-table-cell>{{ usuario.apellido }}</md-table-cell>
        <md-table-cell>{{ usuario.fechaNacimiento }}</md-table-cell>
        <md-table-cell>{{ usuario.genero }}</md-table-cell>
        <md-table-cell>{{ usuario.roles }}</md-table-cell>
        <md-table-cell>{{ usuario.correo }}</md-table-cell>
        <md-table-cell>{{ usuario.telefono }}</md-table-cell>
        <md-table-cell>{{ usuario.rtn }}</md-table-cell>
        <md-table-cell>{{ usuario.direccion }}</md-table-cell>
        <md-table-cell>
          <router-link :to="{name:'EmpleadoEditar', params:{id:usuario.id}}">Editar</router-link>
          
         
        </md-table-cell>
         <md-table-cell>
          
          
          <a @click.prevent="eliminarEntrada(usuario.id)" href="#">Eliminar</a>
        </md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "tabla-usuarios",
  data() {
    return {
    
      usuarios: []

    }
  },
  mounted() {
   this.cargarEntrada()
},
  methods:{

    cargarEntrada(){
       let vue = this;
     axios.get('http://localhost:8000/api/usuarios').then((res) => {
                console.log(res.data)
                this.usuarios = res.data.results
            });
    },
    eliminarEntrada(id){

      var op = window.confirm("¿Desea eliminar el registro permanentemente?")
      if (op){

      
      axios.delete('http://localhost:8000/api/usuarios/'+id+'/delete')
      .then((respuesta)=>{
        console.log(respuesta)
        this.cargarEntrada()
      })
      }
    }
  }
}
</script>
