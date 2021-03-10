<template>
  <div id="app">
    <section class="dashboard">
      <div class="dashboard__row">
        <latest-transactions-chart style="flex:2" :entries="transactions" />
        <transaction-breakdown-chart  :entries="transactions" />
      </div>
      <div class="dashboard__row">
        <transaction-details-grid id="td-grid" :entries="transactions" />
      </div>

    </section>
  </div>
</template>

<script>
import transactions from '@/data/transactions.js';

import LatestTransactionsChart from '@/components/Views/charts/LatestTransactionsChart.vue';
import TransactionBreakdownChart from '@/components/Views/charts/TransactionBreakdownChart.vue';
import TransactionDetailsGrid from '@/components/Views/charts/TransactionDetailsGrid.vue';

export default {
  name: 'app',
  components: {
    LatestTransactionsChart,
    TransactionBreakdownChart,
    TransactionDetailsGrid,
  },
  data() {
    return {
      transactions,
    }
  },
  mounted() {
  }
}
</script>
