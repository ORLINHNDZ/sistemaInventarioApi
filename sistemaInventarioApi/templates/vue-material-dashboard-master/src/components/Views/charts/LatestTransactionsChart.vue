<template>
    <zingchart :data="chartConfig" :height="'100%'"/>
</template>
<script>
import 'zingchart/es6';
import zingchartVue from 'zingchart-vue';
export default {
  props: ['entries'],
  computed: {
    values() {
      return this.entries.map(o => {
          return [o.timestamp, parseFloat(o.amount.slice(1,-1))]
       });
    },
    chartConfig() {
      // TODO: Add a series object
      return {
        type: 'line',
        title: {
          text: 'Latest Transactions',
          adjustLayout: true,
          align: 'left',
          margin: 0,
          fontColor: '#5d7d9a'
        },
        subtitle: {
          text: 'Last 30 days',
          align: 'left',
          fontColor: '#5d7d9a'
        },
        plot: {
          aspect: 'spline',
          marker: {
            visible: false,
          },

        },
        crosshairX:{
          plotLabel :{
            negation: "currency",
            text: '$%v',
            'thousands-separator': ","
          },
          marker: {
            visible: false,
          }
        },
        tooltip: { 
          visible: false,

        },
        plotarea: {
          margin: '35 35 60 60'

        },
        scaleX: {
          transform: {
            type: 'date',
            all: '%M %d',
          }
        },
        scaleY: {
          label: {
            text: 'Amount in USD',
          },
          short:true,
          shortUnit: 'K',
        },
        series: [
          {
            values: this.values,
            text: 'Sales'
          }
        ],
      };
    }
  },
}
</script>