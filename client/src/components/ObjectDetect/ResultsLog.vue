<template>
  <div class="flex-column-centered">
    <h2>Results log</h2>
    <v-card v-for="detection in imageDetections" :key="detection.url">
      <v-card-item>
        <v-card-title>Objects Detected</v-card-title>
        <v-card-subtitle>
          <v-icon>mdi-clock-time-four</v-icon>
          {{ detection.time }}
        </v-card-subtitle>
        <v-card-text>
          <v-row>
            <v-col cols="6" align-self="start">
              <v-list>
                <v-list-item
                  v-for="object in detection.objects"
                  :key="object.object + object.confidence"
                >
                  <template v-slot:prepend>
                    <v-chip :color="chipColour(object.confidence)">{{
                      object.confidence
                    }}</v-chip>
                  </template>
                  {{ object.object }}
                </v-list-item>
              </v-list>
            </v-col>
            <v-col cols="6" id="card-image-container">
              <v-img max-height="200" :src="detection.url" />
              <v-btn
                append-icon="mdi-download"
                :href="detection.url"
                target="_blank"
                color="primary"
                variant="tonal"
                >Download Image</v-btn
              >
            </v-col>
          </v-row>
        </v-card-text>
      </v-card-item>
    </v-card>
    <p v-for="detection in imageDetections" :key="detection">
      {{ imageDetections }}
    </p>
  </div>
</template>

<script setup>
import { useStore } from "vuex";
import { computed } from "vue";

const store = useStore();

const imageDetections = computed(() => store.state.imageDetections);

function chipColour(value) {
  if (value < 0.5) {
    return "red";
  } else if (value < 0.75) {
    return "orange";
  } else {
    return "green";
  }
}
</script>

<style scoped>
.v-card {
  margin: 1rem auto;
  max-width: 1000px;
  width: 100%;
  padding: 1rem;
}
.v-card a {
  margin: 2rem auto 0;
}
.v-card .v-list-item {
  padding: 0;
}
.v-card .v-chip {
  margin-right: 1rem;
}
#card-image-container {
  display: flex;
  flex-direction: column;
}
</style>
