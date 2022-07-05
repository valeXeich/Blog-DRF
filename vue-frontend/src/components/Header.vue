<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
    <a href="#" class="navbar-brand">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="30" height="30" alt="logo">
    </a>
    <a href="#" class="navbar-brand">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Vue.js_Logo_2.svg/1184px-Vue.js_Logo_2.svg.png" width="30" height="30" alt="logo">
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <router-link :to="'/'" class="nav-link">Главная</router-link>
            </li>
            <li class="nav-item ">
                <a href="#" class="nav-link">Контакты</a>
            </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
            <input name="q" v-model="q" type="text" class="form-control mr-sm-2" placeholder="Поиск" aria-label="Поиск">
            <button class="btn btn-outline-success my-2 my-sm-0 mr-2" type="submit" @click.stop.prevent="submit()">Поиск</button>
        </form>
        <router-link v-if="!isAuthenticated" :to="'/log-in'" class="btn btn-outline-light mr-2">Вход</router-link>
        <router-link v-if="!isAuthenticated" :to="'/sign-up'" class="btn btn-outline-light mr-2">Регистрация</router-link>
        <router-link :to="`/profile/${username}`" class="navbar-text mr-2" v-if="username">{{ username }}</router-link>
        <button v-if="isAuthenticated" @click="logOut" class="btn btn-outline-light">Выход</button>
    </div>
</nav>
</template>

<script>
import axios from "axios";

export default {
  name: "my-header",
  data() {
    return {
      q: null,
      isAuthenticated: this.$store.state.isAuthenticated,
      username: ''
    }
  },
  methods: {
    submit() {
      this.$router.push('/search?q='+this.q)
    },
    logOut() {
      localStorage.removeItem('token_access')
      localStorage.removeItem('token_refresh')
      axios.defaults.headers.common['Authorization'] = ''
      this.isAuthenticated = false
    },
    async getInfoUser() {
      if(this.isAuthenticated) {
        const response = await axios.get('http://127.0.0.1:8000/auth/users/me/')
        this.username = response.data.username
      }
    }
  },
  mounted() {
    this.getInfoUser()
  }
}
</script>

<style scoped>

</style>