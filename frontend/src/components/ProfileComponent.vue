<script lang="ts">
import { apolloClient } from "../api/client";
import router from "../router/router";
import { useAuthStore } from "../store/auth";

export default {
  name: "profileComponent",
  props: ["userData"],

  setup() {
    const logout = async () => {
      await useAuthStore().logoutUser();
      await router.push({ name: "posts" });
    };

    return { logout };
  },
};
</script>

<template>
  <div class="profile-container">
    <div v-if="userData" class="w-min m-auto mt-36 text-center">
      <p class="text-xl mb-8">
        <font-awesome-icon icon="fa-solid fa-user" class="mr-2" />About
      </p>
      <div class="w-min">
        <table
          class="table-auto text-sm text-left text-gray-700 dark:text-gray-300 text-center"
        >
          <thead
            class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-50"
          ></thead>
          <tbody>
            <tr class="profile-table-row">
              <th scope="row">Username</th>
              <td class="py-4 px-6">
                {{ userData.username }}
              </td>
            </tr>
            <tr class="profile-table-row">
              <th scope="row">First name</th>
              <td class="py-4 px-6">
                {{ userData.firstName }}
              </td>
            </tr>
            <tr class="profile-table-row">
              <th scope="row">Last name</th>
              <td class="py-4 px-6">
                {{ userData.lastName }}
              </td>
            </tr>
            <tr class="profile-table-row">
              <th scope="row">Email</th>
              <td class="py-4 px-6">
                {{ userData.email }}
              </td>
            </tr>
          </tbody>
        </table>
        <button
          @click="logout"
          class="float-right mt-6 py-2.5 px-5 text-sm font-medium text-gray-900 bg-white rounded-lg border border-gray-200 hover:bg-gray-100 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
        >
          Logout
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-container {
  margin-top: 9vh;
}
.profile-table-row {
  @apply bg-white border-b dark:bg-gray-800 dark:border-gray-700;
}
.profile-table-row th {
  @apply py-4 px-6 font-bold text-gray-900 whitespace-nowrap dark:text-white;
}
</style>
