<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">
  <my-header></my-header>
  <router-view></router-view>
  <my-footer></my-footer>
</template>


<script>
import MyHeader from "@/components/Header";
import MyFooter from "@/components/Footer";
import axios from "axios";
export default {
  components: {
    MyFooter,
    MyHeader,
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const access = this.$store.state.token_access
    if (access) {
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + access
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
    console.log(localStorage.getItem('username'))
  },
  mounted() {
    setInterval(() => {
      this.getAccess()
    }, 40000)
  },
  methods: {
    async getAccess(e) {
      const refresh = localStorage.getItem('token_refresh')
      const response = await axios.post('http://127.0.0.1:8000/auth/jwt/refresh/', {refresh: refresh})
      localStorage.setItem('token_access', response.data.access)
    }
  }
}

</script>

<style>
body {
    margin-bottom: 60px;
}

html {
    position: relative;
    min-height: 100%;
}
</style>
