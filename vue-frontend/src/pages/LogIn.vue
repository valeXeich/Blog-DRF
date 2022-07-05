<template>
  <div>
    <div class="text-center">
      <form class="form-signin" @submit.prevent="submitForm">
        <h1 class="h3 mb-3 mt-3 font-weight-normal">Пожалуйста укажите логин и пароль</h1>
        <label for="inputUsername" class="sr-only">Имя пользователя</label>
        <input id="inputUsername" class="form-control" placeholder="Имя пользователя" required="" v-model="login">
        <label for="inputPassword" class="sr-only">Пароль</label>
        <input type="password" id="inputPassword" class="form-control mt-2" placeholder="Пароль" required="" v-model="password">
        <button class="btn mt-2 btn-lg btn-primary btn-block" type="submit">Войти</button>
      </form>
      <div class="alert alert-danger mt-2" role="alert" v-if="errors.length">
       <p v-for="error in errors" :key="error">{{ error }}</p>
    </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
export default {
  name: "LogIn",
  data() {
    return {
      login: '',
      password: '',
      errors: []
    }
  },
  methods: {
    async submitForm() {
    axios.defaults.headers.common["Authorization"] = ""
    this.$store.commit('removeToken')
    const formData = {
      username: this.login,
      password: this.password
    }
    try {
      const response = await axios.post('http://127.0.0.1:8000/auth/jwt/create/', formData);
      const token_access = response.data.access
      const token_refresh = response.data.refresh
      localStorage.setItem('token_access', token_access)
      localStorage.setItem('token_refresh', token_refresh)
      axios.defaults.headers.common["Authorization"] = 'Bearer ' + token_access
      const user_info = await axios.get('http://127.0.0.1:8000/auth/users/me/')
      localStorage.setItem('username', user_info.data.username)
      await this.$router.push('/')
    } catch (e) {
      this.errors.push('Логин или пароль неверны')
    }
  }
}
}

</script>

<style scoped>
.form-signin {
  margin-left: 700px;
  margin-right: 700px;
}

.alert {
  margin-left: 700px;
  margin-right: 700px;
}
</style>