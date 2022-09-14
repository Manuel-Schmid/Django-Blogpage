<template>
  <ProfileComponent :user-data="store.user" />
</template>

<script lang="ts">
import ProfileComponent from "../components/ProfileComponent.vue";
import { useAuthStore } from "../store/auth";

export default {
  name: "profileContainer",
  components: { ProfileComponent },

  setup() {
    const store = useAuthStore();

    return { store };
  },
};
</script>

<style scoped></style>
