<script lang="ts">
import { ref } from "vue";

export default {
  name: "ResetEmailFormComponent",
  setup() {
    let emailSentSuccessfully = ref(false);
    const sendEmail = () => {
      //...
      emailSentSuccessfully.value = true;
    };
    return { emailSentSuccessfully, sendEmail };
  },
};
</script>

<template>
  <div class="reset-container h-[91vh]">
    <div class="w-full h-full flex justify-center items-center text-left">
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white text-center"
          >
            Which E-Mail should we send the reset link to?
          </h1>
          <form class="space-y-4 md:space-y-6" @submit.prevent="sendEmail">
            <div>
              <label
                for="email"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Your E-Mail</label
              >
              <input
                type="email"
                name="email"
                id="email"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="john.doe@example.com"
                required=""
              />
            </div>
            <div
              v-if="emailSentSuccessfully"
              class="flex items-center justify-between"
            >
              <div class="flex items-start text-green-500">
                E-Mail sent successfully.
              </div>
            </div>
            <button
              @click="sendEmail"
              class="w-full text-white bg-blue-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
            >
              Send Reset E-Mail
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.reset-container {
  margin-top: 9vh;
}
</style>
