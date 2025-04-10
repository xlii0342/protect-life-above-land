import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import PetOwner from '../views/PetOwner.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/pet-owner',
    name: 'PetOwner',
    component: PetOwner
  },
 
  {
    path: '/map',
    name: 'Map',
    component: () => import('../views/Map.vue')
  },
  {
    path: '/learn',
    name: 'Learn',
    component: () => import('../views/Learn.vue')
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
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router 