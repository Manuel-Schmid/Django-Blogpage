import { defineStore } from 'pinia'
import { useQuery } from "@vue/apollo-composable";
import gql from "graphql-tag";
import { computed, ref } from "vue";

export const useStore = defineStore('blog', {
  state: () =>
    ({
      posts: ref(),
    }),
  getters: {
    getPosts: (state) => state.posts,
  },
  actions: {
    async setPosts(tagSlugParam:string | null = null, categorySlugParam:string | null = null) {
      let response = await useQuery(gql`
            query postsByTagAndCategorySlug($tagSlug: String, $categorySlug: String) {
                posts(tagSlug: $tagSlug, categorySlug: $categorySlug) {
                    slug
                    title
                    dateCreated
                    category {
                        name
                        slug
                    }
                    owner {
                        firstName
                        lastName
                    }
                }
            }
          `,
          {
            tagSlug: tagSlugParam,
            categorySlug: categorySlugParam,
          }
        );
      // this.posts = computed(() => response.value)
      // this.posts = response.result
      // console.log(response.result.value);
      console.log(response.result.value);
    },
  },
})