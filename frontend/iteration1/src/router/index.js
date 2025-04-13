import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import PetOwner from '../views/PetOwner.vue'
import Learn from '../views/Learn.vue'
import VideoGuide from '../views/VideoGuide.vue'

const routes = [
  {
    path: '/',
    name: 'VideoGuide',
    component: VideoGuide
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/pet-owner',
    name: 'PetOwner',
    component: PetOwner
  },
  {
    path: '/learn',
    name: 'Learn',
    component: Learn
  },
  // 暂时注释掉缺失的模块
  /*
  {
    path: '/map',
    name: 'Map',
    component: () => import('../views/Map.vue')
  },
  {
    path: '/report',
    name: 'Report',
    component: () => import('../views/Report.vue')
  },
  {
    path: '/support',
    name: 'Support',
    component: () => import('../views/Support.vue')
  }
  */
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router 