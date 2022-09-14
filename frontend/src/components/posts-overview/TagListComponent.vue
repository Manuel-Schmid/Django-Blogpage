<script>
import { useRoute } from "vue-router";

export default {
  name: "TagListComponent",
  props: ["tags"],

  setup() {
    const route = useRoute();
    return { route };
  },
};
</script>

<template>
  <div class="mb-2" v-if="tags">
    <p class="mb-0 font-bold">Tags:</p>
    <div class="mt-2 inline-block items-center justify-center">
      <div v-for="tag in tags" :key="tag.slug" class="float-left">
        <router-link
          v-if="tag.slug === route.query.tag"
          class="tag-link bg-gray-300 dark:bg-slate-500"
          :to="{
            name: route.name,
            query: { ...route.query, tag: undefined, page: undefined },
          }"
        >
          <p class="m-0">{{ tag.name }}</p>
        </router-link>
        <router-link
          v-else
          class="tag-link bg-gray-100 dark:bg-slate-700"
          :to="{
            name: route.name,
            query: { ...route.query, tag: tag.slug, page: undefined },
          }"
        >
          <p class="m-0">{{ tag.name }}</p>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tag-link {
  @apply rounded-3xl pt-1 pr-4 pb-1 pl-4 m-1 float-left text-black no-underline hover:bg-gray-300 dark:hover:bg-slate-500 cursor-pointer;
}
</style>
