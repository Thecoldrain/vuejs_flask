// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import top from './top/top'
import axios from 'axios'
import qs from 'qs'
import "vue-resource/dist/vue-resource"
import $ from 'jquery'
import jquery from "jquery"
import "../node_modules/popper.js/dist/popper"
import '../node_modules/bootstrap/dist/js/bootstrap.min'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
import VueJsonp from 'vue-jsonp'
import resource from "./resource"
import Vueresource from "vue-resource"
import VueCookies from "vue-cookies"

Vue.use(VueCookies);
Vue.use(Vueresource);
Vue.http.options.emulateJSON = true;

Vue.config.productionTip = false;


Vue.prototype.$axios = axios;
Vue.prototype.qs = qs;
Vue.component('top',top);

new Vue({
  el: '#app',
  router,
  resource,
  components: { App, },
  template: '<App/>'
});
