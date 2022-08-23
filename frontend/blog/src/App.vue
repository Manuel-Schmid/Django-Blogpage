<template>
  <NavbarComponent></NavbarComponent>
  <PostsOverviewComponent></PostsOverviewComponent>

</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue'
import PostsOverviewComponent from "@/components/PostsOverviewComponent";

export default {
  name: 'App',
  components: {
    NavbarComponent,
    PostsOverviewComponent,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
