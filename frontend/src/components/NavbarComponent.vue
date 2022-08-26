<script lang="ts">
export default {
  name: "NavbarComponent",
};
</script>

<template>
  <header class="header fixed top-0 left-0 w-full bg-white">
    <nav class="navbar h-full pr-4 flex flex-row items-center">
      <div class="w-auto flex flex-row">
        <router-link class="nav-item pt-2 pr-5 pb-2 pl-5 mt-0 mr-1 mb-0 ml-1 leading-5 text-black font-bold text-center" :to="{ name: 'posts' }">
          Posts
        </router-link>
        <div class="nav-item pt-2 pr-5 pb-2 pl-5 mt-0 mr-1 mb-0 ml-1 leading-5 text-black font-bold text-center">My Blog</div>
        <div class="nav-item pt-2 pr-5 pb-2 pl-5 mt-0 mr-1 mb-0 ml-1 leading-5 text-black font-bold text-center">Profile</div>
      </div>
    </nav>
  </header>
</template>

<style scoped>
.header {
  height: 9vh;
  z-index: 100;
  -webkit-box-shadow: 10px 10px 16px -19px rgba(0, 0, 0, 0.75);
  -moz-box-shadow: 10px 10px 16px -19px rgba(0, 0, 0, 0.75);
  box-shadow: 10px 10px 16px -19px rgba(0, 0, 0, 0.75);
}
.navbar {
  justify-content: end;
  -webkit-box-shadow: 10px 10px 16px -19px rgba(0, 0, 0, 0.75);
  -moz-box-shadow: 10px 10px 16px -19px rgba(0, 0, 0, 0.75);
  box-shadow: 10px 10px 16px -19px rgba(0, 0, 0, 0.75);
}
.navbar a {
  color: inherit;
  text-decoration: inherit;
}
.nav-item {
  background-color: whitesmoke;
  letter-spacing: 1px;
  font-size: 1em;
  text-align: center;
  transition: background-color 200ms;
}
.nav-item:hover {
  background-color: lightgrey;
  cursor: pointer;
  border-bottom: 1px solid black;
  padding-bottom: calc(0.5rem - 1px);
}
</style>

