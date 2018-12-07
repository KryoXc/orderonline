import Vue from 'vue'
import Router from 'vue-router'
import Shop from '@/components/Shop'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/clients/onlineordering',
      name: 'Shop',
      component: Shop
    },
    {
      path: '/clients/onlineorderbackend',
      name: 'ShopFlask',
      component: Shop
    }
  ],
  mode: 'history'
})
