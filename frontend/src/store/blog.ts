import { defineStore } from "pinia";
import gql from "graphql-tag";
import { apolloClient } from "../api/client";

export const useStore = defineStore("blog", {
  state: () => ({
    posts: [],
    post: null,
    tags: [],
    usedTags: [],
    userID: 3, // todo
  }),
  getters: {
    getPosts: (state) => state.posts,
    getPost: (state) => state.post,
    getTags: (state) => state.tags,
    getUsedTags: (state) => state.usedTags,
    getUserID: (state) => state.userID,
  },
  actions: {
    async fetchPosts(
      tagSlugParam: string | undefined,
      categorySlugParam: string | undefined
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
              comments {
                id
              }
              postLikes {
                id
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
    async fetchPost(postSlug: string | undefined) {
      this.post = null;
      const response = await apolloClient.query({
        query: gql`
          query getPostBySlug($slug: String!) {
            postBySlug(slug: $slug) {
              id
              title
              slug
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
              postLikes {
                id
                user {
                  id
                }
              }
              comments {
                title
                text
                owner {
                  firstName
                  lastName
                }
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
    async fetchTags() {
      if (this.tags.length === 0) {
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
      }
    },
    async fetchUsedTags() {
      if (this.usedTags.length === 0) {
        const response = await apolloClient.query({
          query: gql`
            {
              usedTags {
                name
                slug
              }
            }
          `,
        });
        this.usedTags = response.data.usedTags;
      }
    },
    async createComment(commentInput: any) {
      await apolloClient.mutate({
        mutation: gql`
          mutation CreateComment($commentInput: CommentInput!) {
            createComment(commentInput: $commentInput) {
              comment {
                title
                text
                owner {
                  firstName
                  lastName
                }
              }
              success
            }
          }
        `,
        variables: {
          commentInput: commentInput,
        },
      });
      this.fetchPost(this.post.slug);
    },

    fetchPostLike(postId: Number, userId: Number) {
      const response = apolloClient.query({
        query: gql`
          query postLikeByUserAndPost($postId: ID, $userId: ID) {
            postLike(postId: $postId, userId: $userId) {
              id
            }
          }
        `,
        variables: {
          postId: postId,
          userId: userId,
        },
      });
      return response;
    },

    async createPostLike(postLikeInput: any) {
      await apolloClient.mutate({
        mutation: gql`
          mutation creatPostLike($postLikeInput: PostLikeInput!) {
            createPostLike(postLikeInput: $postLikeInput) {
              postLike {
                id
              }
            }
          }
        `,
        variables: {
          postLikeInput: postLikeInput,
        },
      });
      this.fetchPost(this.post.slug);
    },

    async deletePostLike(postLikeInput: any) {
      await apolloClient.mutate({
        mutation: gql`
          mutation postLikeByUserAndPost($postLikeInput: PostLikeInput!) {
            deletePostLike(postLikeInput: $postLikeInput) {
              success
            }
          }
        `,
        variables: {
          postLikeInput: postLikeInput,
        },
      });
      this.fetchPost(this.post.slug);
    },
  },
});
