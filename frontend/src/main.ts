import { createApp, provide, h } from "vue";
import { createPinia } from "pinia";
import piniaPersist from "pinia-plugin-persist";
import App from "./App.vue";
import router from "./router/router";
import { DefaultApolloClient } from "@vue/apollo-composable";
import { apolloClient } from "./api/client";
import "./global.css";
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faPlus,
  faMinus,
  faThumbsUp,
  faComment,
  faUser,
  faArrowRight,
  faArrowLeft,
  faTrash,
  faXmark,
  faCheck,
} from "@fortawesome/free-solid-svg-icons";
import {
  faCircleXmark,
  faPenToSquare,
} from "@fortawesome/free-regular-svg-icons";

library.add(
  faPlus,
  faMinus,
  faThumbsUp,
  faComment,
  faUser,
  faArrowRight,
  faArrowLeft,
  faTrash,
  faXmark,
  faCheck,
  faCircleXmark,
  faPenToSquare
);

const app = createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient);
  },

  render: () => h(App),
}).component("font-awesome-icon", FontAwesomeIcon);
const pinia = createPinia();
pinia.use(piniaPersist);

app.use(router);
app.use(pinia);

app.mount("#app");
