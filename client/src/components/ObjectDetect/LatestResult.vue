<template>
  <div id="result-container">
    <v-img max-height="300" :src="latestDetection.url" v-if="latestDetection" />
  </div>
</template>

<script setup>
import { useStore } from "vuex";
import { computed } from "vue";

const store = useStore();

const latestDetection = computed(() => store.state.imageDetections[0]);
</script>

<style scoped>
#result-container {
  margin: 2rem;
}
</style>
