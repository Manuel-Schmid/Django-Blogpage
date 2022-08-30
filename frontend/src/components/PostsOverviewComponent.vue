<script lang="ts">
import { useRoute } from "vue-router";
import { ref } from "vue";

export default {
  name: "PostOverviewComponent",
  props: ["postsData", "tagsData"],

  setup() {
    let hover = ref('none')
    const route = useRoute();

    const formatDate = (date: string) => {
      let options: any = { year: "numeric", month: "2-digit", day: "2-digit" };
      return new Date(date).toLocaleDateString("en-GB", options);
    };

    const formatFullname = (firstName: string, lastName: string) => {
      return `${firstName} ${lastName}`;
    };

    return { formatDate, formatFullname, route, hover };
  },
};


</script>

<template>
  <div class="post-overview-container p-12 flex justify-center items-center">
    <div class="content-container w-full">
      <div class="mb-2" v-if="tagsData">
        <p class="mb-0 font-bold">Tags:</p>
        <div class="mt-2 inline-block items-center justify-center">
          <router-link
            v-for="tag in tagsData"
            :key="tag.slug"
            :class="['post-tag pt-1 pr-4 pb-1 pl-4 m-1 float-left text-black no-underline hover:bg-gray-300 dark:hover:bg-slate-500', (tag.slug === route.query.tag) ? 'bg-gray-300 dark:bg-slate-500 cursor-default' : 'bg-gray-100 dark:bg-slate-700 cursor-pointer']"
            :to="{ name: route.name, query: { tag: tag.slug } }"
          >
            <p class="m-0">{{ tag.name }}</p>
          </router-link>
        </div>
      </div>
      <p class="title leading-5 text-black font-bold mb-8 mt-4 mt-9">Posts:</p>
      <div v-if="postsData">
        <router-link
          v-for="(post, index) in postsData"
          :key="post.id"
          :to="{ name: 'postDetail', params: { slug: post.slug } }"
          @mouseenter="hover=index"
          @mouseleave="hover='none'"
          :class="['post shadow-lg mt-2 mb-2 pt-5 pr-2 pb-1 pl-2 float-left inline-block text-black no-underline dark:bg-[#262b39]', hover===index ? 'shadow-2xl' : '']"
        >
          <div class="post-title pt-0 pr-4 pb-0 pl-4 leading-5 text-black font-bold">
            <p class="mb-4">{{ post.title }}</p>
          </div>
          <div class="post-creation-info">
            <p>
              {{ formatFullname(post.owner.firstName, post.owner.lastName) }} -
              {{ formatDate(post.dateCreated) }}
            </p>
          </div>
          <div class="text-right">
            <p class="post-category">{{ post.category.name }}</p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.post-overview-container {
  margin-top: 9vh;
}
.content-container {
  max-width: 970px;
}
.post-tag {
  border-radius: 15px;
}
.title {
  letter-spacing: 1px;
  font-size: 2em;
}
.post {
  width: calc(40% - 20px);
  margin-right: 5%;
  margin-left: 5%;
  border-radius: 15px;
  transition: box-shadow 200ms;
}
.post-title {
  letter-spacing: 1px;
  font-size: 1.4em;
}
.post-category {
  margin: 0.5em;
}

</style>
