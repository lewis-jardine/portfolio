<template>
  <v-progress-circular
    :size="75"
    :width="7"
    indeterminate
    color="primary"
    v-if="loading"
  ></v-progress-circular>
</template>

<script setup>
import { defineProps } from "vue";

// eslint-disable-next-line
const props = defineProps({
  loading: Boolean,
});
</script>

<style scoped>
.v-progress-circular {
  margin-top: 2rem;
}
</style>
