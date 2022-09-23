import { defineStore } from "pinia";
import gql from "graphql-tag";
import { apolloClient } from "../api/client";
import router from "../router/router";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    refreshToken: null,
    user: null,
  }),
  persist: {
    enabled: true,
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
        // todo
      }
    },
    async fetchUser() {
      this.user = null;
      const response = await apolloClient.query({
        query: gql`
          {
            user {
              id
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
        // todo
      }
    },
    async logoutUser() {
      this.user = this.refreshToken = null;
      // delete cookies
      const responseDeleteTokenCookie = await apolloClient.query({
        query: gql`
          mutation {
            deleteTokenCookie {
              deleted
            }
          }
        `,
      });
      const ResponseDeleteRefreshTokenCookie = await apolloClient.query({
        query: gql`
          mutation {
            deleteRefreshTokenCookie {
              deleted
            }
          }
        `,
      });
      if (
        responseDeleteTokenCookie.data.deleteTokenCookie.deleted &&
        ResponseDeleteRefreshTokenCookie.data.deleteRefreshTokenCookie.deleted
      ) {
        await apolloClient.resetStore();
      }
    },
    async sendPasswordResetEmail(email: string) {
      await apolloClient.query({
        query: gql`
          mutation SendPasswordResetEmail($email: String!) {
            sendPasswordResetEmail(email: $email) {
              success
            }
          }
        `,
        variables: {
          email: email,
        },
      });
    },
  },
});
