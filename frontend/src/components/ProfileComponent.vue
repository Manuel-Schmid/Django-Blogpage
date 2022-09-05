<script lang="ts">
export default {
  name: "profileComponent",
  props: ["userData"],

  setup() {
    return {};
  },
};
</script>

<template>
  <div>
    <p>{{ userData }}</p>
  </div>
</template>

<style scoped></style>
