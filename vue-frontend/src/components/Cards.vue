<template>
        <div v-for="post in posts" :key="post.slug" class="col-md-4">
            <div class="card mb-4 shadow-sm">
                <img :src="post.poster" alt="" class="card-img-top">
                <div class="card-body">
                    <h4 class="card-title">{{ post.title }}</h4>
                    <div v-html="post.content" class="truncate"></div>
                    <div class="mb-2">
                      <span v-for="tag in post.tags">
                        <a href="#" class="mr-1 badge badge-info">#{{ tag }}</a>
                      </span>
                    </div>
                    <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                            <router-link :to="`/post/${post.slug}`" class="btn btn-sm btn-outline-secondary">Подробнее</router-link>
                        </div>
                        <small class="text-muted">{{ post.created_date.slice(0, 10) }}</small>
                    </div>
                </div>
            </div>
        </div>
</template>

<script>
export default {
  name: "cards",
  props: {
    posts: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
.truncate {
  height: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>