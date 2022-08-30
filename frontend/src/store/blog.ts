import { defineStore } from "pinia";
import gql from "graphql-tag";
import { apolloClient } from "../api/client";

export const useStore = defineStore("blog", {
  state: () => ({
    posts: [],
    post: {},
    tags: [],
  }),
  getters: {
    getPosts: (state) => state.posts,
    getPost: (state) => state.post,
    getTags: (state) => state.tags
  },
  actions: {
    async fetchPosts(
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
    async fetchPost(
      postSlug: string,
    ) {
      const response = await apolloClient.query({
        query: gql`
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
        variables: {
          slug: postSlug,
        },
      });
      this.post = response.data.postBySlug;
    },
    async fetchTags () {
      const response = await apolloClient.query({
        query: gql`
            {
                tags {
                    name
                    slug
                }
            }
        `,
      });
      this.tags = response.data.tags;
    },
  },
});