<script lang="ts">
import CommentFormComponent from "./CommentFormComponent.vue";
import CommentComponent from "./CommentComponent.vue";
import { ref } from "vue";
import { useAuthStore } from "../store/auth";

export default {
  name: "CommentSectionComponent",
  props: {
    postId: String,
    comments: {},
  },
  components: {
    CommentFormComponent,
    CommentComponent,
  },

  setup() {
    let commentFormActive = ref(false);
    let authStore = useAuthStore();
    return { commentFormActive, authStore };
  },
};
</script>

<template>
  <p class="font-bold text-xl mb-5">
    <span>Comments:</span>
  </p>
  <button
    v-if="authStore.user"
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
    <CommentComponent
      v-for="comment in comments"
      :comment="comment"
      :is-own-comment="comment.owner.id === authStore.user?.id"
    ></CommentComponent>
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
