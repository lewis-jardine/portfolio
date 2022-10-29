<template>
  <v-card>
    <v-card-item>
      <v-card-title> {{ project.name }} </v-card-title>
      <v-card-subtitle> {{ formattedDate }} </v-card-subtitle>
    </v-card-item>
    <v-card-text> {{ project.description }} </v-card-text>
    <v-card-actions>
      <v-btn
        append-icon="mdi-open-in-new"
        variant="outlined"
        :href="project.html_url"
        target="_blank"
        color="primary"
        >Go To Repo</v-btn
      >
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { defineProps, computed } from "vue";

// eslint-disable-next-line
const props = defineProps({
  project: {
    id: Number,
    created_at: String,
    description: String,
    html_url: String,
  },
});

const formattedDate = computed(() =>
  new Date(props.project.created_at).toLocaleDateString("en-GB")
);
</script>

<style scoped>
a {
  margin-left: 0.5rem;
  margin-bottom: 0.5rem;
}
</style>
