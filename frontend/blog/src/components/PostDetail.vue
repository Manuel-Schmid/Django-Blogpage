<script setup>
import { ref } from 'vue'; // defineProbs
import { useQuery } from '@vue/apollo-composable';
import gql from 'graphql-tag';

const response = useQuery(gql`
      query getPostById {
          postById(id: 1) {
            title
          }
      }
    `);
console.log(response.result);

const postData = {
  data: {
    postById: {
      title: 'Alea iacta est',
      text: 'Phasellus ipsum nulla, lobortis quis sem pharetra, cursus interdum dui. Fusce turpis eros, pretium non metus luctus, pellentesque maximus dolor. Aliquam erat volutpat. Sed nec interdum lorem. Nullam eget eros vitae libero interdum accumsan. Integer consequat tellus vel ipsum pulvinar pharetra. In tristique, justo imperdiet sagittis eleifend, augue metus condimentum quam, ut convallis sapien libero quis elit. Nulla lobortis nisl blandit nulla dapibus, vitae facilisis diam blandit. Fusce mollis at arcu vel fringilla. Cras iaculis lobortis ex, eu lobortis mi hendrerit id. Etiam feugiat at ante sed condimentum. Donec gravida lectus ut ullamcorper tempus. Pellentesque quis eros id leo mollis hendrerit. Vivamus vel leo mollis, facilisis velit sodales, ultricies sapien. Aliquam in ante sit amet eros ultricies interdum accumsan posuere dui. Quisque at massa tristique, finibus dolor cursus, lacinia orci. Sed in consectetur ligula. Etiam id mi quis nisi eleifend consectetur sed id urna. Donec feugiat massa sed ante gravida pharetra nec condimentum leo. In viverra dui eu arcu fringilla, non cursus odio vulputate. Morbi volutpat sed metus sit amet tincidunt.',
      image: 'images/junction.jpeg',
      dateCreated: '2022-08-15T15:00:57.031000+00:00',
      category: {
        name: 'Politics'
      },
      owner: {
        firstName: 'Winston',
        lastName: 'Wolf',
      },
      tags: [
        {name: "lorem"},
        {name: "ipsum"},
        {name: "dolor"},
        {name: "sit"},
        {name: "amet"},
      ]
    }
  }
};




const apiMediaURL = 'http://api.my-app.lo/media/';

const title = ref(postData.data.postById.title);
const text = ref(postData.data.postById.text);
const category = ref(postData.data.postById.category.name);
const owner = ref(postData.data.postById.owner.firstName + ' ' + postData.data.postById.owner.lastName);
const tags = ref(postData.data.postById.tags);
const imageURL = ref(apiMediaURL + postData.data.postById.image);


let options = { weekday: 'long', year: 'numeric', month: '2-digit', day: '2-digit' };
const date = ref(new Date(postData.data.postById.dateCreated).toLocaleDateString("en-GB", options));

</script>


<template>
  <div class="post-container">
    <div class="post">
      <div class="post-content">
        <div class="post-header">
          <div class="post-title">
            <p>{{ title }}</p>
          </div>
          <div class="post-date">
            <p>
              {{ date }}
            </p>
        </div>
        </div>
        <div class="post-text">
          <p>
            {{ text }}
          </p>
        </div>
        <div class="post-owner">
          <p>
            {{ '- ' + owner }}
          </p>
        </div>
        <div class="post-image-container">
          <img class="post-image" :src="imageURL" alt="Post Image">
        </div>
        <div class="post-category">
          <p>
            {{ category }}
          </p>
        </div>
        <div class="post-tags">
          <ul>
            <li v-for="tag in tags" class="post-tag" :key="tag.name">{{ tag.name }}</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.post-container {
  margin-top: 9vh;
  padding: 50px;
}
.post {

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
.post-date {
  position: absolute;
  top: -20px;
  right: 0;
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

}
.post-tags {

}
.post-tag {

}







</style>


