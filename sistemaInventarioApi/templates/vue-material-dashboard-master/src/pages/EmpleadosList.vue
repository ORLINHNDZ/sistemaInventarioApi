<template>
  <div class="content">
    <div class="md-layout">
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100"
      >
        <md-card>
          <md-card-header data-background-color="green">
            <md-button  data-background-color="blue" :to="{name:'EmpleadoAgregar'}">Agregar Nuevo empleado</md-button>
           
            <h4 class="title">Empleados</h4>
            <p class="category"></p>
          </md-card-header>
          <md-card-content>
            <empleado-table table-header-color="green"></empleado-table>
          </md-card-content>
        </md-card>
      </div>

     
    </div>
  </div>
</template>

<style lang="scss" scoped>
  md-button {
    display: position right;
  }
</style>

<script>
import EmpleadoTable from '../components/Crud/Empleados/EmpleadoTable.vue';


export default {
  components: {
    EmpleadoTable
  }
  
 

  
};
</script>

