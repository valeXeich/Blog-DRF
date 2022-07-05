<template>
  <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <nav aria-label="breadcrumb" class="mt-4">
            <ol class="breadcrumb">
              <li class="breadcrumb-item"><a href="/" >Главная</a></li>
              <li class="breadcrumb-item active" aria-current="page">{{ post.title }}</li>
            </ol>
          </nav>
          <img class="img-fluid rounded " src="https://docs.microsoft.com/ru-ru/learn/achievements/python-install-vscode-social.png" alt="">
          <hr>
          <p v-html="post.content"></p>
          <div class="d-flex justify-content-end">
            <span v-for="tag in post.tags">
                  <a class="mr-1 badge badge-info">#{{ tag }}</a>
            </span>
          </div>
          <hr>
          <div class="d-flex">
            <router-link class="mr-auto p-2 lead author" :to="`/profile/${post.author}`">{{ post.author }}</router-link>
<!--            <div class="mr-auto p-2 lead">Автор: {{ post.author }}</div>-->
            <div class="p-2">Опубликовано: {{ post.created_date.slice(0, 10) }}</div>
          </div>
          <hr>
          <Comments :post="post.id"/>
        </div>
        <Aside :tags="tags" :posts="posts"></Aside>
      </div>
    </div>
</template>

<script>
import axios from "axios";
import Aside from "@/components/Aside";
import Comments from "@/components/Comments";
export default {
  name: "PostDetail",
  components: {
    Aside,
    Comments
  },
  data() {
    return {
      post: '',
      posts: [],
      tags: [],
    }
  },
  methods: {
    async fetchPost() {
      const post_slug = this.$route.params.slug
      const response = await axios.get(`http://127.0.0.1:8000/api/post/detail/${post_slug}`)
      this.post = response.data
    },
    async getLastPosts() {
      const response = await axios.get('http://127.0.0.1:8000/api/aside/')
      this.posts = response.data
    },
    async getTags() {
      const response = await axios.get('http://127.0.0.1:8000/api/tag/list')
      this.tags = response.data
    }
  },
  mounted() {
    this.getLastPosts()
    this.getTags()
  },
  watch: {
    '$route.params.slug': {
      immediate: true,
      handler: 'fetchPost'
    }
  }
}
</script>

<style scoped>
.author {
  text-decoration: none
}
</style>