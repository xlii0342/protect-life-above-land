import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import PetOwner from '../views/PetOwner.vue'
import Learn from '../views/Learn.vue'
import Gamification from '@/components/Gamification.vue'

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
    path: '/learn',
    name: 'Learn',
    component: Learn
  },
  {
    path: '/student-educator',
    name: 'StudentEducator',
    component: () => import('../views/Learn.vue')
  },
  {
    path: '/learn.vue',
    name: 'Beginner',
    component: () => import('../views/Learn.vue')
  },
  // Map component is now available
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
    path: '/volunteer',
    name: 'Volunteer',
    component: () => import('../views/Volunteer.vue')
  },
  { path: '/game', name: 'game', component: Gamification },
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router 