<template>
  <PostDetailComponent :post-data="result" />
</template>

<script lang="ts">
import { useRoute } from "vue-router/dist/vue-router";
import { useQuery } from "@vue/apollo-composable";
import gql from "graphql-tag";
import PostDetailComponent from "../components/PostDetailComponent.vue";

export default {
  name: "PostDetailView",
  components: {
    PostDetailComponent,
  },

  setup() {
    const route = useRoute();
    const slug = route.params.slug;

    let { result } = useQuery(
      gql`
        query getPostBySlug($slug: String!) {
          postBySlug(slug: $slug) {
            title
            text
            image
            dateCreated
            category {
              name
              slug
            }
            owner {
              firstName
              lastName
            }
            tags {
              name
              slug
            }
          }
        }
      `,
      {
        slug: slug,
      }
    );
    return { result };
  },
};
</script>
