import { createRouter, createWebHistory } from "vue-router";
import { trackRouter } from "vue-gtag-next";
// import Home from '../views/Home/Home.vue'
import Landing from "@/views/Landing/Landing.vue";

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: Landing
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

trackRouter(router);

export default router
