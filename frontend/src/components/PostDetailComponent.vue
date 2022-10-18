<script lang="ts">
import CommentSectionComponent from "../components/CommentSectionComponent.vue";
import { formatDateLong, getImageURL, formatFullname } from "../helper/helper";
import { ref } from "vue";
import { usePostStore } from "../store/blog";
import { useAuthStore } from "../store/auth";
import { useRoute } from "vue-router/dist/vue-router";

export default {
  name: "PostDetailComponent",
  props: ["postData"],
  components: {
    CommentSectionComponent,
  },

  setup(props: { postData: any }) {
    const postLiked = ref(!!props.postData?.isLiked);
    let postStore = usePostStore();
    let authStore = useAuthStore();
    const route = useRoute();

    const togglePostLike = async (post: Number) => {
      if (postLiked.value) {
        await postStore.deletePostLike();
      } else {
        await postStore.createPostLike();
      }
      postLiked.value = !postLiked.value;
    };

    return {
      formatDateLong,
      getImageURL,
      formatFullname,
      postLiked,
      togglePostLike,
      authStore,
      route,
    };
  },
};
</script>

<template>
  <div
    class="post-container p-12 flex justify-center items-center dark:text-white"
  >
    <div class="post">
      <div>
        <div class="w-full relative">
          <div
            class="post-title leading-5 text-black dark:text-white font-bold mb-3"
          >
            <p class="mb-0">{{ postData.title }}</p>
          </div>
          <div>
            <p class="mb-0">
              {{ formatDateLong(postData.dateCreated) }}
            </p>
          </div>
        </div>
        <div class="pt-8 pr-8 pb-0 pl-8 text-left">
          <p>
            {{ postData.text }}
          </p>
        </div>
        <div class="pr-10 text-right mt-3">
          <p>
            -
            {{
              formatFullname(postData.owner.firstName, postData.owner.lastName)
            }}
          </p>
        </div>
        <div v-if="postData.image" class="pt-2 pr-8 pb-2 pl-8 mt-6">
          <img
            class="w-full"
            :src="getImageURL(postData.image)"
            alt="Post Image"
          />
        </div>
        <div class="mt-4 w-full">
          <div class="w-full">
            <div class="float-right text-center w-min mt-2 mr-16">
              <font-awesome-icon
                v-if="authStore.user"
                icon="fa-thumbs-up"
                class="text-3xl mb-0.5 cursor-pointer"
                :class="[
                  postLiked
                    ? 'text-blue-700 dark:text-white'
                    : 'dark:text-slate-500',
                ]"
                @click="togglePostLike(postData.id)"
              ></font-awesome-icon>
              <font-awesome-icon
                v-else
                icon="fa-thumbs-up"
                class="text-3xl mb-0.5 dark:text-slate-500"
              ></font-awesome-icon>
              <span class="w-full cursor-default">{{
                postData.likeCount
              }}</span>
            </div>
            <div class="mr-0 mb-1 ml-8 flex m-0">
              <p class="font-bold mr-1">Category:</p>
              <router-link
                :to="{
                  name: 'posts',
                  query: { category: postData.category.slug },
                }"
                class="text-black no-underline"
              >
                {{ postData.category.name }}
              </router-link>
            </div>
            <div class="ml-8 flex m-0">
              <p class="font-bold mr-1">Tags:</p>
              <router-link
                v-for="tag in postData.tags"
                :to="{ name: 'posts', query: { tag: tag.slug } }"
                :key="tag.slug"
                class="text-black no-underline mr-1"
              >
                {{ tag.name }},
              </router-link>
            </div>
            <div class="w-full mt-8">
              <CommentSectionComponent
                :post-id="postData.id"
                :comments="postData.comments"
              ></CommentSectionComponent>
            </div>
          </div>
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
