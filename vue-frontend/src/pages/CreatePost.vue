<template>
  <h3 class="text-center mt-4">Создание поста</h3>
  <form @submit.prevent="createPost" class="frm" enctype="multipart/form-data">
    <div class="mb-3 ">
      <label for="exampleFormControlInput1" class="form-label">Название: </label>
      <input v-model="title" type="text" class="form-control" required id="exampleFormControlInput1">
      <p class="error" v-if="errors.title">*{{ errors.title }}</p>
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label">Контент поста: </label>
      <textarea v-model="content" required class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
      <p class="error" v-if="errors.content">*{{ errors.content }}</p>
    </div>
    <div class="mb-3">
      <label for="formFile" class="form-label">Выберите постер поста: </label>
      <br>
      <input @change="onFileChange" required class="" ref="file" type="file" id="formFile">
      <p class="error" v-if="errors.image">*{{ errors.image }}</p>
    </div>
    <label>Выберите теги: </label>
    <select v-model="selected_tags" class="form-select form-control scl" multiple size="5" required>
      <option v-for="tag in tags" :key="tag.id" :value="tag.id">{{ tag.title }}</option>
    </select>
    <p class="error" v-if="errors.tags">*{{ errors.tags }}</p>
    <button type="submit" class="btn btn-primary mt-3 float-right">Создать</button>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "CreatePost",
  data() {
    return {
      title: '',
      content: '',
      poster: null,
      selected_tags: [],
      tags: [],
      errors: {
        'title': '',
        'content': '',
        'tags': '',
        'poster': ''
      }
    }
  },
  methods: {
    async createPost() {
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      const formData = {
        title: this.title,
        content: this.content,
        tags: JSON.stringify(this.selected_tags),
        poster: this.poster
      }
      try {
        await axios.post('http://127.0.0.1:8000/api/post/create', formData, config);
        await this.$router.push('/')
      } catch (e) {
        this.errors = [{}]
        if (e.response.data['taken']) {
          this.errors.title = 'Название уже занято'
        }
        if (e.response.data['number']) {
          this.errors.title = 'В название не должно быть чисел'
        }
        if (e.response.data['title_length']) {
          this.errors.title = 'Название должно иметь не менее 5 символов'
        }
        if (e.response.data['content_length']) {
          this.errors.content = 'Контент должен иметь не менее 50 символов'
        }
        if (e.response.data['tag_id']) {
          this.errors.tags = 'Выберите хотя бы один тег'
        }
        if (e.response.data['poster']) {
          this.errors.image = 'Неправильный формат изображени'
        }
        console.log(e)
      }
      this.title = '';
      this.content = '';
      this.$refs.file.value=null;
      this.selected_tags = []
    },
    async fetchTags() {
      const response = await axios.get('http://127.0.0.1:8000/api/tag/list')
      this.tags = response.data
    },
    onFileChange() {
      this.poster = this.$refs.file.files.item(0)
    },
  },
  mounted() {
    this.fetchTags()
  }
}
</script>

<style scoped>
.frm {
  width: 50%;
  margin-left: auto;
  margin-right: auto;
}

.scl {
  width: 950px
}

.error {
  color: red
}
</style>