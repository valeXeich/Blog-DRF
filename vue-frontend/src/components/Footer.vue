<template>
<footer class="footer">
    <div class="container">
        <p class="float-right">
            <a href="#">Наверх</a>
        </p>
        <span class="text-muted">Агентство по разработке потрясных сайтов на bootstrap, drf vuejs. А это просто наш блог.</span>
    </div>
</footer>
</template>

<script>
export default {
  name: "my-footer"
}
</script>

<style scoped>
footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 10px;
    line-height: 60px;
    background-color: #f5f5f5;
}
</style>