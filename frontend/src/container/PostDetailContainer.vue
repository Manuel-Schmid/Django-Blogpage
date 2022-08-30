<template>
  <PostDetailComponent :post-data="store.getPost" />
</template>

<script lang="ts">
import { useRoute } from "vue-router/dist/vue-router";
import PostDetailComponent from "../components/PostDetailComponent.vue";
import { useStore as usePostsStore } from "../store/blog";

export default {
  name: "PostDetailView",
  components: {
    PostDetailComponent,
  },

  setup() {
    const route = useRoute();
    const store = usePostsStore();
    store.fetchPost(route.params.slug as string);

    return { store };
  },
};
</script>
