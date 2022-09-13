<template>
  <PostsOverviewComponent
    :posts-data="store.getPosts"
    :num-post-pages="store.getNumPostPages"
    :active-page="activePage"
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
