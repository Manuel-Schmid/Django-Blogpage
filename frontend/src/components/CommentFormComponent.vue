<script lang="ts">
import { ref } from "vue";
import { useStore } from "../store/blog";
import { useRoute } from "vue-router";

export default {
  name: "CommentFormComponent",
  props: {
    postId: String,
  },
  emits: ["toggle-comment-form"],

  setup(props: { postId: any }, ctxt: { emit: (arg0: string) => void }) {
    let title = ref("");
    let text = ref("");

    const route = useRoute();
    const postSlug = route.params.slug as string;

    const saveComment = () => {
      if (!(title.value && text.value)) {
        return;
      }
      const commentInput = {
        title: title.value,
        text: text.value,
        post: props.postId,
        owner: useStore().getUserID,
      };
      const store = useStore();
      store.createComment(commentInput);

      ctxt.emit("toggle-comment-form");
    };

    return { title, text, postSlug, saveComment };
  },
};
</script>

<template>
  <div class="text-left w-full mb-4">
    <input class="border p-2 w-full" v-model="title" placeholder="Title" />
    <textarea
      class="border w-full p-2 h-36 mt-3"
      v-model="text"
      placeholder="Text"
    />
    <button
      @click="saveComment(postSlug)"
      class="py-2 px-8 mt-2 rounded-lg float-right bg-slate-100 hover:bg-slate-200"
    >
      Save
    </button>
  </div>
</template>

<style scoped></style>
