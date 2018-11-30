<template>
  <div class=ordermenu>
    <div class="menu-container">
      <div class=row v-for="i in Math.ceil(items.length / 3)" v-bind:key="i">
        <span class="row-item" v-for="item in items.slice((i - 1) * 3, i * 3)" :key='item.id'>
          <menu-item :onClick="consoleClick" :name="item.name"/>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import MenuItem from './MenuItem'

export default {
  name: 'ordermenu',
  data () {
    return {
      items: [
        {
          id: 0,
          name: 'taco'
        },
        {
          id: 1,
          name: 'burrito'
        },
        {
          id: 2,
          name: 'margarita'
        },
        {
          id: 3,
          name: 'chimichanga'
        },
        {
          id: 4,
          name: 'al pastor'
        },
        {
          id: 5,
          name: 'cochinita pibil'
        }
      ]
    }
  },
  components: {
    'menu-item': MenuItem
  },
  methods: {
    consoleClick () {
      console.log('button clicked')
    }
  }
}
</script>

<style>
.ordermenu {
  background-color: #bbbbbb;
  max-width: 60%;
  margin: auto;
  height: 1000px;
}
.menu-container {
  background-color: #aaa;
}
.row {
  padding: 10px;
}
.row-item {
  display: inline-block;
  padding: 15px;
}
</style>
