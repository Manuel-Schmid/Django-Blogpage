import { createApp, provide, h } from "vue";
import { createPinia } from "pinia";
import piniaPersist from "pinia-plugin-persist";
import App from "./App.vue";
import router from "./router/router";
import { DefaultApolloClient } from "@vue/apollo-composable";
import { apolloClient } from "./api/client";
import "./global.css";

const app = createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient);
  },

  render: () => h(App),
});
const pinia = createPinia();
pinia.use(piniaPersist);

app.use(router);
app.use(pinia);

app.mount("#app");
