<script>
import { useQuery } from '@vue/apollo-composable';
import gql from 'graphql-tag';

export default {
  setup() {
    let { result } = useQuery(gql`
      query getPostBySlug($slug: String!) {
        postBySlug(slug: $slug) {
          title
          text
          image
          dateCreated
          category {
            name
          }
          owner {
            firstName
            lastName
          }
          tags {
            name
          }
        }
      }
      `, {
      slug: "suspendisse-varius",
    });
    return { result, formatDate, getImageURL, formatFullname };
  }
}

const formatDate = (date) => {
  let options = { weekday: 'long', year: 'numeric', month: '2-digit', day: '2-digit' };
  return new Date(date).toLocaleDateString("en-GB", options);
}

const getImageURL = (image) => {
  return process.env.VUE_APP_MEDIA_URL + image;
}

const formatFullname = (firstName, lastName) => {
  return firstName + ' ' + lastName
}

</script>


<template>
  <div class="post-container" >
    <div class="post" v-if="result">
      <div class="post-content">
        <div class="post-header">
          <div class="post-title">
            <p>{{ result.postBySlug.title }}</p>
          </div>
          <div class="post-date">
            <p>
              {{ formatDate(result.postBySlug.dateCreated) }}
            </p>
          </div>
        </div>
        <div class="post-text">
          <p>
            {{ result.postBySlug.text }}
          </p>
        </div>
        <div class="post-owner">
          <p>
            {{ '- ' + formatFullname(result.postBySlug.owner.firstName, result.postBySlug.owner.lastName) }}
          </p>
        </div>
        <div class="post-image-container" v-if="result.postBySlug.image">
          <img class="post-image" :src="getImageURL(result.postBySlug.image)" alt="Post Image">
        </div>
        <div class="post-category flex margin-zero">
          <p><b>Category:&nbsp;</b></p>
          <p>{{ result.postBySlug.category.name }}</p>
        </div>
        <div class="post-tags flex margin-zero">
          <p><b>Tags:&nbsp;</b></p>
          <p v-for="tag in result.postBySlug.tags" class="post-tag" :key="tag.name">{{ tag.name }},&nbsp;</p>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.post-container {
  margin-top: 9vh;
  padding: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.post {
  max-width: 940px;
}
.post-container {

}
.post-content {

}
.post-header {
  width: 100%;
  position: relative;
}
.post-title {
  line-height: 20px;
  color: black;
  font-weight: bold;
  letter-spacing: 1px;
  font-size: 2em;
}
.post-title p, .post-date p {
  margin-bottom: 0;
}
.post-date {

}
.post-text {
  padding: 30px 30px 0 30px;
  text-align: left;
}
.post-owner {
  padding: 0 40px 0 0;
  text-align: right;
}
.post-image-container {
  padding: 10px 30px;
}
.post-image {
  width: 100%;
}
.post-category {
  margin: 30px 0 3px 30px;
}
.post-tags {
  margin-left: 30px;
}
.post-tag {
  /*text-decoration: underline;*/
}
.flex {
  display: flex;
}
.margin-zero * {
  margin: 0;
}






</style>


