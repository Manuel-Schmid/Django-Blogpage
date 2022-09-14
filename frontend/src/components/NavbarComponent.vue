<script lang="ts">
import { ref } from "vue";
import { useAuthStore } from "../store/auth";

export default {
  name: "NavbarComponent",

  setup() {
    const isDarkMode = ref(localStorage.theme === "dark");

    const toggleDarkMode = () => {
      if (localStorage.theme === "light") {
        localStorage.theme = "dark";
        isDarkMode.value = true;
      } else {
        localStorage.theme = "light";
        isDarkMode.value = false;
      }
      updateTheme();
    };

    const authStore = useAuthStore();

    return { toggleDarkMode, isDarkMode, authStore };
  },

  mounted() {
    updateTheme();
  },
};

function updateTheme() {
  if (
    localStorage.theme === "dark" ||
    (!("theme" in localStorage) &&
      window.matchMedia("(prefers-color-scheme: dark)").matches)
  ) {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }
}
</script>
<template>
  <header
    class="header fixed top-0 left-0 w-full shadow-md bg-white dark:bg-gray-900 dark:text-white"
  >
    <nav class="navbar h-full flex flex-row items-center">
      <label
        for="default-toggle"
        class="inline-flex relative items-center cursor-pointer ml-5"
      >
        <input
          type="checkbox"
          :checked="isDarkMode"
          id="default-toggle"
          class="sr-only peer"
          @click="toggleDarkMode()"
        />
        <div
          class="w-11 h-6 bg-slate-800 dark:bg-gray-200 dark:after:border-gray-300 after:bg-gray-50 :focus:outline-none peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-slate-300"
        ></div>
        <span
          class="ml-3 text-sm font-medium text-gray-900 dark:text-gray-300"
          >{{ isDarkMode ? "Light Mode" : "Dark Mode" }}</span
        >
      </label>
      <div class="w-auto flex flex-row absolute right-0 mr-5">
        <router-link class="nav-item" :to="{ name: 'posts' }">
          Posts
        </router-link>
        <router-link
          v-if="authStore.user"
          class="nav-item"
          :to="{ name: 'profile' }"
        >
          {{ authStore.user.username }}
        </router-link>
        <router-link v-else class="nav-item" :to="{ name: 'login' }">
          Login
        </router-link>
      </div>
    </nav>
  </header>
</template>

<style scoped>
.header {
  height: 9vh;
  z-index: 100;
}
.nav-item {
  transition: background-color 100ms;
  @apply pt-2 pr-5 pb-2 pl-5 mt-0 mr-1 mb-0 ml-1 leading-5 font-bold text-center hover:cursor-pointer hover:bg-zinc-200 dark:hover:bg-gray-700 dark:border-white;
}
.nav-item:hover {
  border-bottom: 1px solid;
  padding-bottom: calc(0.5rem - 1px);
}
</style>
