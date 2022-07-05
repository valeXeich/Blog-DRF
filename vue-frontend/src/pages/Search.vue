<template>
<div class="container">
<div>
  <div class="row">
    <div class="col-lg-12">
      <nav aria-label="breadcrumb" class="mt-4">
        <ol class="breadcrumb">
          <li class="breadcrumb-item"><router-link to="/">Главная</router-link></li>
          <li class="breadcrumb-item active" aria-current="page">Поиск</li>
        </ol>
      </nav>
      <p class="lead">Найдено записей: {{ posts.length }}</p>
      <div class="container">
        <div class="row">
          <cards :posts="posts"></cards>
        </div>
      </div>
    </div>
  </div>
</div>
</div>
</template>

<script>
import axios from "axios";
import Cards from "@/components/Cards";
export default {
  name: "Search",
  components: {
    Cards
  },
  data() {
    return {
      posts: []
    }
  },
  methods: {
    async fetchSearch() {
      const response = await axios.get(`http://127.0.0.1:8000/api/post/list/?q=${this.$route.query.q}`)
      this.posts = response.data.results
    }
  },
  watch: {
    '$route.query.q': {
      immediate: true,
      handler: 'fetchSearch'
    }
  }
}
</script>

<style scoped>

</style>