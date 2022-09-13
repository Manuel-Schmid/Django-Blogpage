<script lang="ts">
import { useRoute } from "vue-router/dist/vue-router";

export default {
  name: "PaginationComponent",
  props: ["numPostPages", "activePage"],

  setup() {
    const route = useRoute();
    return { route };
  },
};
</script>

<template>
  <div class="float-left w-full h-min my-10">
    <div class="m-auto w-max">
      <div v-for="pageNr in numPostPages" class="float-left">
        <span
          v-if="activePage === pageNr"
          class="pagination-link bg-gray-300 cursor-default"
        >
          {{ pageNr }}
        </span>
        <router-link
          v-else
          :to="{ name: route.name, query: { page: pageNr } }"
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
