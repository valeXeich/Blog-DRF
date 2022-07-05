import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router/router";
import store from "@/store"
import axios from "axios";


const app = createApp(App)

// axios.defaults.baseURL = 'http://127.0.0.1:8000/'

app.use(router)
app.use(store)
app.mount('#app')

// const ax = axios.create({
//   baseURL: 'http://127.0.0.1:8000/',
//   headers: {
//     'Content-type': 'application/json'
//   }
// })


