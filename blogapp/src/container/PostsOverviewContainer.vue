<template>
  <h1>OVERVIEW</h1>
  <PostsOverviewComponent :posts-data="result" />
</template>

<script lang="ts">
import gql from "graphql-tag";
import PostsOverviewComponent from "../components/PostsOverviewComponent.vue";
import { useQuery } from "@vue/apollo-composable";

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
