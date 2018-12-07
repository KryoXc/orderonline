<template>
  <div class="menu-item" @click="onClick">
    {{ name }}
  </div>
</template>

<script>

export default {
  name: 'menu-item',
  props: {
    name: String,
    onClick: {
      type: Function,
      required: true
    }
  }
}
</script>

<style>
.menu-item {
  border-radius: 10px;
  box-shadow: 2px 2px;
  background-color: #dddddd;
  height: 200px;
  width: 200px;
  margin: 15px;;
}
.menu-item:hover {
  background-color: #00cc00;
  height: 205px;
  width: 205px;
  transition: all 0.3s ease-out;
}
.menu-item:not(:hover) {
  .background-color: #ddd;
  height: 200px;
  width: 200px;
  transition: all 0.3s ease;
}
</style>
