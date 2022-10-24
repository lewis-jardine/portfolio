<template>
  <v-app>
    <top-navbar></top-navbar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
import TopNavbar from "./components/TopNavbar.vue";
</script>

<style>
main {
  margin-top: 4rem;
}
</style>
