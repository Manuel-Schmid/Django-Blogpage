import { defineStore } from "pinia";
import gql from "graphql-tag";
import { apolloClient } from "../api/client";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    authToken: "",
  }),
  getters: {
    getAuthToken: (state) => state.authToken,
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
    },
    persist: {
      enabled: true,
    },
  },
});
