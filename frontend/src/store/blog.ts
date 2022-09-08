import { defineStore } from "pinia";
import gql from "graphql-tag";
import { apolloClient } from "../api/client";
import { Post, Tag } from "../api/models";
import PostsByTagAndCategorySlug from "../graphql/posts.gql";

export type PostState = {
  posts: Post[];
  post: Post | null;
  tags: Tag[];
  usedTags: Tag[];
};

export const usePostStore = defineStore("blog", {
  state: () =>
    ({
      posts: [],
      post: null,
      tags: [],
      usedTags: [],
    } as PostState),
  getters: {
    getPosts: (state) => state.posts,
    getPost: (state) => state.post,
    getTags: (state) => state.tags,
    getUsedTags: (state) => state.usedTags,
  },
  actions: {
    async fetchPosts(
      tagSlugParam: string | undefined,
      categorySlugParam: string | undefined
    ) {
      const response = await apolloClient.query({
        query: PostsByTagAndCategorySlug,
        variables: {
          tagSlug: tagSlugParam,
          categorySlug: categorySlugParam,
        },
      });
      this.posts = response.data.posts;
    },
    async fetchPost(postSlug: string | undefined, reload: boolean) {
      if (reload) this.post = null;
      const response = await apolloClient.query({
        query: gql`
          query getPostBySlug($slug: String!) {
            postBySlug(slug: $slug) {
              id
              title
              slug
              text
              image
              isLiked
              likeCount
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
      if (this.post) {
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
        await this.fetchPost(this.post.slug, false);
      }
    },
    async createPostLike() {
      if (this.post) {
        const response = await apolloClient.mutate({
          mutation: gql`
            mutation createPostLike($postLikeInput: PostLikeInput!) {
              createPostLike(postLikeInput: $postLikeInput) {
                postLike {
                  id
                }
              }
            }
          `,
          variables: {
            postLikeInput: {
              post: this.post.id,
            },
          },
        });
        if (response.data.createPostLike.postLike) {
          await this.fetchPost(this.post.slug, false);
        }
      }
    },
    async deletePostLike() {
      if (this.post) {
        await apolloClient.mutate({
          mutation: gql`
            mutation deletePostLike($postLikeInput: PostLikeInput!) {
              deletePostLike(postLikeInput: $postLikeInput) {
                success
              }
            }
          `,
          variables: {
            postLikeInput: {
              post: this.post.id,
            },
          },
        });
        await this.fetchPost(this.post.slug, false);
      }
    },
  },
});
