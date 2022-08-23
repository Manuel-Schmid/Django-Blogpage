<template>
  <PostOverviewComponent :posts-data="result" />
</template>

<script>
import PostOverviewComponent from '@/components/PostsOverviewComponent'
import {useQuery} from "@vue/apollo-composable";
import gql from "graphql-tag";

export default {
  name: 'PostOverviewView',
  components: {
    PostOverviewComponent
  },

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
      `);
    return { result };
  }
}
</script>
