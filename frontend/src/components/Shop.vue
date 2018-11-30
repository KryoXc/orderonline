<template>
  <div class="shop">
    <div>
      here's some shopping
    </div>
    <div>
      <ordermenu></ordermenu>
    </div>
  </div>
</template>

<script>
import OrderMenu from './OrderMenu'

export default {
  name: 'shop',
  components: {
    'ordermenu': OrderMenu
  }
}
</script>

<style>
.shop {
  margin: auto;
  height: 1000px;
  background-color: #999999;
  max-width:80%;
}
</style>
