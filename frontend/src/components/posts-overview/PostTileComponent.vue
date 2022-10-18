<script lang="ts">
import {
  formatFullname,
  formatDateShort,
  getImageURL,
} from "../../helper/helper";

export default {
  name: "PostTileComponent",
  props: ["post"],

  setup() {
    return { formatFullname, formatDateShort, getImageURL };
  },
};
</script>

<template>
  <router-link
    :to="{ name: 'postDetail', params: { slug: post.slug } }"
    :class="[
      'post rounded-2xl shadow-lg mt-2 mb-2 pt-5 pr-2 pb-1 pl-2 float-left inline-block text-black no-underline dark:bg-[#262b39] hover:shadow-2xl',
    ]"
  >
    <div
      class="post-title tracking-wide tracking-wide pt-0 pr-4 pb-0 pl-4 leading-5 text-black font-bold dark:text-white"
    >
      <p class="mb-4">{{ post.title }}</p>
    </div>
    <div class="post-creation-info">
      <p>
        {{ formatFullname(post.owner.firstName, post.owner.lastName) }} -
        {{ formatDateShort(post.dateCreated) }}
      </p>
    </div>
    <div v-if="post.image" class="pt-3 pr-2 pb-1 pl-2 h-44 flex">
      <img
        class="w-full max-h-full"
        :src="getImageURL(post.image)"
        alt="Post Image"
      />
    </div>
    <div class="w-1/2 float-left text-left">
      <div class="m-2 icons-container">
        <span class="ml-2 w-1/2">
          <font-awesome-icon icon="fa-thumbs-up"></font-awesome-icon>
          {{ post.likeCount }}
        </span>
        <span class="ml-5 w-1/2">
          <font-awesome-icon icon="fa-comment"></font-awesome-icon>
          {{ post.commentCount }}
        </span>
      </div>
    </div>
    <div class="text-right float-right w-1/2">
      <p class="m-2">{{ post.category.name }}</p>
    </div>
  </router-link>
</template>

<style scoped>
.post {
  width: calc(40% - 20px);
  margin-right: 5%;
  margin-left: 5%;
  transition: box-shadow 200ms;
}
.post-title {
  font-size: 1.4em;
}
.icons-container {
  width: calc(100% - 1rem);
}
</style>
