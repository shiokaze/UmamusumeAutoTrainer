import { createRouter, createWebHistory } from 'vue-router'
import AutoController from '../views/AutoController.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'controller',
      component: AutoController
    }
  ]
})

export default router
