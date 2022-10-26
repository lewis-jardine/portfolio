import { createRouter, createWebHistory } from "vue-router";

import WelcomeView from "../views/WelcomeView.vue";
import ObjectDetectorView from "../views/ObjectDetectorView.vue";
import OtherProjectsView from "../views/OtherProjectsView.vue";
import LoginView from "../views/LoginView.vue";

const routes = [
  {
    path: "/",
    name: "welcome",
    component: WelcomeView,
  },
  {
    path: "/od",
    name: "od",
    component: ObjectDetectorView,
  },
  {
    path: "/projects",
    name: "projects",
    component: OtherProjectsView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
