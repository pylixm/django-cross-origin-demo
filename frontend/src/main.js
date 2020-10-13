// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import axios from 'axios'
import VueResource from 'vue-resource'
import Cookies from 'js-cookie'

// axios.interceptors.request.use((config) => {
//   config.headers['X-Requested-With'] = 'XMLHttpRequest';
//   let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
//   config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
//   return config
// });



Vue.use(VueResource)
Vue.use(Cookies)
Vue.config.productionTip = false

// axios.defaults.withCredentials=false
Vue.prototype.$axios = axios



/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
