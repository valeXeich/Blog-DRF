<template>
  <div class="text-center">
    <form @submit.prevent="submitForm" class="form-signin">
      <h1 class="h3 mb-3 mt-3 font-weight-normal">Для регистрации укажите имя пользователя и пароль</h1>
      <label for="inputUsername" class="sr-only">Имя пользователя</label>
      <input id="inputUsername" class="form-control" placeholder="Имя пользователя" required="" v-model="username">
      <label for="inputPassword" class="sr-only">Пароль</label>
      <input type="password" id="inputPassword" class="form-control mt-2" placeholder="Пароль" required="" v-model="password">
      <label for="ReInputPassword" class="sr-only">Повторите пароль</label>
      <input type="password" id="ReInputPassword" class="form-control mt-2" placeholder="Повторите пароль" required="" v-model="password2">
      <button class="btn mt-2 btn-lg btn-primary btn-block" type="submit">Регистрация</button>
    </form>
    <div class="alert alert-danger mt-2" role="alert" v-if="errors.length">
       <p v-for="error in errors" :key="error">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignUp",
  data() {
    return {
      username: '',
      password: '',
      password2: '',
      errors: [],
      success: ''
    }
  },
  methods: {
    async submitForm() {
      this.errors = []

      if (this.username === '') {
        this.errors.push('Укажите пользователя')
      }

      if (this.password === '') {
        this.errors.push('Пароль слишком короткий')
      }

      if (this.password2 !== this.password) {
        this.errors.push('пароли не совпадают')
      }

      if (this.errors.length === 0) {
        const formData = {
          username: this.username,
          password: this.password
        }
        try {
          const response = await axios.post('http://127.0.0.1:8000/auth/users/', formData);
          await this.$router.push('/log-in')
        } catch(e) {
          if (e.response.data.username[0] === 'A user with that username already exists.') {
            this.errors.push('Такой пользователь уже существует')
          } else {
            this.errors.push('Что-то пошло не так')
          }
          this.username = '';
          this.password = '';
          this.password2 = '';
        }
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