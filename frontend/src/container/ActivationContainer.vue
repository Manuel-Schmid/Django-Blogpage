<template></template>

<script lang="ts">
import { useRoute } from "vue-router/dist/vue-router";
import router from "../router/router";
import { ref } from "vue";
import { useAuthStore } from "../store/auth";

export default {
  name: "ActivationContainer",
  setup() {
    const token = useRoute().params.token as string;
    const verificationSuccess = ref(undefined);

    const verifyToken = async () => {
      verificationSuccess.value = await useAuthStore().verifyAccount(token);
      await router.push({
        name: "login",
        query: { verified: verificationSuccess.value },
      });
    };

    verifyToken();
    return { verificationSuccess };
  },
};
</script>
