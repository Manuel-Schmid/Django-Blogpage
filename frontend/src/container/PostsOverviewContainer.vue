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
    const routeName = route.name;
    const slug = route.params.slug;

    let { result } = (routeName == 'categoryPosts') ?
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
      ) : (routeName == 'tagPosts') ?
        useQuery(gql`
          query postsByTagSlug($tagSlug: String) {
            posts(tagSlug: $tagSlug) {
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
            tagSlug: slug,
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
