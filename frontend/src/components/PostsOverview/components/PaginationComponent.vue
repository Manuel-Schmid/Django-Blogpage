<script lang="ts">
export default {
  name: "PaginationComponent",
  setup() {
    return {};
  },
};
</script>

<template>
  <div class="float-left w-full h-min my-10">
    <div class="m-auto w-max">
      <div v-for="pageNr in 3" class="float-left">
        <router-link
          :to="{
            name: 'posts',
            params: { page: pageNr },
          }"
          class="rounded-3xl w-7 h-7 bg-gray-200 text-black mx-2 text-center leading-7 cursor-pointer"
        >
          {{ pageNr }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
