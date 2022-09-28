<script lang="ts">
import router from "../router/router";
import { useAuthStore } from "../store/auth";
import PasswordChangeFormComponent from "./PasswordChangeFormComponent.vue";
import { ref } from "vue";

export default {
  name: "profileComponent",
  components: { PasswordChangeFormComponent },

  props: ["userData"],

  setup() {
    const passwordChangeFormActive = ref(false);
    const emailEditable = ref(false);
    const newEmail = ref("");

    const logout = async () => {
      await useAuthStore().logoutUser();
      await router.push({ name: "posts" });
    };

    const changeEmail = async () => {
      const success = await useAuthStore().changeEmail(newEmail.value);
      if (success) {
        emailEditable.value = false;
      }
    };

    return {
      logout,
      changeEmail,
      passwordChangeFormActive,
      emailEditable,
      newEmail,
    };
  },
};
</script>

<template>
  <div class="profile-container">
    <div v-if="userData" class="w-min m-auto mt-36 text-center">
      <p class="text-xl mb-8">
        <font-awesome-icon icon="fa-solid fa-user" class="mr-2" />About
      </p>
      <div class="w-max">
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
                <div v-if="emailEditable">
                  <input
                    type="email"
                    v-model="newEmail"
                    class="dark:bg-slate-700 px-2 w-max"
                  />
                  <font-awesome-icon
                    @click="emailEditable = false"
                    icon="fa-solid fa-xmark"
                    class="email-field-icon ml-2 mr-1"
                  />
                  <font-awesome-icon
                    @click="changeEmail"
                    icon="fa-solid fa-check"
                    class="email-field-icon mx-1"
                  />
                </div>
                <div v-else>
                  {{ userData.email }}
                  <font-awesome-icon
                    @click="
                      newEmail = userData.email;
                      emailEditable = true;
                    "
                    icon="fa-regular fa-pen-to-square"
                    class="cursor-pointer pl-2"
                  />
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="h-max">
          <button
            @click="passwordChangeFormActive = !passwordChangeFormActive"
            class="float-left mt-6 py-2.5 px-8 text-sm font-medium text-gray-900 bg-white rounded-lg border border-gray-200 hover:bg-gray-100 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
          >
            Change Password
          </button>
          <PasswordChangeFormComponent
            v-if="passwordChangeFormActive"
            @toggle-password-change-form="
              passwordChangeFormActive = !passwordChangeFormActive
            "
          ></PasswordChangeFormComponent>
        </div>
        <button
          @click="logout"
          class="float-right mt-6 py-2.5 px-6 text-sm font-medium text-gray-900 bg-white rounded-lg border border-gray-200 hover:bg-gray-100 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
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
.email-field-icon {
  @apply text-lg cursor-pointer mb-[-0.125rem];
}
</style>
