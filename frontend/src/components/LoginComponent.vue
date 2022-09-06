<script lang="ts">
import { ref } from "vue";
import { useAuthStore } from "../store/auth";

export default {
  name: "LoginComponent",

  setup() {
    let username = ref("");
    let password = ref("");

    let authStore = useAuthStore();

    const submitLogin = () => {
      authStore.fetchRefreshToken(username.value, password.value);
    };

    return { username, password, submitLogin };
  },
};
</script>

<template>
  <div class="login-container h-[91vh]">
    <div class="w-full h-full flex justify-center items-center text-left">
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white text-center"
          >
            Sign in to your account
          </h1>
          <form class="space-y-4 md:space-y-6" @submit.prevent="submitLogin">
            <div>
              <label
                for="email"
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
                name="password"
                v-model="password"
                id="password"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required=""
              />
            </div>
            <!--            <div class="flex items-center justify-between">-->
            <!--              <div class="flex items-start"></div>-->
            <!--              <a-->
            <!--                href="#"-->
            <!--                class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500"-->
            <!--                >Forgot password?</a-->
            <!--              >-->
            <!--            </div>-->
            <button
              @click="submitLogin"
              class="w-full text-white bg-blue-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
            >
              Sign in
            </button>
            <!--            <p class="text-sm font-light text-gray-500 dark:text-gray-400">-->
            <!--              Don’t have an account yet?-->
            <!--              <a-->
            <!--                href="#"-->
            <!--                class="font-medium text-primary-600 hover:underline dark:text-primary-500"-->
            <!--                >Sign up</a-->
            <!--              >-->
            <!--            </p>-->
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  margin-top: 9vh;
}
.label {
  @apply text-lg font-bold;
}
</style>
