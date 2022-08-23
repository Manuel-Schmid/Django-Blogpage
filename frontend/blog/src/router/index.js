import { createRouter, createWebHistory } from 'vue-router'
import PostsOverviewContainer from '@/container/PostsOverviewContainer.vue'
import PostDetailContainer from '@/container/PostDetailContainer'

const routes = [
  {
    path: '/posts',
    name: 'posts',
    component: PostsOverviewContainer
  },
  {
    path: '/posts/:slug',
    name: 'postDetail',
    component: PostDetailContainer,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
