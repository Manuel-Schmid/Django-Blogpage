<template>
  <PostsOverviewComponent :posts-data="result"/>
</template>

<script lang="ts">
import gql from "graphql-tag";
import { useQuery } from "@vue/apollo-composable";
import PostsOverviewComponent from "../components/PostsOverviewComponent.vue";
import { useRoute } from "vue-router";


export default {
  name: "PostOverviewContainer",
  components: {
    PostsOverviewComponent,
  },

  setup() {
    const route = useRoute();
    const slug = route.params.slug;

    let { result } = slug ?
      useQuery(gql`
        query postsByCategorySlug($categorySlug: String) {
          posts(categorySlug: $categorySlug) {
            slug
            title
            dateCreated
            category {
              name
              slug
            }
            owner {
              firstName
              lastName
            }
          }
        }
      `,
        {
          categorySlug: slug,
        }
      ) :
      useQuery(gql`
        {
          posts {
            slug
            title
            dateCreated
            category {
              name
              slug
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
