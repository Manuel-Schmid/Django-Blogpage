<script lang="ts">
import { useRoute } from "vue-router/dist/vue-router";
import { useAuthStore } from "../store/auth";
import { ref } from "vue";

export default {
  name: "PasswordResetFormComponent",

  setup() {
    const route = useRoute();
    const authStore = useAuthStore();
    const resetSuccess = ref(undefined);
    const newPassword1 = ref("");
    const newPassword2 = ref("");

    const confirmReset = async () => {
      resetSuccess.value = await authStore.resetPassword(
        route.params.token as string,
        newPassword1.value,
        newPassword2.value
      );
    };

    return { confirmReset, newPassword1, newPassword2, resetSuccess };
  },
};
</script>

<template>
  <div class="pw-reset-container h-[91vh]">
    <div class="w-full h-full flex justify-center items-center text-left">
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white text-center"
          >
            Change your password
          </h1>
          <form @submit.prevent="confirmReset">
            <div>
              <label
                for="password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >New Password</label
              >
              <input
                type="password"
                name="password"
                v-model="newPassword1"
                id="password"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required=""
              />
            </div>
            <div class="mt-3">
              <label
                for="password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Confirm new password</label
              >
              <input
                type="password"
                name="password"
                v-model="newPassword2"
                id="passwordConfirm"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required=""
              />
            </div>
            <div
              v-if="resetSuccess"
              class="flex items-center justify-between mt-1 mb-3"
            >
              <div class="flex items-start text-green-500">
                Password reset successful.
              </div>
            </div>
            <div
              v-else-if="resetSuccess === false"
              class="flex items-center justify-between mt-1 mb-3"
            >
              <div class="flex items-start text-red-600">
                Password reset failed.
              </div>
            </div>
            <div v-else class="my-7"></div>
            <button
              @click="confirmReset"
              class="w-full text-white bg-blue-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
            >
              Reset Password
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pw-reset-container {
  margin-top: 9vh;
}
</style>
