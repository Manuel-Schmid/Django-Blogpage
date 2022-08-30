<template>
  <PostsOverviewComponent :posts-data="store.getPosts" :tags-data="store.getTags"/>
</template>

<script lang="ts">
import gql from "graphql-tag";
import { useQuery } from "@vue/apollo-composable";
import PostsOverviewComponent from "../components/PostsOverviewComponent.vue";
import { useRoute } from "vue-router";
import { useStore as usePostsStore } from "../store/blog";


export default {
  name: "PostOverviewContainer",
  components: {
    PostsOverviewComponent,
  },

  setup() {
    const route = useRoute();
    const tagSlug = route.query.tag ? route.query.tag.toString() : null;
    const categorySlug = route.params.slug ? route.params.slug.toString() : null;

    const store = usePostsStore();
    store.fetchPosts(tagSlug, categorySlug)
    if (store.getTags.length == 0) {
      store.fetchTags()
    }

    return { store };
  },
};
</script>