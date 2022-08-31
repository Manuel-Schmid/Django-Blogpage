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
      <router-link
        v-for="tag in tags"
        :key="tag.slug"
        :class="[
          'rounded-3xl pt-1 pr-4 pb-1 pl-4 m-1 float-left text-black no-underline hover:bg-gray-300 dark:hover:bg-slate-500',
          tag.slug === route.query.tag
            ? 'bg-gray-300 dark:bg-slate-500 cursor-default'
            : 'bg-gray-100 dark:bg-slate-700 cursor-pointer',
        ]"
        :to="{ name: route.name, query: { tag: tag.slug } }"
      >
        <p class="m-0">{{ tag.name }}</p>
      </router-link>
    </div>
  </div>
</template>

<style scoped></style>
