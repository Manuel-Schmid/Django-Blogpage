<script>
import { useQuery } from '@vue/apollo-composable';
import gql from 'graphql-tag';

export default {
  setup() {
    let { result } = useQuery(gql`
        {
          posts {
            id
            slug
            title
            dateCreated
            category {
              name
            }
            owner {
              firstName
              lastName
            }
          }
        }
      `, {
      id: 2,
    });
    return { result, formatDate, formatFullname };
  }
}

const formatDate = (date) => {
  let options = { year: 'numeric', month: '2-digit', day: '2-digit' };
  return new Date(date).toLocaleDateString("en-GB", options);
}

const formatFullname = (firstName, lastName) => {
  return firstName + ' ' + lastName
}

</script>


<template>
  <div class="post-overview-container">
    <div class="content-container">
      <p class="title">Posts: </p>
      <div class="posts-container" v-if="result">
            <router-link :to="{ name: 'postDetail', params: { slug: post.slug } }" class="post" v-for="post in result.posts" :key="post.id">
              <div class="post-title">
                <p>{{ post.title }}</p>
              </div>
              <div class="post-creation-info">
                <p>
                  {{ formatFullname(post.owner.firstName, post.owner.lastName) + ' - ' + formatDate(post.dateCreated) }}
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
.title {
  line-height: 20px;
  color: black;
  font-weight: bold;
  letter-spacing: 1px;
  font-size: 2em;
}
.posts-container {

}
.posts-container a {
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
  -webkit-box-shadow: -5px 4px 17px 2px rgba(179,179,179,0.45);
  -moz-box-shadow: -5px 4px 17px 2px rgba(179,179,179,0.45);
  box-shadow: -5px 4px 17px 2px rgba(179,179,179,0.45);
}
.post:hover {
  -webkit-box-shadow: -5px 4px 17px 7px rgba(179,179,179,0.45);
  -moz-box-shadow: -5px 4px 17px 7px rgba(179,179,179,0.45);
  box-shadow: -5px 4px 17px 7px rgba(179,179,179,0.45);
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


