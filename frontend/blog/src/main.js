import App from './App.vue';
import { createApp, provide, h } from 'vue';
import { DefaultApolloClient } from '@vue/apollo-composable';
import apolloClient from "@/ApolloClient";
import router from './router'

const app = createApp({
    setup () {
        provide(DefaultApolloClient, apolloClient);
    },

    render: () => h(App),
}).use(router);

app.mount('#app');
