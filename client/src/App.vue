<template>
  <v-app>
    <top-navbar></top-navbar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
import TopNavbar from "./components/UI/TopNavbar.vue";
</script>

<style>
main {
  margin-top: 4rem;
  background-image: linear-gradient(to right, #8d0780e6, #f09819);
}
.flex-column-centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  right: 50%;
  transform: translate(50%);
  color: white;
}
.flex-column-centered h2 {
  margin-bottom: 2rem;
  font-size: 2rem;
}

.centered {
  position: relative;
  right: 50%;
  transform: translate(50%);
}
.v-counter {
  color: white;
}
</style>
