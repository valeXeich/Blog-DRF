<template>
  <div class="container">
    <div class="main-body mt-4">
      <div class="row gutters-sm">
        <div class="col-md-4 mb-3">
          <div class="card">
            <div class="card-body">
              <div class="d-flex flex-column align-items-center text-center">
                <div class="container">
                  <img v-if="avatar_preview" :src="avatar_preview" alt="Admin" class="rounded-circle" width="150">
                  <img v-else :src="profile.avatar" alt="Admin" class="rounded-circle" width="150">
                  <label v-if="username === $route.params.slug" for="frstimage"><i class="bi bi-camera fa-download"></i></label>
                  <input v-if="username === $route.params.slug" @change="onFileChange" id="frstimage" ref="avatar" class="avatar-input" type="file">
                </div>
                <div>
                <button @click.prevent="UploadAvatar" v-if="avatar_preview" class="btn btn-primary btn-sm mt-2">Сохранить</button>
                <button @click.prevent="cancelUpdate" v-if="avatar_preview" class="btn btn-danger btn-sm mt-2 ml-2">Отменить</button>
                  </div>
                <div class="mt-3">
                  <h4>{{ profile_username }}</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-8">
          <div class="row">
            <div class="col-md-offset-1 col-md-12">
              <div class="panel">
                <div class="panel-heading">
                  <div class="row">
                    <div class="col-sm-12 col-xs-12">
                      <router-link v-if="username === $route.params.slug" :to="'/create/post'" class="btn btn-sm btn-primary pull-left"><i class="fa fa-plus-circle"></i> Создать пост</router-link>
                    </div>
                  </div>
                </div>
                <div class="panel-body table-responsive">
                  <table class="table">
                    <thead>
                    <tr>
                      <th>View</th>
                      <th>Name</th>
                      <th>Date</th>
                      <th v-if="username === $route.params.slug">Delete</th>
                      <th v-else></th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-if="posts" v-for="post in posts">
                      <td>
                        <ul class="action-list">
                          <li><router-link :to="`/post/${post.slug}`" class="btn btn-success"><i class="fa fa-search"></i></router-link></li>
                        </ul>
                      </td>
                      <td>{{ post.title }}</td>
                      <td>{{ post.created_date.slice(0, 10) }}</td>
                      <td>
                        <button v-if="username === $route.params.slug" @click.prevent="deletePost(post.slug, posts.indexOf(post))" class="btn btn-sm btn-danger ml-2"><i class="fa fa-times"></i></button>
                      </td>
                    </tr>
                    </tbody>
                  </table>
                  <h4 v-if="posts.length === 0" class="text-center">Список постов пуст</h4>
                  <pagination
                      class="mt-2"
                      :previous="previous"
                      :total="total"
                      :current_page="current_page"
                      :next="next"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Pagination from "@/components/Pagination";
export default {
  components: {
    Pagination
  },
  name: "Profile",
  data() {
    return {
      posts: [],
      total: [],
      next: [],
      previous: [],
      current_page: 0,
      avatar: null,
      avatar_preview: null,
      profile: '',
      profile_username: '',
      check: null,
      username: this.$store.state.username
    }
  },
  methods: {
    async UserPosts() {
      let page = this.$route.query.page !== undefined ? `?page=${this.$route.query.page}` : '';
      const response = await axios.get(`http://127.0.0.1:8000/api/user-posts/${this.$route.params.slug}/${page}`)
      let next = response.data.next !== null ? response.data.next.split('/')[6] : null;
      let previous = response.data.previous !== null ? response.data.previous.split('/')[6] : null;
      let current_page = this.$route.query.page
      this.posts = response.data.results;
      this.total = Math.ceil(response.data.count / 6);
      this.next = next
      this.previous = previous
      this.current_page = Number(current_page)
    },
    async deletePost(post_slug, post_index) {
      await axios.delete(`http://127.0.0.1:8000/api/post/detail/${post_slug}`)
      this.posts.splice(post_index, 1)
    },
    async UploadAvatar() {
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
      }
      await axios.patch(`http://127.0.0.1:8000/api/update/avatar/${this.$route.params.slug}/`, {avatar: this.avatar}, config)
      this.avatar_preview = null
      this.check = true
    },
    async getProfile() {
      const response = await axios.get(`http://127.0.0.1:8000/api/update/avatar/${this.$route.params.slug}/`)
      this.profile = response.data
      this.profile_username = this.profile.user.username
      this.check = null
    },
    onFileChange() {
      this.avatar = this.$refs.avatar.files.item(0)
      this.avatar_preview = URL.createObjectURL(this.avatar)
    },
    cancelUpdate() {
      this.avatar_preview = null
    }
  },
  mounted() {
    this.UserPosts()
    this.getProfile()
  },
  watch: {
    'posts.length': {
      immediate: true,
      handler: 'UserPosts'
    },
    '$route.query.page': {
      immediate: true,
      handler: 'UserPosts'
    },
    'check': {
      immediate: true,
      handler: 'getProfile'
    }
  }
}
</script>

