<template>
<div>
    <div class="container">
        <p class="my-3">Другие теги:
          <router-link :to="`/tags/${tag.slug}`" class="badge badge-success mr-1" v-for="tag in tags" :key="tag.slug">#{{tag.title}} </router-link>
        </p>
        <div class="row">
          <div v-if="posts" v-for="post in posts" :key="post.slug" class="col-md-4">
            <div class="card mb-4 shadow-sm">
              <img src="https://docs.microsoft.com/ru-ru/learn/achievements/python-install-vscode-social.png" alt="" class="card-img-top">
              <div class="card-body">
                <h4 class="card-title">{{ post.title }}</h4>
                <div v-html="post.content" class="truncate"></div>
                <div class="mb-2">
              <span v-for="tag in post.tags">
                <router-link :to="`/tags/${tag}`" class="mr-1 badge badge-info">#{{ tag }}</router-link>
              </span>
                </div>
                <div class="d-flex justify-content-between align-items-center">
                  <div class="btn-group">
                    <router-link :to="`/post/${post.slug}`" class="btn btn-sm btn-outline-secondary">Подробнее</router-link>
                  </div>
                  <small class="text-muted">{{ post.created_date }}</small>
                </div>
              </div>
            </div>
          </div>
        </div>
      <h4 v-if="posts.length === 0" class="text-center mt-2">Постов с таким тегов нету</h4>
      </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Tags",
  data() {
    return {
      posts: [],
      tags: []
    }
  },
  methods: {
    async getPostByTag() {
      const tag_slug = this.$route.params.slug
      const response = await axios.get(`http://127.0.0.1:8000/api/tag/${tag_slug}`)
      this.posts = response.data.results
    },
    async getTags() {
      const response = await axios.get('http://127.0.0.1:8000/api/tag/list')
      this.tags = response.data
    }
  },
  mounted() {
    this.getTags()
  },
  watch: {
    'posts': {
      immediate: true,
      handler: 'getPostByTag'
    },
  }
}
</script>

<style scoped>

</style>