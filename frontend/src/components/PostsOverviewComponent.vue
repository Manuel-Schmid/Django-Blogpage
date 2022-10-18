<script lang="ts">
import { useRoute } from "vue-router";
import PostTileComponent from "./posts-overview/PostTileComponent.vue";
import TagListComponent from "./posts-overview/TagListComponent.vue";
import PaginationComponent from "./posts-overview/PaginationComponent.vue";

export default {
  name: "PostsOverviewComponent",
  components: {
    PostTileComponent,
    TagListComponent,
    PaginationComponent,
  },

  props: ["postsData", "tagsData", "activePage"],

  setup() {
    const route = useRoute();
    return { route };
  },
};
</script>

<template>
  <div class="post-overview-container p-12 dark:text-white">
    <div class="content-container m-auto w-full">
      <TagListComponent :tags-data="tagsData"></TagListComponent>
      <p
        class="text-3xl tracking-wide leading-5 text-black font-bold mb-8 mt-4 mt-9 dark:text-white"
      >
        Posts:
      </p>
      <div v-if="postsData">
        <PostTileComponent
          v-for="post in postsData.posts"
          :key="post.id"
          :post="post"
        >
        </PostTileComponent>
        <PaginationComponent
          v-if="postsData.numPostPages > 1"
          :num-post-pages="postsData.numPostPages"
          :active-page="activePage"
        ></PaginationComponent>
      </div>
    </div>
  </div>
</template>

<style scoped>
.post-overview-container {
  margin-top: 9vh;
}
.content-container {
  max-width: 970px;
}
</style>
