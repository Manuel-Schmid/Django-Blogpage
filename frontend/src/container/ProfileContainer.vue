<template>
  <ProfileComponent :user-data="store.getUser" />
</template>

<script lang="ts">
import ProfileComponent from "../components/ProfileComponent.vue";
import { useRoute } from "vue-router";
import { usePostStore as usePostsStore } from "../store/blog";

export default {
  name: "profileContainer",
  components: { ProfileComponent },

  setup() {
    const route = useRoute();
    const store = usePostsStore();
    store.fetchUser();

    return { store };
  },
};
</script>

<style scoped></style>
