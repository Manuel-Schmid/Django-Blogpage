<template>
  <PostsOverviewComponent
    :posts-data="store.posts"
    :num-post-pages="store.numPostPages"
    :active-page="activePage"
    :tags-data="store.usedTags"
  />
</template>

<script lang="ts">
import PostsOverviewComponent from "../components/PostsOverviewComponent.vue";
import { useRoute } from "vue-router";
import { usePostStore } from "../store/blog";

export default {
  name: "PostsOverviewContainer",
  components: {
    PostsOverviewComponent,
  },

  setup() {
    const route = useRoute();
    const store = usePostStore();
    const activePage: number = route.query.page ? +route.query.page : 1;

    store.fetchPosts(
      route.query.tag as string,
      route.params.slug as string,
      activePage
    );
    store.fetchUsedTags();

    return { store, activePage };
  },
};
</script>
