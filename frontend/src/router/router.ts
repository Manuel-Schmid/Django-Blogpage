import { createRouter, createWebHistory } from "vue-router";
import PostsOverviewContainer from "../container/PostsOverviewContainer.vue";
import PostDetailContainer from "../container/PostDetailContainer.vue";
import ProfileContainer from "../container/ProfileContainer.vue";
import LoginComponent from "../components/LoginComponent.vue";
import PasswordResetFormComponent from "../components/PasswordResetFormComponent.vue";
import ResetEmailFormComponent from "../components/ResetEmailFormComponent.vue";
import RegistrationComponent from "../components/RegistrationComponent.vue";
import ActivationContainer from "../container/ActivationContainer.vue";

const routes: any = [
  {
    path: "/login/:verified?",
    name: "login",
    component: LoginComponent,
  },
  {
    path: "/activate/:token",
    name: "activation",
    component: ActivationContainer,
  },
  {
    path: "/signup",
    name: "registration",
    component: RegistrationComponent,
  },
  {
    path: "/password-reset/:token",
    name: "passwordReset",
    component: PasswordResetFormComponent,
  },
  {
    path: "/reset-email",
    name: "resetEmailForm",
    component: ResetEmailFormComponent,
  },
  {
    path: "/profile",
    name: "profile",
    component: ProfileContainer,
  },
  {
    path: "/posts/:category?:tags?:page?",
    name: "posts",
    component: PostsOverviewContainer,
  },
  {
    path: "/posts/:slug",
    name: "postDetail",
    component: PostDetailContainer,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
