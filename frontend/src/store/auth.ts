import { defineStore } from "pinia";
import gql from "graphql-tag";
import { apolloClient } from "../api/client";
import router from "../router/router";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    refreshToken: "",
    user: {},
  }),
  persist: {
    enabled: true,
  },
  getters: {
    getRefreshToken: (state) => state.refreshToken,
    getUser: (state) => state.user,
  },
  actions: {
    async fetchRefreshToken(username: String, password: String) {
      const response = await apolloClient.mutate({
        mutation: gql`
          mutation TokenAuth($username: String!, $password: String!) {
            tokenAuth(username: $username, password: $password) {
              refreshToken
            }
          }
        `,
        variables: {
          username: username,
          password: password,
        },
      });
      if (response.data !== null) {
        this.refreshToken = response.data.tokenAuth.refreshToken;
        await this.fetchUser();
        await router.push({ name: "posts" });
      } else {
        // inform user login failed
        console.log("login failed");
      }
    },
    async fetchUser() {
      this.user = {};
      const response = await apolloClient.query({
        query: gql`
          {
            user {
              username
              email
              firstName
              lastName
            }
          }
        `,
      });
      if (response.data !== null) {
        this.user = response.data.user;
      } else {
        // inform user login failed
        console.log("login failed");
      }
    },
  },
});
