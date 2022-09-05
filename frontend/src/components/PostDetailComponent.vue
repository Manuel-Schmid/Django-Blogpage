<script lang="ts">
import CommentSectionComponent from "./CommentSectionComponent.vue";
import { formatDateLong, getImageURL, formatFullname } from "../helper/helper";
import { ref } from "vue";
import { useStore } from "../store/blog";

export default {
  name: "PostDetailComponent",
  props: ["postData"],
  components: {
    CommentSectionComponent,
  },

  setup(props: any) {
    let postLiked = ref(false);
    let store = useStore();

    const togglePostLike = (post: Number, user: Number) => {
      const postLikeInput = {
        post: post,
        user: user,
      };
      if (postLiked.value) {
        store.deletePostLike(postLikeInput);
      } else {
        store.createPostLike(postLikeInput);
      }

      postLiked.value = !postLiked.value;
    };

    return {
      formatDateLong,
      getImageURL,
      formatFullname,
      postLiked,
      store,
      togglePostLike,
    };
  },
};
</script>

<template>
  <div class="post-container p-12 flex justify-center items-center">
    <div v-if="postData" class="post">
      <div>
        <div class="w-full relative">
          <div class="post-title leading-5 text-black font-bold mb-3">
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
                @click="togglePostLike(postData.id, store.getUserID)"
                icon="fa-thumbs-up"
                class="text-3xl mb-0.5"
                :class="postLiked ? 'text-blue-600' : ''"
              ></font-awesome-icon>
              <span class="w-full">{{ postData.postLikes.length }}</span>
            </div>
            <div class="mr-0 mb-1 ml-8 flex m-0">
              <p class="font-bold mr-1">Category:</p>
              <router-link
                :to="{
                  name: 'categoryPosts',
                  params: { slug: postData.category.slug },
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
