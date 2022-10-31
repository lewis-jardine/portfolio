<template>
  <div id="result-container">
    <v-row>
      <v-col cols="6">
        <img class="responsive-img" :src="latestImage" />
      </v-col>
      <v-col cols="6">
        <img class="responsive-img" :src="latestImage" />
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
import { useStore } from "vuex";
import { computed } from "vue";

const store = useStore();

const latestImage = computed(() => store.state.latestImage);

const latestDetection = computed(() => store.state.imageDetections);
console.log(latestDetection);
</script>

<style scoped>
#result-container {
  margin: 2rem;
}
</style>
