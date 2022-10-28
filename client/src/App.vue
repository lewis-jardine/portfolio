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
}
.flex-column-centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  right: 50%;
  transform: translate(50%);
}
.centered {
  position: relative;
  right: 50%;
  transform: translate(50%);
}
</style>
