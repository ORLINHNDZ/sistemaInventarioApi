<template>
  <div class="content">
    <div class="md-layout">
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100"
      >
        <md-card>
          <md-card-header data-background-color="green">
            <div class="right">
            <md-button class="md-plane md-primary" data-background-color="blue" :to="{name:'EmpleadoAgregar'}">
            <md-icon>add</md-icon>
            </md-button>
            </div>
                      
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
  .right {
    padding-bottom: -10px;
    text-align: right;
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

