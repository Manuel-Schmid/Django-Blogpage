<script lang="ts">
import { ref } from "vue";

export default {
  name: "PasswordChangeFormComponent",
  emits: ["toggle-password-change-form"],

  setup(props: any, ctxt: { emit: (arg0: string) => void }) {
    let newPassword1 = ref("");
    let newPassword2 = ref("");

    const changePassword = () => {
      // usePostStore().createComment(commentInput);

      ctxt.emit("toggle-password-change-form");
    };

    return { newPassword1, newPassword2, changePassword };
  },
};
</script>

<template>
  <div class="text-left w-full mb-4">
    <input
      class="border p-2 w-full dark:border-slate-600 dark:bg-slate-600"
      v-model="newPassword1"
      type="password"
      placeholder="••••••••"
    />
    <input
      class="border p-2 w-full dark:border-slate-600 dark:bg-slate-600"
      v-model="newPassword2"
      type="password"
      placeholder="••••••••"
    />
    <button
      @click="changePassword"
      class="py-2 px-8 mt-2 rounded-lg float-right bg-slate-100 hover:bg-slate-200 dark:bg-slate-600 hover:dark:bg-slate-700"
    >
      Save
    </button>
  </div>
</template>

<style scoped></style>
