<template>
  <div class="flex-column-centered">
    <h2>Results log</h2>
    <p v-for="detection in imageDetections" :key="detection">
      {{ detection }}
    </p>
  </div>
</template>

<script setup>
import { useStore } from "vuex";
import { computed } from "vue";

const store = useStore();

const imageDetections = computed(() => store.state.imageDetections);
</script>
