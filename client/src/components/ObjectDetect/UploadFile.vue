<template>
  <div class="flex-column-centered">
    <h2>Select an image to analyse</h2>
    <div id="form-upload">
      <v-file-input
        label="Upload image"
        v-model="chosenImages"
        variant="solo"
        prepend-icon="none"
        prepend-inner-icon="mdi-image"
        accept="image/*"
        show-size
        counter
      >
        <template v-slot:selection="{ fileNames }">
          <template v-for="fileName in fileNames" :key="fileName">
            <v-chip size="small" label color="primary" class="mr-2">
              {{ fileName }}
            </v-chip>
          </template>
        </template>
      </v-file-input>
      <v-btn
        :disabled="!chosenImages"
        append-icon="mdi-upload"
        @click="onUpload"
        >Upload</v-btn
      >
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const chosenImages = ref();
const imageObjects = ref();

function onUpload() {
  const formData = new FormData();
  formData.append("file", chosenImages.value[0]);
  fetch("http://localhost:8000/upload", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      imageObjects.value = data.objects;
      console.log(data);
    })
    .catch((err) => console.error(err));
}
</script>

<style scoped>
.v-input {
  width: 30rem;
  min-width: 50%;
}

#form-upload {
  display: flex;
  gap: 2rem;
}
#form-upload .v-btn {
  height: 3.2rem;
}
</style>
