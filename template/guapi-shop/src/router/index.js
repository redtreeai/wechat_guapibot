import Vue from 'vue'
import Router from 'vue-router'
import _ from 'lodash'

Router.prototype.openPage = function (link, query) {
  this.push({
    path: link,
  })
}

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/mine'
    },


    {
      path: '/mine',
      name: 'mine',
      component(resolve){
        require(['@/views/mine/index.vue'], resolve)
      }
    },


    {
      path: '/pay',
      name: 'pay',
      component(resolve){
        require(['@/views/pay/index.vue'], resolve)
      }
    },
    {
      path: '/addr',
      name: 'addr',
      component(resolve){
        require(['@/views/addr/index.vue'], resolve)
      }
    },
   {
      path: '/addaddr',
      name: 'addaddr',
      component(resolve){
        require(['@/views/addaddr/index.vue'], resolve)
      }
    },
     {
      path: '/order',
      name: 'order',
      component(resolve){
        require(['@/views/order/index.vue'], resolve)
      }
    },
    {
      path: '/qusebi',
      name: 'qusebi',
      component(resolve){
        require(['@/views/goods/qusebi/index.vue'], resolve)
      }
    },
    {
      path: '/shuidi',
      name: 'shuidi',
      component(resolve){
        require(['@/views/goods/shuidi/index.vue'], resolve)
      }
    },
    {
      path: '/qibing',
      name: 'qibing',
      component(resolve){
        require(['@/views/goods/qibing/index.vue'], resolve)
      }
    },











  ]
})
