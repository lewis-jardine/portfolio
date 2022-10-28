<template>
  <v-table fixed-header height="300px">
    <thead>
      <tr>
        <th class="text-left">Name</th>
        <th class="text-left">priority</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="comp in comps" :key="comp.name">
        <td>{{ comp.name }}</td>
        <td>{{ comp.priority }}</td>
      </tr>
    </tbody>
  </v-table>
</template>

<script setup>
const comps = [
  {
    name: "Python",
    priority: 5,
  },
];
</script>
