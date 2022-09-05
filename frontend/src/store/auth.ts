import { defineStore } from "pinia";
import gql from "graphql-tag";
import { apolloClient } from "../api/client";
import router from "../router/router";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    authToken: "",
    username: "",
  }),
  getters: {
    getAuthToken: (state) => state.authToken,
    getUsername: (state) => state.username,
  },
  actions: {
    async fetchAuthToken(username: String, password: String) {
      const response = await apolloClient.mutate({
        mutation: gql`
          mutation TokenAuth($username: String!, $password: String!) {
            tokenAuth(username: $username, password: $password) {
              token
              payload
              refreshExpiresIn
            }
          }
        `,
        variables: {
          username: username,
          password: password,
        },
      });
      this.authToken = response.data.tokenAuth.token;
      this.username = response.data.tokenAuth.payload.username;
      await router.push({ name: "posts" });
    },
    persist: {
      enabled: true,
    },
  },
});
