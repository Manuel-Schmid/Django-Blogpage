<script>
import { ref } from "vue";
import { useStore } from "../store/blog";

export default {
  name: "CommentFormComponent",
  props: {
    postSlug: String,
  },

  setup(props) {
    let title = ref("");
    let text = ref("");
    const userID = useStore().getUserID;
    const postSlug = props.postSlug;

    const saveComment = () => {
      console.log(title.value);
      console.log(text.value);
      console.log(userID);
      console.log(postSlug);
    };

    return { title, text, saveComment };
  },
};
</script>

<template>
  <div class="text-left w-2/5">
    <p class="text-l pb-0.5">Title:</p>
    <input class="border p-2 w-full" v-model="title" placeholder="Your title" />
    <p class="mt-2 text-l pb-0.5">Text:</p>
    <textarea
      class="border w-full p-2"
      v-model="text"
      placeholder="Your text"
    />
    <button
      @click="saveComment"
      class="py-2 px-8 mt-2 border-2 float-right bg-gray-100 hover:bg-gray-200"
    >
      Save
    </button>
  </div>
</template>

<style scoped></style>
