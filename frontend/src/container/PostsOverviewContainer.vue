<template>
  <PostsOverviewComponent :posts-data="postsData" :tags-data="tagsData"/>
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
    const tag = route.query.tag;
    const routeName = route.name;

    let { result } =
      (routeName == 'categoryPosts' && tag) ?
        useQuery(gql`
          query postsByTagAndCategorySlug($tagSlug: String, $categorySlug: String) {
            posts(tagSlug: $tagSlug, categorySlug: $categorySlug) {
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
            tagSlug: tag,
            categorySlug: route.params.slug,
          }
      ) : (routeName == 'categoryPosts') ?
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
          categorySlug: route.params.slug,
        }
      ) : (tag) ?
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
            tagSlug: tag,
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
    let postsData = result

    let tags = useQuery(gql`
          {
            tags {
              name
              slug
            }
          }
        `);
    let tagsData = tags.result
    return { postsData, tagsData };
  },
};
</script>
