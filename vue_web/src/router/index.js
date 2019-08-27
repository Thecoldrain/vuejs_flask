import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import login from '@/login/login'
import js_test from "@/components/js_test";

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: "/login",
      component: login
    },
    {
      path:"/test",
      component:js_test
    }


  ]
})
