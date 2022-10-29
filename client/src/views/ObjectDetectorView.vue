<template>
  <div id="od-container">
    <upload-file></upload-file>
    <latest-result></latest-result>
    <results-log></results-log>
  </div>
</template>

<script setup>
import UploadFile from "@/components/ObjectDetect/UploadFile.vue";
import LatestResult from "@/components/ObjectDetect/LatestResult.vue";
import ResultsLog from "@/components/ObjectDetect/ResultsLog.vue";
</script>

<style scoped>
#od-container {
  margin: 2rem;
}
</style>
