import { defineStore } from "pinia";
import { apolloClient } from "../api/client";
import { PaginationPosts, Post, Tag } from "../api/models";
import Posts from "../graphql/getPosts.gql";
import PostBySlug from "../graphql/getPost.gql";
import Tags from "../graphql/getTags.gql";
import UsedTags from "../graphql/getUsedTags.gql";
import CreateComment from "../graphql/createComment.gql";
import DeleteComment from "../graphql/deleteComment.gql";
import CreatePostLike from "../graphql/createPostLike.gql";
import DeletePostLike from "../graphql/deletePostLike.gql";

export type PostState = {
  paginatedPosts: PaginationPosts | null;
  post: Post | null;
  tags: Tag[];
  usedTags: Tag[];
};

export const usePostStore = defineStore("blog", {
  state: () =>
    ({
      paginatedPosts: null,
      post: null,
      tags: [],
      usedTags: [],
    } as PostState),
  actions: {
    async fetchPosts(
      tagSlugsParam: string | undefined,
      categorySlugParam: string | undefined,
      activePage: number
    ) {
      this.paginatedPosts = null;
      const response = await apolloClient.query({
        query: Posts,
        variables: {
          tagSlugs: tagSlugsParam,
          categorySlug: categorySlugParam,
          activePage: activePage,
        },
      });
      this.paginatedPosts = response.data.paginatedPosts;
    },
    async fetchPost(postSlug: string | undefined, reload: boolean) {
      if (reload) this.post = null;
      const response = await apolloClient.query({
        query: PostBySlug,
        variables: {
          slug: postSlug,
        },
      });
      this.post = response.data.postBySlug;
    },
    async fetchTags() {
      if (this.tags.length === 0) {
        const response = await apolloClient.query({
          query: Tags,
        });
        this.tags = response.data.tags;
      }
    },
    async fetchUsedTags(category: string | undefined) {
      if (this.usedTags.length === 0 || category) {
        const response = await apolloClient.query({
          query: UsedTags,
          variables: {
            categorySlug: category,
          },
        });
        this.usedTags = response.data.usedTags;
      }
    },
    async createComment(commentInput: any) {
      if (this.post) {
        await apolloClient.mutate({
          mutation: CreateComment,
          variables: {
            commentInput: commentInput,
          },
        });
        await this.fetchPost(this.post.slug, false);
      }
    },
    async deleteComment(commentId: number) {
      await apolloClient.mutate({
        mutation: DeleteComment,
        variables: {
          commentId: commentId,
        },
      });
      await this.fetchPost(this.post?.slug, false);
    },
    async createPostLike() {
      if (this.post) {
        const response = await apolloClient.mutate({
          mutation: CreatePostLike,
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
          mutation: DeletePostLike,
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
