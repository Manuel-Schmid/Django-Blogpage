import { createRouter, createWebHistory } from 'vue-router'
import PostsOverviewView from '@/views/PostsOverviewView.vue'
import PostDetailView from '@/views/PostDetailView'

const routes = [
  {
    path: '/posts',
    name: 'posts',
    component: PostsOverviewView
  },
  {
    path: '/posts/:slug',
    name: 'postDetail',
    component: PostDetailView,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
