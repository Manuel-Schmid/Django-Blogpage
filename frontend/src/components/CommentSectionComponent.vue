<script lang="ts">
import { formatFullname } from "../helper/helper";
import CommentFormComponent from "./CommentFormComponent.vue";
import { ref } from "vue";

export default {
  name: "CommentSectionComponent",
  props: {
    postId: String,
    comments: {},
  },
  components: {
    CommentFormComponent,
  },

  setup() {
    let commentFormActive = ref(false);
    return { formatFullname, commentFormActive };
  },
};
</script>

<template>
  <p class="font-bold text-xl mb-5">
    <span>Comments</span>
  </p>
  <button
    @click="commentFormActive = !commentFormActive"
    class="py-2 px-4 border-b border-black bg-gray-50 hover:bg-gray-100 dark:bg-slate-700 hover:dark:bg-slate-600 rounded-3xl"
  >
    <font-awesome-icon
      icon="fa-solid fa-plus"
      :class="['mr-2', commentFormActive ? 'icon-diagonal' : 'icon-vertical']"
    />
    Add a comment
  </button>
  <div class="w-3/4 m-auto my-4 flex">
    <CommentFormComponent
      v-if="commentFormActive"
      :post-id="postId"
      @toggle-comment-form="commentFormActive = !commentFormActive"
    ></CommentFormComponent>
  </div>
  <div class="mt-3">
    <div
      v-for="comment in comments"
      class="bg-gray-100 dark:bg-slate-700 rounded-xl p-3 my-3 text-left w-3/4 m-auto"
    >
      <p class="font-bold">{{ comment.title }}</p>
      <p>{{ comment.text }}</p>
      <p class="text-right px-3 pt-2">
        {{ formatFullname(comment.owner.firstName, comment.owner.lastName) }}
      </p>
    </div>
  </div>
</template>

<style scoped>
.icon-vertical {
  rotate: 0deg;
  transition: 300ms;
}
.icon-diagonal {
  rotate: 135deg;
  transition: 300ms;
}
</style>