<style scoped>

.avatar-input {
  display: none;
  visibility: none;
}

.fa-download {
  font-size: 28px;
}

.container { position: relative; }
.container .fa-download { position: absolute; bottom: 1px; left: 139px; }

.panel{
    font-family: 'Raleway', sans-serif;
    padding: 0;
    border: none;
    box-shadow: 0 0 10px rgba(0,0,0,0.08);
}
.panel .panel-heading{
    background: #535353;
    padding: 15px;
    border-radius: 0;
}
.panel .panel-heading .btn{
    color: #fff;
    background-color: #000;
    font-size: 14px;
    font-weight: 600;
    padding: 7px 15px;
    border: none;
    border-radius: 0;
    transition: all 0.3s ease 0s;
}
.panel .panel-heading .btn:hover{ box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); }
.panel .panel-heading .form-horizontal .form-group{ margin: 0; }
.panel .panel-heading .form-horizontal label{
    color: #fff;
    margin-right: 10px;
}
.panel .panel-heading .form-horizontal .form-control{
    display: inline-block;
    width: 80px;
    border: none;
    border-radius: 0;
}
.panel .panel-heading .form-horizontal .form-control:focus{
    box-shadow: none;
    border: none;
}
.panel .panel-body{
    padding: 0;
    border-radius: 0;
}
.panel .panel-body .table thead tr th{
    color: #fff;
    background: #8D8D8D;
    font-size: 17px;
    font-weight: 700;
    padding: 12px;
    border-bottom: none;
}
.panel .panel-body .table thead tr th:nth-of-type(1){ width: 120px; }
.panel .panel-body .table thead tr th:nth-of-type(3){ width: 50%; }
.panel .panel-body .table tbody tr td{
    color: #555;
    background: #fff;
    font-size: 15px;
    font-weight: 500;
    padding: 13px;
    vertical-align: middle;
    border-color: #e7e7e7;
}
.panel .panel-body .table tbody tr:nth-child(odd) td{ background: #f5f5f5; }
.panel .panel-body .table tbody .action-list{
    padding: 0;
    margin: 0;
    list-style: none;
}
.panel .panel-body .table tbody .action-list li{ display: inline-block; }
.panel .panel-body .table tbody .action-list li a{
    color: #fff;
    font-size: 13px;
    line-height: 28px;
    height: 28px;
    width: 33px;
    padding: 0;
    border-radius: 0;
    transition: all 0.3s ease 0s;
}
.panel .panel-body .table tbody .action-list li a:hover{ box-shadow: 0 0 5px #ddd; }
.panel .panel-footer{
    color: #fff;
    background: #535353;
    font-size: 16px;
    line-height: 33px;
    padding: 25px 15px;
    border-radius: 0;
}
.pagination{ margin: 0; }
.pagination li a{
    color: #fff;
    background-color: rgba(0,0,0,0.3);
    font-size: 15px;
    font-weight: 700;
    margin: 0 2px;
    border: none;
    border-radius: 0;
    transition: all 0.3s ease 0s;
}
.pagination li a:hover,
.pagination li a:focus,
.pagination li.active a{
    color: #fff;
    background-color: #000;
    box-shadow: 0 0 5px rgba(0,0,0,0.4);
}
</style>