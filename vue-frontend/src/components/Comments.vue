<template>
<div>
    <div class="card my-4">
      <h5 class="card-header">Прокомментируй:</h5>
      <div class="card-body">
        <form v-if="isAuthenticated" @submit.prevent="createComment">
          <div class="form-group">
            <textarea v-model="content" class="form-control" rows="3"></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
      </div>
    </div>
    <div class="media mb-4" v-for="comment in comments" :key="comment.id">
      <img class="d-flex mr-3 rounded-circle" height="50" width="50" src="https://pbs.twimg.com/media/DgKNKWiWkAAhPvL.png" alt="">
      <div class="media-body">
        <h5 class="mt-0">{{ comment.author }}</h5>
        {{ comment.content }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Comments",
  data() {
    return {
      content: '',
      comments: [],
      isAuthenticated: this.$store.state.isAuthenticated
    }
  },
  methods: {
    async createComment() {
      const formData = {
        content: this.content,
        post: this.$route.params.slug
      }
      const response = await axios.post('http://127.0.0.1:8000/api/comment/create/', formData)
      this.comments.push(response.data)
      this.content = ''
    },
    async getComments() {
      const response = await axios.get(`http://127.0.0.1:8000/api/post-comments/${this.$route.params.slug}`)
      this.comments = response.data
  }
  },
  watch: {
    '$route.params.slug': {
      immediate: true,
      handler: 'getComments'
    }
  }
}
</script>

<style scoped>

</style>