import Vue from 'vue'
import App from './App.vue'

import Vuex from "vuex";
import VueRouter from "vue-router";

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';

import router from '@/router'
import store from '@/store'

Vue.config.productionTip = false
Vue.use(Vuex)
Vue.use(VueRouter)
Vue.use(ElementUI)

new Vue({
    el: '#app',
    store: store,
    router,
    render: h => h(App),
    components: {
        App
    }
}).$mount('#app')

import axios from 'axios'
import VueAxios from 'vue-axios'
axios.defaults.baseURL = 'http://127.0.0.1:5000';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';
Vue.use(VueAxios, axios)


// 如果即将进入的路由对象是登录页，则进行跳转，否则验证是否携带accessToken,如果有，则进
// 行跳转，没有，则不允许跳转
// router.beforeEach((to,from,next) => {
// 	// 如果即将进入的路由对象是登录页，则进行跳转，否则验证是否携带accessToken,如果有，则进
// 	// 行跳转，没有，则不允许跳转
//     if((to.path === "/login") || (to.path === "/register")){
//         next()
//     }else{
//         if (sessionStorage.getItem('accessToken')){
//             next()
//         } else {
//             next("/login")
//         }
//     }
// })