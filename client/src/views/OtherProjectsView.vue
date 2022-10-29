<template>
  <div id="projects-container">
    <div class="flex-column-centered">
      <h2>Featured Projects</h2>
      <project-carousel></project-carousel>
    </div>
    <v-divider></v-divider>
    <div class="flex-column-centered">
      <h2>GitHub Projects</h2>
      <loading-spinner :loading="loading"></loading-spinner>
      <v-row>
        <v-col
          cols="4"
          v-for="project in projects.slice().reverse()"
          :key="project.id"
        >
          <project-card :project="project"></project-card>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<style scoped>
#projects-container {
  margin: 2rem;
}

hr {
  margin: 3rem 0;
  border-top: 2px solid white;
}
</style>

<script setup>
import { onMounted, ref } from "vue";
import ProjectCard from "../components/ProjectCard.vue";
import ProjectCarousel from "../components/ProjectCarousel";

const projects = ref([]);
const loading = ref(false);

function getProjects() {
  loading.value = true;
  fetch("https://api.github.com/users/lewis-jardine/repos")
    .then((response) => response.json())
    .then((data) => {
      console.log(data.created_at);
      projects.value = data;
      loading.value = false;
    });
}

onMounted(() => {
  getProjects();
});
</script>
