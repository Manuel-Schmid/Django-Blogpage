<script lang="ts">
export default {
  name: "PostDetailComponent",
  props: ["postData"],

  setup() {
    const formatDate = (date: string) => {
      let options: any = {
        weekday: "long",
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      };
      return new Date(date).toLocaleDateString("en-GB", options);
    };

    const getImageURL = (image: string) => {
      return `${import.meta.env.VITE_MEDIA_URL}${image}`;
    };

    const formatFullname = (firstName: string, lastName: string) => {
      return `${firstName} ${lastName}`;
    };

    const isObjectEmpty = (obj: Object) => {
      return obj
        && Object.keys(obj).length === 0
        && Object.getPrototypeOf(obj) === Object.prototype
    }

    return { formatDate, getImageURL, formatFullname, isObjectEmpty };
  },
};
</script>

<template>
  <div class="post-container p-12 flex justify-center items-center">
    <div v-if="!isObjectEmpty(postData)" class="post">
      <p>{{  }}</p>
      <div>
        <div class="w-full relative">
          <div class="post-title leading-5 text-black font-bold mb-3">
            <p class="mb-0">{{ postData.title }}</p>
          </div>
          <div>
            <p class="mb-0">
              {{ formatDate(postData.dateCreated) }}
            </p>
          </div>
        </div>
        <div class="pt-8 pr-8 pb-0 pl-8 text-left">
          <p>
            {{ postData.text }}
          </p>
        </div>
        <div class="pr-10 text-right">
          <p>
            -
            {{
              formatFullname(
                postData.owner.firstName,
                postData.owner.lastName
              )
            }}
          </p>
        </div>
        <div v-if="postData.image" class="pt-2 pr-8 pb-2 pl-8">
          <img
            class="w-full mt-4"
            :src="getImageURL(postData.image)"
            alt="Post Image"
          />
        </div>
        <div class="mt-8 mr-0 mb-1 ml-8 flex m-0">
          <p class="font-bold">Category:&nbsp</p>
          <router-link
            :to="{ name: 'categoryPosts', params: { slug: postData.category.slug } }"
            class="text-black no-underline"
          >
            {{ postData.category.name }}
          </router-link>
        </div>
        <div class="ml-8 flex m-0">
          <p class="font-bold">Tags:&nbsp</p>
          <router-link
            v-for="tag in postData.tags"
            :to="{ name: 'posts', query: { tag: tag.slug } }"
            :key="tag.slug"
            class="text-black no-underline"
          >
            {{ tag.name }},&nbsp;
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.post-container {
  margin-top: 9vh;
}
.post-container a:hover {
  text-decoration: underline;
}
.post {
  max-width: 940px;
}
.post-title {
  letter-spacing: 1px;
  font-size: 2em;
}
</style>
