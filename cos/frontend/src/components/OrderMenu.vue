<template>
  <div class=ordermenu>
    <div class="menu-container" v-for="item in menu" :key="item.id">
      <menu-item :onClick="consoleClick" :name="item.name"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MenuItem from './MenuItem'

axios.interceptors.request.use(request => {
  console.log('Starting Request', request)
  return request
})

export default {
  name: 'ordermenu',
  props: {
    menu: Array
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
  margin: auto;
  height: 150vh;
}
.menu-container {
  background-color: #aaa;
  display: inline-block;
}
.row {
  padding: 10px;
}
.row-item {
  display: inline-block;
  padding: 15px;
}
</style>
