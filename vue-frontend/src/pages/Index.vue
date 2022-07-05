<template>
  <slider></slider>
  <div class="container">
    <h1 class="my-3">Последние записи блога</h1>
    <div class="row">
      <cards :posts="posts"></cards>
    </div>
  </div>
  <pagination
      :previous="previous"
      :total="total"
      :current_page="current_page"
      :next="next"
  />
  <br>
</template>

<script>
import Cards from "@/components/Cards";
import Pagination from "@/components/Pagination";
import Slider from "@/components/Slider";
import axios from 'axios'
export default {
components: {
    Cards,
    Pagination,
    Slider
  },
  data() {
    return {
      posts: [],
      total: [],
      next: [],
      previous: [],
      current_page: 0,
    }
  },
  methods: {
    async fetchPosts() {
        let page = this.$route.query.page !== undefined ? `?page=${this.$route.query.page}` : '';
        const response = await axios.get(`http://127.0.0.1:8000/api/post/list/${page}`);
        let next = response.data.next !== null ? response.data.next.split('/')[6] : null;
        let previous = response.data.previous !== null ? response.data.previous.split('/')[6] : null;
        let current_page = this.$route.query.page
        this.posts = response.data.results;
        this.total = Math.ceil(response.data.count / 6);
        this.next = next
        this.previous = previous
        this.current_page = Number(current_page)
      console.log(this.posts[4].poster)
    }
  },
  watch: {
  '$route.query.page': {
    immediate: true,
    handler: 'fetchPosts',
  },
},
}
</script>

<style scoped>

</style>