<template>
  <PostsOverviewComponent
    :posts-data="store.getPosts"
    :tags-data="store.getUsedTags"
  />
</template>

<script lang="ts">
import PostsOverviewComponent from "../components/PostsOverviewComponent.vue";
import { useRoute } from "vue-router";
import { useStore as usePostsStore } from "../../../store/blog";

export default {
  name: "PostOverviewContainer",
  components: {
    PostsOverviewComponent,
  },

  setup() {
    const route = useRoute();
    const store = usePostsStore();
    store.fetchPosts(route.query.tag as string, route.params.slug as string);
    store.fetchUsedTags();

    return { store };
  },
};
</script>
