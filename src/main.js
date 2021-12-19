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


axios.interceptors.request.use(
	config => {
		let token = localStorage.getItem('Authorization');
		if(token){
			config.headers.common['token'] = token
		}
		return config
	},
	err => {
		return Promise.reject(err);
	}
)