<template>
  <PostDetailComponent v-if="store.post" :post-data="store.post" />
</template>

<script lang="ts">
import { useRoute } from "vue-router/dist/vue-router";
import PostDetailComponent from "../components/PostDetailComponent.vue";
import { usePostStore } from "../store/blog";

export default {
  name: "PostDetailView",
  components: {
    PostDetailComponent,
  },

  setup() {
    const route = useRoute();
    const store = usePostStore();
    store.fetchPost(route.params.slug as string, true);

    return { store };
  },
};
</script>
