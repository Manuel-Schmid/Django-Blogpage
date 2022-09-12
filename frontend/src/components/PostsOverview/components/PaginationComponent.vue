<script lang="ts">
import { useRoute } from "vue-router/dist/vue-router";

export default {
  name: "PaginationComponent",
  setup() {
    const route = useRoute();
    const activePage = route.params.page ? route.params.page : 1;
    return { activePage };
  },
};
</script>

<template>
  <div class="float-left w-full h-min my-10">
    <div class="m-auto w-max">
      <div v-for="pageNr in 3" class="float-left">
        <span
          v-if="activePage === pageNr"
          class="pagination-link bg-gray-300 cursor-default"
        >
          {{ pageNr }}
        </span>
        <router-link
          v-else
          :to="{
            name: 'posts',
            params: { page: pageNr },
          }"
          class="pagination-link bg-gray-100 cursor-pointer"
        >
          {{ pageNr }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pagination-link {
  @apply rounded-3xl w-7 h-7 text-black px-3 py-1.5 mx-2 text-center leading-7;
}
</style>
