<template>
  <h1>OVERVIEW</h1>
  <PostsOverviewComponent :posts-data="result" />
</template>

<script lang="ts">
import gql from "graphql-tag";
import { useQuery } from "@vue/apollo-composable";
import PostsOverviewComponent from "../components/PostsOverviewComponent.vue";

export default {
  name: "PostOverviewContainer",
  components: {
    PostsOverviewComponent,
  },

  setup() {
    let { result } = useQuery(gql`
      {
        posts {
          id
          slug
          title
          dateCreated
          category {
            name
          }
          owner {
            firstName
            lastName
          }
        }
      }
    `);
    return { result };
  },
};
</script>
