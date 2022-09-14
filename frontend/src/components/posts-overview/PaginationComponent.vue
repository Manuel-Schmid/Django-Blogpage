<script lang="ts">
import { useRoute } from "vue-router/dist/vue-router";

export default {
  name: "PaginationComponent",
  props: ["numPostPages", "activePage"],

  setup(props: { numPostPages: number; activePage: number }) {
    let numPostPagesList = Array.from(
      { length: props.numPostPages },
      (x, i) => ++i
    );

    let paginationPageNums = slicePaginationPageNums(
      numPostPagesList,
      props.activePage
    );

    let firstPage = paginationPageNums.includes(1) ? 0 : 1;
    let lastPage = paginationPageNums.includes(props.numPostPages)
      ? 0
      : props.numPostPages;

    const route = useRoute();
    return { route, paginationPageNums, firstPage, lastPage };
  },
};

function slicePaginationPageNums(numPostPages: any, activePage: number) {
  return numPostPages.length > 7 && activePage > numPostPages.length - 4
    ? numPostPages.slice(numPostPages.length - 7, numPostPages.length)
    : numPostPages.length > 7 && numPostPages.length > 4 && activePage > 4
    ? numPostPages.slice(activePage - 4, activePage + 3)
    : numPostPages.slice(0, 7);
}
</script>

<template>
  <div class="float-left w-full h-min my-10">
    <div class="m-auto w-max">
      <div
        class="pagination-link-wrapper mr-3"
        :class="!firstPage && 'invisible'"
      >
        <router-link
          :to="{ name: route.name, query: { ...route.query, page: firstPage } }"
          class="pagination-special-link-wrapper"
        >
          <span class="pagination-special-link">
            <font-awesome-icon
              icon="fa-solid fa-arrow-left"
              class="float-left mr-2"
            />
            <span>{{ firstPage }}</span>
          </span>
        </router-link>
      </div>
      <div v-for="pageNr in paginationPageNums" class="pagination-link-wrapper">
        <span
          v-if="activePage === pageNr"
          class="pagination-link bg-gray-300 dark:bg-slate-500 cursor-default"
        >
          {{ pageNr }}
        </span>
        <router-link
          v-else
          :to="{ name: route.name, query: { ...route.query, page: pageNr } }"
          class="pagination-link bg-gray-100 dark:bg-slate-700 cursor-pointer"
        >
          {{ pageNr }}
        </router-link>
      </div>
      <div v-if="lastPage" class="pagination-link-wrapper ml-3">
        <router-link
          :to="{ name: route.name, query: { ...route.query, page: lastPage } }"
          class="pagination-special-link-wrapper"
        >
          <span class="pagination-special-link">
            <span>{{ lastPage }}</span>
            <font-awesome-icon
              icon="fa-solid fa-arrow-right"
              class="float-right ml-2 leading-5"
            />
          </span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pagination-link {
  @apply rounded-3xl min-w-[1.75rem] px-2 h-7 text-black mx-1 text-center leading-[1.85rem] dark:text-white;
}
.pagination-link-wrapper {
  @apply float-left flex items-center justify-center;
}
.pagination-special-link-wrapper {
  @apply pagination-link cursor-pointer;
}
.pagination-special-link {
  @apply inline-block w-max leading-5;
}
</style>
