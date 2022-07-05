<template>
<nav aria-label="Paginate me">
  <ul class="pagination justify-content-center">
    <router-link v-if="previous != null" class="page-link" :to="previous" tabindex="-1">Предыдущая</router-link>
    <li v-if="previous != null" class="page-item disabled">
      <a class="page-link disabled" href="#" tabindex="-1">Предыдущая</a>
    </li>
    <span v-if="total > 1" v-for="i in total">
      <li  v-if="current_page === i || ($route.query.page === '/' && i === 1)" class="page-item active">
        <router-link class="page-link" :to="`?page=${i}`">{{i}}</router-link></li>
      <li v-else class="page-item">
        <router-link class="page-link" :to="`?page=${i}`">{{i}}</router-link></li>
    </span>
    <router-link v-if="next != null" class="page-link" :to="next">Следующая</router-link>
    <li v-if="next != null" class="page-item disabled">
      <a class="page-link" href="#">Следующая</a>
    </li>
  </ul>
</nav>
<br>
</template>

<script>
export default {
  name: "pagination",
  props: ['previous', 'total', 'current_page', 'next']
}
</script>

<style scoped>

</style>