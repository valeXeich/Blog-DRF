
import {createRouter, createWebHistory} from "vue-router";
import Index from "@/pages/Index";
import PostDetail from "@/pages/PostDetail";
import Tags from "@/pages/Tags";
import Search from "@/pages/Search";
import SignUp from "@/pages/SignUp";
import LogIn from "@/pages/LogIn";
import Profile from "@/pages/Profile";
import CreatePost from "@/pages/CreatePost";



const routes = [
    {
        path: '/',
        component: Index
    },
    {
        path: '/sign-up',
        component: SignUp
    },
    {
        path: '/log-in',
        component: LogIn
    },
    {
        path: '/profile/:slug',
        component: Profile
    },
    {
        path: '/create/post',
        component: CreatePost
    },
    {
        path: '/search',
        component: Search
    },
    {
        path: '/post/:slug',
        component: PostDetail
    },
    {
        path: '/tags/:slug',
        component: Tags
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;