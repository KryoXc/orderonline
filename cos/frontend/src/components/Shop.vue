<template>
  <div class="shop">
    <div>
      here's some shopping
    </div>
    <div class="shop-container">
      <div class="sections-container">
        <sections v-if='false'></sections>
      </div>
      <div class="ordermenu-container">
        <ordermenu v-bind:menu="menu"></ordermenu>
      </div>
      <div class='cart-container'>
        <cart></cart>
      </div>
    </div>
  </div>
</template>

<script>
import OrderMenu from './OrderMenu'
import Cart from './Cart'
import Sections from './Sections'

import axios from 'axios'

export default {
  name: 'shop',
  components: {
    'ordermenu': OrderMenu,
    'cart': Cart,
    'sections': Sections
  },
  data () {
    return {
      menu: [],
      endpoint: 'https://www.cdmorales.net/clients/onlineorderbackend/api/getmenu'
    }
  },
  created () {
    this.getMenu()
  },
  methods: {
    getMenu () {
      axios.get(this.endpoint)
        .then(response => {
          this.menu = response.data
        })
        .catch(error => {
          console.log('-----error-----')
          console.log(error)
        })
    }
  }
}
</script>

<style>
.shop-container {
  display: flex;
  justify-content: space-between;
  margin: auto;
  padding: 15px;
  height: 150vh;
  background-color: #999999;
  max-width:80%;
}
.ordermenu-container {
  width: 60%;
  height: 150vh;
}
.cart-container {
  width: 20%;
  height: 25vh;
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  padding: 15px;
}
.sections-container {
  width: 20%;
  height: 50vh;
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  padding: 15px;
}
</style>
