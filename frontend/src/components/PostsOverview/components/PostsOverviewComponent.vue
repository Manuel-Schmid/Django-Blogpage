<script lang="ts">
import { useRoute } from "vue-router";
import { ref } from "vue";
import PostTileComponent from "../components/PostTileComponent.vue";
import TagListComponent from "../components/TagListComponent.vue";
import PaginationComponent from "../components/PaginationComponent.vue";

export default {
  name: "PostOverviewComponent",
  components: {
    PostTileComponent,
    TagListComponent,
    PaginationComponent,
  },

  props: ["postsData", "tagsData", "numPostPages"],

  setup() {
    let hover = ref("none");
    const route = useRoute();
    return { route, hover };
  },
};
</script>

<template>
  <div class="post-overview-container p-12">
    <div class="content-container w-full">
      <TagListComponent :tags="tagsData"></TagListComponent>
      <p
        class="text-3xl tracking-wide leading-5 text-black font-bold mb-8 mt-4 mt-9"
      >
        Posts:
      </p>
      <div v-if="postsData">
        <PostTileComponent
          v-for="post in postsData"
          :key="post.id"
          :post="post"
        >
        </PostTileComponent>
        <PaginationComponent
          :num-post-pages="numPostPages"
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
