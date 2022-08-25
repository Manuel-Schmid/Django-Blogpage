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

    return { formatDate, getImageURL, formatFullname };
  },
};
</script>

<template>
  <div class="post-container">
    <div v-if="postData" class="post">
      <div class="post-content">
        <div class="post-header">
          <div class="post-title">
            <p>{{ postData.postBySlug.title }}</p>
          </div>
          <div class="post-date">
            <p>
              {{ formatDate(postData.postBySlug.dateCreated) }}
            </p>
          </div>
        </div>
        <div class="post-text">
          <p>
            {{ postData.postBySlug.text }}
          </p>
        </div>
        <div class="post-owner">
          <p>
            -
            {{
              formatFullname(
                postData.postBySlug.owner.firstName,
                postData.postBySlug.owner.lastName
              )
            }}
          </p>
        </div>
        <div v-if="postData.postBySlug.image" class="post-image-container">
          <img
            class="post-image"
            :src="getImageURL(postData.postBySlug.image)"
            alt="Post Image"
          />
        </div>
        <div class="post-category flex margin-zero">
          <p><b>Category:&nbsp;</b></p>
          <router-link :to="{ name: 'categoryPosts', params: { slug: postData.postBySlug.category.slug } }">
            {{ postData.postBySlug.category.name }}
          </router-link>
        </div>
        <div class="post-tags flex margin-zero">
          <p><b>Tags:&nbsp;</b></p>
          <router-link
            v-for="tag in postData.postBySlug.tags"
            :to="{ name: 'posts', query: { tag: tag.slug } }"
            :key="tag.slug"
            class="post-tag"
          >
            {{ tag.name }},&nbsp;
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
