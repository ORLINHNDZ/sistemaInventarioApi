<template>
  <div class="content">
    <div class="md-layout">
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100"
      >
        <md-card>
          <md-card-header data-background-color="green">
            <div class="right">
            <md-button class="md-plane md-primary" data-background-color="blue" :to="{name:'ProductoAgregar'}">
            <md-icon>add</md-icon>
            </md-button>
            </div>
            <h4 class="title">Productos Disponibles</h4>
            <p class="category"></p>
          </md-card-header>
          <md-card-content>
            <simple-table table-header-color="green"></simple-table>
          </md-card-content>
        </md-card>
      </div>

     
    </div>
  </div>
</template>

<style>
  .right {
    padding-bottom: -10px;
    text-align: right;
  }
  
</style>

<script>
import { SimpleTable } from "@/components";


export default {
  components: {
    SimpleTable
  },
  
 

  
};
</script>

