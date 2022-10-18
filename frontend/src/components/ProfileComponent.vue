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
    const firstNameEditable = ref(false);
    const newFirstName = ref("");
    const lastNameEditable = ref(false);
    const newLastName = ref("");
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

    const updateAccount = async (firstName: string, lastName: string) => {
      if (firstName && lastName) {
        const success = await useAuthStore().updateAccount(firstName, lastName);
        if (success) {
          firstNameEditable.value = false;
          lastNameEditable.value = false;
        }
      }
    };

    return {
      logout,
      changeEmail,
      emailEditable,
      newEmail,
      updateAccount,
      firstNameEditable,
      newFirstName,
      lastNameEditable,
      newLastName,
      passwordChangeFormActive,
    };
  },
};
</script>

<template>
  <div class="profile-container">
    <div v-if="userData" class="w-min m-auto mt-36 text-center">
      <p class="text-xl mb-8 dark:text-white">
        <font-awesome-icon icon="fa-solid fa-user" class="mr-2" />About
      </p>
      <div class="w-min">
        <table
          class="table-auto text-sm text-left text-gray-700 dark:text-gray-300 w-max text-center"
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
                <div v-if="firstNameEditable">
                  <input
                    type="text"
                    v-model="newFirstName"
                    class="bg-gray-100 dark:bg-slate-700 px-2 max-w-[58%]"
                  />
                  <font-awesome-icon
                    @click="
                      newFirstName = userData.firstName;
                      firstNameEditable = false;
                    "
                    icon="fa-solid fa-xmark"
                    class="input-field-icon ml-2 mr-1"
                  />
                  <font-awesome-icon
                    @click="updateAccount(newFirstName, newLastName)"
                    icon="fa-solid fa-check"
                    class="input-field-icon mx-1"
                  />
                </div>
                <div v-else>
                  {{ userData.firstName }}
                  <font-awesome-icon
                    @click="
                      newFirstName = userData.firstName;
                      newLastName = userData.lastName;
                      emailEditable = false;
                      firstNameEditable = true;
                      lastNameEditable = false;
                    "
                    icon="fa-regular fa-pen-to-square"
                    class="cursor-pointer pl-2"
                  />
                </div>
              </td>
            </tr>
            <tr class="profile-table-row">
              <th scope="row">Last name</th>
              <td class="py-4 px-6">
                <div v-if="lastNameEditable">
                  <input
                    type="text"
                    v-model="newLastName"
                    class="bg-gray-100 dark:bg-slate-700 px-2 max-w-[58%]"
                  />
                  <font-awesome-icon
                    @click="lastNameEditable = false"
                    icon="fa-solid fa-xmark"
                    class="input-field-icon ml-2 mr-1"
                  />
                  <font-awesome-icon
                    @click="updateAccount(newFirstName, newLastName)"
                    icon="fa-solid fa-check"
                    class="input-field-icon mx-1"
                  />
                </div>
                <div v-else>
                  {{ userData.lastName }}
                  <font-awesome-icon
                    @click="
                      newFirstName = userData.firstName;
                      newLastName = userData.lastName;
                      emailEditable = false;
                      firstNameEditable = false;
                      lastNameEditable = true;
                    "
                    icon="fa-regular fa-pen-to-square"
                    class="cursor-pointer pl-2"
                  />
                </div>
              </td>
            </tr>
            <tr class="profile-table-row">
              <th scope="row">Email</th>
              <td class="py-4 px-6">
                <div v-if="emailEditable">
                  <input
                    type="email"
                    v-model="newEmail"
                    class="bg-gray-100 dark:bg-slate-700 px-2 w-max"
                  />
                  <font-awesome-icon
                    @click="emailEditable = false"
                    icon="fa-solid fa-xmark"
                    class="input-field-icon ml-2 mr-1"
                  />
                  <font-awesome-icon
                    @click="changeEmail"
                    icon="fa-solid fa-check"
                    class="input-field-icon mx-1"
                  />
                </div>
                <div v-else>
                  {{ userData.email }}
                  <font-awesome-icon
                    @click="
                      newEmail = userData.email;
                      emailEditable = true;
                      firstNameEditable = false;
                      lastNameEditable = false;
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

.input-field-icon {
  @apply text-lg cursor-pointer mb-[-0.125rem];
}
</style>
