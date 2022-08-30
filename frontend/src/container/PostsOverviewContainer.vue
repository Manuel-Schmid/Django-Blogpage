<template>
  <PostsOverviewComponent :posts-data="store.getPosts" :tags-data="tagsData"/>
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
    store.setPosts(tagSlug, categorySlug)
    // const postsData = store.getPosts
    // console.log(postsData);

    let tags = useQuery(gql`
          {
            tags {
              name
              slug
            }
          }
        `);
    let tagsData = tags.result
    return { store, tagsData };
  },
};
</script>
