<template>
  <div id="projects-container">
    <div class="flex-column-centered">
      <h2>Featured Projects</h2>
      <project-carousel></project-carousel>
    </div>
    <v-divider></v-divider>
    <div class="flex-column-centered">
      <h2>GitHub Projects</h2>
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

h2 {
  color: white;
  margin-bottom: 2rem;
  font-size: 2rem;
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

let projects = ref([]);

function getProjects() {
  fetch("https://api.github.com/users/lewis-jardine/repos")
    .then((response) => response.json())
    .then((data) => {
      console.log(data.created_at);
      projects.value = data;
      console.log(projects.value);
    });
}

onMounted(() => {
  getProjects();
});
</script>
