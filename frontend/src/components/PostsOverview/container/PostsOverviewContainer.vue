<template>
  <PostsOverviewComponent
    :posts-data="store.getPosts"
    :num-post-pages="store.getNumPostPages"
    :tags-data="store.getUsedTags"
  />
</template>

<script lang="ts">
import PostsOverviewComponent from "../components/PostsOverviewComponent.vue";
import { useRoute } from "vue-router";
import { usePostStore } from "../../../store/blog";

export default {
  name: "PostOverviewContainer",
  components: {
    PostsOverviewComponent,
  },

  setup() {
    const route = useRoute();
    const store = usePostStore();
    const page: number = route.params.page ? +route.params.page : 1;
    store.fetchPosts(
      route.query.tag as string,
      route.params.slug as string,
      page
    );
    store.fetchUsedTags();

    return { store };
  },
};
</script>
