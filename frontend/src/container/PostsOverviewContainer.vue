<template>
  <PostsOverviewComponent
    :posts-data="store.paginatedPosts"
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
    const tags = route.query.tags as string;
    const category = route.query.category as string;

    store.fetchPosts(tags, category, activePage);
    store.fetchUsedTags(category);

    return { store, activePage };
  },
};
</script>
