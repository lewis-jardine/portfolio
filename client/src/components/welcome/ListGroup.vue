<template>
  <v-list-group value="database">
    <template v-slot:activator="{ props }">
      <v-list-item v-bind="props">Database</v-list-item>
    </template>
    <v-list-item
      v-for="([icon, title, description, link], i) in database"
      :prepend-icon="icon"
      :key="i"
      :title="title"
      :subtitle="description"
      :value="title"
      :height="60"
      :href="link"
      target="_blank"
      :active="false"
    >
    </v-list-item>
  </v-list-group>
</template>

<script setup></script>
