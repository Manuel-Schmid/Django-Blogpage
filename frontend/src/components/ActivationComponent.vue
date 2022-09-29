<script lang="ts">
import { useRoute } from "vue-router/dist/vue-router";
import { ref } from "vue";
import { useAuthStore } from "../store/auth";

export default {
  name: "ActivationComponent",
  setup() {
    const token = useRoute().params.token as string;
    const verificationSuccess = ref(undefined);

    const verifyToken = async () => {
      verificationSuccess.value = await useAuthStore().verifyAccount(token);
    };

    verifyToken();
    return { verificationSuccess };
  },
};
</script>

<template>
  <div class="mt-[9vh] h-[91vh] dark:text-white">{{ verificationSuccess }}</div>
</template>

<style scoped></style>
