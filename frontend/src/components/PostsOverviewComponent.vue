<script lang="ts">
import router from "../router";
import { useRoute } from "vue-router";

export default {
  name: "PostOverviewComponent",
  props: ["postsData", "tagsData"],

  setup() {
    const route = useRoute();

    const formatDate = (date: string) => {
      let options: any = { year: "numeric", month: "2-digit", day: "2-digit" };
      return new Date(date).toLocaleDateString("en-GB", options);
    };

    const formatFullname = (firstName: string, lastName: string) => {
      return `${firstName} ${lastName}`;
    };
    return { formatDate, formatFullname, route };
  },
};
</script>

<template>
  <div class="post-overview-container">
    <div class="content-container">
      <div class="tags-container" v-if="tagsData">
        <p style="margin-bottom: 0"><b>Tags:&nbsp;</b></p>
        <div class="tags">
          <router-link
            v-for="tag in tagsData.tags"
            :key="tag.slug"
            :class="['post-tag', (tag.slug === route.query.tag) ? 'active-tag' : '']"
            :to="{ name: route.name, query: { tag: tag.slug } }"
          >
            <p class="tag-name">{{ tag.name }}</p>
          </router-link>
        </div>
      </div>
      <p class="title">Posts:</p>
      <div v-if="postsData" class="posts-container">
        <router-link
          v-for="post in postsData.posts"
          :key="post.id"
          :to="{ name: 'postDetail', params: { slug: post.slug } }"
          class="post"
        >
          <div class="post-title">
            <p>{{ post.title }}</p>
          </div>
          <div class="post-creation-info">
            <p>
              {{ formatFullname(post.owner.firstName, post.owner.lastName) }} -
              {{ formatDate(post.dateCreated) }}
            </p>
          </div>
          <div class="post-category">
            <p>{{ post.category.name }}</p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
