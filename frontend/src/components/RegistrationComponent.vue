<script lang="ts">
import { ref } from "vue";
import { useAuthStore } from "../store/auth";

export default {
  name: "RegistrationComponent",
  setup() {
    let usedEmail = "";
    const email = ref("");
    const username = ref("");
    const password1 = ref("");
    const password2 = ref("");
    const signupSuccess: any = ref(undefined);
    const alreadyVerified = ref(false);

    const clearInputs = async () => {
      usedEmail = await email.value;
      email.value = "";
      username.value = "";
      password1.value = "";
      password2.value = "";
    };

    const submitRegistration = async () => {
      signupSuccess.value = await useAuthStore().registerUser(
        email.value,
        username.value,
        password1.value,
        password2.value
      );
      if (signupSuccess.value) {
        await clearInputs();
      }
    };

    const resendActivationEmail = async () => {
      const responseErrors = await useAuthStore().resendActivationEmail(
        usedEmail
      );
      if (responseErrors === null) {
        signupSuccess.value = true;
      } else {
        alreadyVerified.value =
          responseErrors.email[0].code === "already_verified";
      }
    };

    return {
      submitRegistration,
      resendActivationEmail,
      email,
      username,
      password1,
      password2,
      resetSuccess: signupSuccess,
      alreadyVerified,
    };
  },
};
</script>

<template>
  <div class="mt-[9vh] h-[91vh]">
    <div class="w-full h-full flex justify-center items-center text-left">
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white text-center"
          >
            Create a new account
          </h1>
          <form
            ref="signupForm"
            class="space-y-4 md:space-y-5"
            @submit.prevent="submitRegistration"
          >
            <div>
              <label
                for="email"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Your email</label
              >
              <input
                type="email"
                name="email"
                v-model="email"
                id="email"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="john.doe@example.com"
                required=""
              />
            </div>
            <div>
              <label
                for="username"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Your username</label
              >
              <input
                type="text"
                name="username"
                v-model="username"
                id="username"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Username"
                required=""
              />
            </div>
            <div>
              <label
                for="password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Password</label
              >
              <input
                type="password"
                name="password1"
                v-model="password1"
                id="password1"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required=""
              />
            </div>
            <div>
              <label
                for="password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Confirm Password</label
              >
              <input
                type="password"
                name="password2"
                v-model="password2"
                id="password2"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required=""
              />
            </div>
            <div v-if="resetSuccess" class="flex items-center justify-between">
              <div>
                <p class="text-green-500">Account activation email was sent.</p>
                <p v-if="alreadyVerified" class="text-red-600">
                  This account has already been verified
                </p>
                <p
                  v-else
                  @click="resendActivationEmail"
                  class="text-green-500 underline cursor-pointer"
                >
                  Send activation link again
                </p>
              </div>
            </div>
            <div
              v-else-if="resetSuccess === false"
              class="flex items-center justify-between"
            >
              <div class="flex items-start text-red-600">
                Registration failed
              </div>
            </div>
            <button
              @click="submitRegistration"
              class="w-full text-white bg-blue-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
            >
              Sign up
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Already have an account?
              <router-link
                class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                :to="{ name: 'login' }"
                >Sign in</router-link
              >
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
