<script lang="ts">
import router from "../router";
import { useRoute } from "vue-router";

export default {
  name: "PostOverviewComponent",
  props: ["postsData", "tagsData"],

  setup() {
    const route = useRoute();

    const formatDate = (date: string) => {
      let options: any = { year: "numeric", month: "2-digit", day: "2-digit" };
      return new Date(date).toLocaleDateString("en-GB", options);
    };

    const formatFullname = (firstName: string, lastName: string) => {
      return `${firstName} ${lastName}`;
    };
    return { formatDate, formatFullname, route };
  },
};
</script>

<template>
  <div class="post-overview-container">
    <div class="content-container">
      <div class="tags-container" v-if="tagsData">
        <p style="margin-bottom: 0"><b>Tags:&nbsp;</b></p>
        <div class="tags">
          <router-link
            v-for="tag in tagsData.tags"
            :key="tag.slug"
            :class="['post-tag', (tag.slug === route.query.tag) ? 'active-tag' : '']"
            :to="{ name: route.name, query: { tag: tag.slug } }"
          >
            <p class="tag-name">{{ tag.name }}</p>
          </router-link>
        </div>
      </div>
      <p class="title">Posts:</p>
      <div v-if="postsData" class="posts-container">
        <router-link
          v-for="post in postsData.posts"
          :key="post.id"
          :to="{ name: 'postDetail', params: { slug: post.slug } }"
          class="post"
        >
          <div class="post-title">
            <p>{{ post.title }}</p>
          </div>
          <div class="post-creation-info">
            <p>
              {{ formatFullname(post.owner.firstName, post.owner.lastName) }} -
              {{ formatDate(post.dateCreated) }}
            </p>
          </div>
          <div class="post-category">
            <p>{{ post.category.name }}</p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.post-overview-container {
  margin-top: 9vh;
  padding: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.content-container {
  width: 100%;
  max-width: 970px;
}
.tags-container {
  margin-bottom: 10px;
}
.tags {
  margin-top: 10px;
  display: inline-block;
  align-items: center;
  justify-content: center;
}
.post-tag {
  background-color: whitesmoke;
  border-radius: 15px;
  padding: 4px 15px;
  margin: 5px;
  float: left;
}
.active-tag {
  background-color: #d7d7d7;
}
.post-tag:hover {
  background-color: #cac9c9;
  cursor: pointer;
}
.tag-name {
  margin: 0;
}
.title {
  line-height: 20px;
  color: black;
  font-weight: bold;
  letter-spacing: 1px;
  font-size: 2em;
}
.posts-container {
}
.posts-container a, .tags-container a {
  color: inherit;
  text-decoration: inherit;
}
.post {
  width: calc(40% - 20px);
  margin: 10px 5%;
  float: left;
  display: inline-block;
  padding: 5px 10px;
  border-radius: 15px;
  transition: 200ms;
  -webkit-box-shadow: -5px 4px 17px 2px rgba(179, 179, 179, 0.45);
  -moz-box-shadow: -5px 4px 17px 2px rgba(179, 179, 179, 0.45);
  box-shadow: -5px 4px 17px 2px rgba(179, 179, 179, 0.45);
}
.post:hover {
  -webkit-box-shadow: -5px 4px 17px 7px rgba(179, 179, 179, 0.45);
  -moz-box-shadow: -5px 4px 17px 7px rgba(179, 179, 179, 0.45);
  box-shadow: -5px 4px 17px 7px rgba(179, 179, 179, 0.45);
  cursor: pointer;
}
.post-link {
  height: 100%;
  width: 100%;
}
.post-title {
  padding: 0 15px;
  line-height: 20px;
  color: black;
  font-weight: bold;
  letter-spacing: 1px;
  font-size: 1.4em;
  transition: 200ms;
}
.post-title p {
  margin-bottom: 15px;
}
.post-creation-info {
}
.post-category {
  text-align: right;
}
.post-category p {
  margin: 0.5em;
}
</style>
