<template>
<div class="col-md-4">
    <div class="card my-4">
      <h5 class="card-header">Теги</h5>
      <div class="card-body">
        <div class="d-flex flex-wrap">
          <router-link :to="`/tags/${tag.slug}`" v-for="tag in tags" :key="tag.title" class="m-2 h5">#{{ tag.title }}</router-link>
        </div>
      </div>
    </div>
    <div class="card my-4">
      <h5 class="card-header">Последние статьи</h5>
      <div class="card-body" v-for="post in posts" :key="post.id">
        <h5 class="card-title">{{ post.title }}</h5>
        <img src="https://docs.microsoft.com/ru-ru/learn/achievements/python-install-vscode-social.png" alt="" class="card-img-top">
        <p class="card-text">{{ post.content }}</p>
        <router-link :to="`/post/${post.slug}`" class="card-link">Ссылка на статью</router-link>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Aside",
  props: {
    tags: {
      type: Array,
      required: true
    },
    posts: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>

</style>