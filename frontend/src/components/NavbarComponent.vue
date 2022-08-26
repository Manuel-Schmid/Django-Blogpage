<script lang="ts">
export default {
  name: "NavbarComponent",
};
</script>

<template>
  <header class="header">
    <nav class="navbar">
      <div class="nav-container">
        <router-link class="nav-item" :to="{ name: 'posts' }">
          Posts
        </router-link>
        <div class="nav-item">My Blog</div>
        <div class="nav-item">Profile</div>
      </div>
    </nav>
  </header>
</template>

<style scoped></style>
