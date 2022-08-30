import { defineStore } from "pinia";
import gql from "graphql-tag";
import { apolloClient } from "../api/client";

export const useStore = defineStore("blog", {
  state: () => ({
    posts: [],
  }),
  getters: {
    getPosts: (state) => state.posts,
  },
  actions: {
    async setPosts(
      tagSlugParam: string | null = null,
      categorySlugParam: string | null = null
    ) {
      const response = await apolloClient.query({
        query: gql`
            query postsByTagAndCategorySlug(
                $tagSlug: String
                $categorySlug: String
            ) {
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
        variables: {
          tagSlug: tagSlugParam,
          categorySlug: categorySlugParam,
        },
      });
      this.posts = response.data.posts;
    },
  },
});