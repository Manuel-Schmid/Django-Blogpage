import { defineStore } from "pinia";
import gql from "graphql-tag";
import { apolloClient } from "../api/client";
import router from "../router/router";
import Register from "../graphql/register.gql";
import VerifyAccount from "../graphql/verifyAccount.gql";
import ResendActivationEmail from "../graphql/resendActivationEmail.gql";
import UpdateAccount from "../graphql/updateAccount.gql";

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
    async registerUser(
      email: string,
      username: string,
      password1: string,
      password2: string
    ) {
      const response = await apolloClient.query({
        query: Register,
        variables: {
          email: email,
          username: username,
          password1: password1,
          password2: password2,
        },
      });
      return response.data.register.success;
    },
    async resendActivationEmail(email: string) {
      const response = await apolloClient.query({
        query: ResendActivationEmail,
        variables: {
          email: email,
        },
      });
      return response.data.resendActivationEmail.errors;
    },
    async verifyAccount(token: string) {
      const response = await apolloClient.query({
        query: VerifyAccount,
        variables: {
          token: token,
        },
      });
      return response.data.verifyAccount.success;
    },
    async sendResetPasswordEmail(email: string) {
      const response = await apolloClient.query({
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
      return response.data.sendPasswordResetEmail.success;
    },
    async resetPassword(
      token: string | undefined,
      newPassword1: string,
      newPassword2: string
    ) {
      const response = await apolloClient.query({
        query: gql`
          mutation PasswordReset(
            $token: String!
            $newPassword1: String!
            $newPassword2: String!
          ) {
            passwordReset(
              token: $token
              newPassword1: $newPassword1
              newPassword2: $newPassword2
            ) {
              success
              errors
            }
          }
        `,
        variables: {
          token: token,
          newPassword1: newPassword1,
          newPassword2: newPassword2,
        },
      });
      return response.data.passwordReset.success;
    },
    async updateAccount(firstName: string, lastName: string) {
      const response = await apolloClient.query({
        query: UpdateAccount,
        variables: {
          firstName: firstName,
          lastName: lastName,
        },
      });
      return response.data.verifyAccount.success;
    },
  },
});
