<script>
import { useRoute } from "vue-router";

export default {
  name: "TagListComponent",
  props: ["tagsData"],

  setup() {
    const route = useRoute();
    return { route };
  },
};
</script>

<template>
  <div class="mb-2" v-if="tagsData">
    <p class="mb-0 font-bold">Tags:</p>
    <div class="mt-2 inline-block items-center justify-center">
      <div v-for="tag in tagsData" :key="tag.slug" class="float-left">
        <router-link
          v-if="route.query.tags?.split(',').includes(tag.slug)"
          class="tag-link bg-gray-300 dark:bg-slate-500 dark:text-white"
          :to="{
            name: route.name,
            query: {
              ...route.query,
              tags: route.query.tags.includes(',')
                ? route.query.tags
                    .replace(tag.slug + ',', '')
                    .replace(',' + tag.slug, '')
                    .replace(tag.slug, '')
                : undefined,
              page: undefined,
            },
          }"
        >
          <p class="m-0">{{ tag.name }}</p>
        </router-link>
        <router-link
          v-else
          class="tag-link bg-gray-100 dark:bg-slate-700 dark:text-white"
          :to="{
            name: route.name,
            query: {
              ...route.query,
              tags: route.query.tags
                ? route.query.tags + ',' + tag.slug
                : tag.slug,
              page: undefined,
            },
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
