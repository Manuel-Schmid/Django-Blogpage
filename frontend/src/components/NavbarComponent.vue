<script lang="ts">
export default {
  name: "NavbarComponent",
};
</script>

<template>
  <header class="">
    <nav class="">
      <div class="">
        <router-link class="" :to="{ name: 'posts' }">
          Posts
        </router-link>
        <div class="">My Blog</div>
        <div class="">Profile</div>
      </div>
    </nav>
  </header>
</template>

<style scoped></style>
