// main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import emailjs from 'emailjs-com'

// —— CSRF Token 配置 ——  
const tokenMeta = document.querySelector('meta[name="csrf-token"]')
if (tokenMeta) {
  const csrfToken = tokenMeta.getAttribute('content')
  axios.defaults.headers.common['X-CSRFToken'] = csrfToken
  axios.defaults.xsrfCookieName = 'csrftoken'
  axios.defaults.xsrfHeaderName = 'X-CSRFToken'
}

// —— 初始化 EmailJS ——  
// 请确认这里的 Public Key 与控制台里看到的一致
emailjs.init('Zt0XmmEON9ohWldYP')

const app = createApp(App)

app.use(store)
app.use(router)

// 可选：把 axios 挂到全局，组件里直接 this.$axios
app.config.globalProperties.$axios = axios

app.mount('#app')
