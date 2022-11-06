<template>
  <v-list v-model:opened="open">
    <v-list-group value="basic">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props">Basic/ Tooling</v-list-item>
      </template>
      <v-list-item
        v-for="([icon, title, description, link], i) in basic"
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
    <v-list-group value="python">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props">Python</v-list-item>
      </template>
      <v-list-item
        v-for="([icon, title, description, link], i) in python"
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
    <v-list-group value="electronics">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props">Electronics</v-list-item>
      </template>
      <v-list-item
        v-for="([icon, title, description, link], i) in electronics"
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
    <v-list-group value="ml">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props">Machine Learning</v-list-item>
      </template>
      <v-list-item
        v-for="([icon, title, description, link], i) in ml"
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
    <v-list-group value="networking">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props">Networking</v-list-item>
      </template>
      <v-list-item
        v-for="([icon, title, description, link], i) in networking"
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
    <v-list-group value="frontend">
      <template v-slot:activator="{ props }">
        <v-list-item v-bind="props">Front-end Development</v-list-item>
      </template>
      <v-list-item
        v-for="([icon, title, description, link], i) in frontend"
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
  </v-list>
</template>

<script setup>
import { ref } from "vue";

const open = ref(["frontend"]);

const basic = ref([
  [
    "mdi-source-branch",
    "Git",
    "All projects published in GH repos using git CLI commands.",
    "https://github.com/lewis-jardine?tab=repositories",
  ],
  [
    "mdi-ubuntu",
    "Linux CLI",
    "Dev primarily on WSL, CLI only env so commands required.",
  ],
  [
    "mdi-download-lock",
    "SSH/ SCP",
    "Required to access, and transfer files on/ off RPi Zero, built in King Cobra",
    "https://dev.azure.com/project-waxwing/SAITInduction/_git/KingCobra?path=/hardware/pi/src",
  ],
  [
    "mdi-microsoft-azure-devops",
    "AzDo",
    "Collaborated with AzDo boards and repos to create King Cobra",
    "https://dev.azure.com/project-waxwing/SAITInduction/_wiki/wikis/SAITInduction.wiki/1620/Project",
  ],
  [
    "mdi-account-group",
    "Team Working Standards and Practices",
    "Worked with team throughout induction, utilising agile to deliver multiple projects.",
    "https://dev.azure.com/project-waxwing/SAITInduction/_wiki/wikis/SAITInduction.wiki/1492/SAIT-Induction",
  ],
  [
    "mdi-remote-desktop",
    "Remote dev containers",
    "Dev'd on WSL via VSCode's remote dev feature.",
  ],
  [
    "mdi-microsoft-visual-studio-code",
    "VSCode Extensions",
    "Extensively utilised prettier, data preview and drawIO extensions.",
  ],
  [
    "mdi-script-text-play",
    "BASH Script",
    "Created a mock wipe-device BASH script for RPi in King Cobra, triggered on tilt",
    "https://dev.azure.com/project-waxwing/SAITInduction/_git/KingCobra?path=/hardware/pi/src/tilt",
  ],
  [
    "mdi-docker",
    "Docker",
    "All induction projects have utilised docker from creation.",
    "https://dev.azure.com/project-waxwing/SAITInduction/_git/KingCobra?path=/docker-compose.yml",
  ],
]);

const python = ref([
  [
    "mdi-console",
    "OOP",
    "Objects used in various python projects. Eg. VideoPlayer in 'facial recognition test' project.",
    "https://github.com/lewis-jardine/facial-recognition-test/blob/main/detect_from_rtsp.py",
  ],
  [
    "mdi-language-python",
    "PEP8",
    "Use the 'Pylint' VSCode extension to ensure code adhers to PEP8",
    "https://code.visualstudio.com/docs/python/linting",
  ],
  [
    "mdi-folder-lock",
    "Venv/ Poetry",
    "All python packages are always installed inside an isolated venv.",
  ],
  [
    "mdi-puzzle",
    "Modularity",
    "Project components are placed in seperate functions/ classes and do not cause side effects",
    "https://github.com/lewis-jardine/portfolio/tree/master/api/ml",
  ],
  [
    "mdi-flask-outline",
    "Flask/ Fast API",
    "Fast API used to handle requests on this website.",
    "https://github.com/lewis-jardine/portfolio/tree/master/api",
  ],
  [
    "mdi-ship-wheel",
    "PIP Wheels",
    "Kamino functionality provided to King Cobra through .whl.",
    "https://dev.azure.com/project-waxwing/SAITInduction/_git/KingCobra?path=/api/Dockerfile",
  ],
  [
    "mdi-notebook",
    "Jupyter Notebooks",
    "Used in JHUB Module 4 submission.",
    "https://gist.github.com/lewis-jardine/0a9da409f550ba0f79a978fb9eccf9ca",
  ],
  [
    "mdi-code-array",
    "Data Structures",
    "Dictionarys, arrays, tuples etc all utilised in variety of projects.",
    "https://github.com/lewis-jardine/vehicle-detection/blob/main/yolov5_strongsort/tracker.py",
  ],
]);

const database = ref([
  ["mdi-search-web", "OpenSearch/ ElasticSearch"],
  [
    "mdi-database-search",
    "SQL",
    "PostGreSQL used in this website.",
    "https://github.com/lewis-jardine/portfolio/tree/master/api",
  ],
  ["mdi-leaf", "MongoDB (NoSQL)"],
]);

const electronics = ref([
  [
    "mdi-fruit-grapes",
    "Raspberry Pi",
    "Used RPi 4 and 0 for camera element of King Cobra, pushing images to API.",
    "https://dev.azure.com/project-waxwing/SAITInduction/_git/KingCobra?path=/README.md&_a=preview",
  ],
  [
    "mdi-raspberry-pi",
    "Microcontrollers",
    "Recreated RPi camera element of King Cobra on ESP32.",
    "https://dev.azure.com/project-waxwing/SAITInduction/_git/KingCobra?path=/hardware/esp32/ESP32%20Capture%20Cam",
  ],
  [
    "mdi-lightning-bolt",
    "Electronic Concepts (V, A, P etc.)",
    "Covered in Level 3 IT Tech apprenticeship.",
    "https://www.instituteforapprenticeships.org/apprenticeship-standards/unified-communications-technician-v1-0",
  ],
]);

const ml = ref([
  [
    "mdi-code-tags-check",
    "Coding Scheme Module 4/ 5",
    "Passed both modules.",
    "https://def-ideas.wazoku.com/user/69c7dd5f2d7042e1bac66a4a69c6eb84?tab=content",
  ],
  [
    "mdi-head-snowflake",
    "ONXX Models",
    "Used YoloV5, an ONXX model, in vehicle detection project.",
    "https://github.com/lewis-jardine/vehicle-detection/tree/main/yolov5_strongsort",
  ],
  [
    "mdi-alpha-t-box",
    "TensorFlow",
    "Keras ANN TF model used in module 4 assessment.",
    "https://gist.github.com/lewis-jardine/0a9da409f550ba0f79a978fb9eccf9ca",
  ],
  [
    "mdi-torch",
    "PyTorch",
    "Yolo models based on PyTorch, so used throughout vehicle detection project.",
    "https://github.com/lewis-jardine/vehicle-detection/blob/main/yolov5_strongsort/tracker.py",
  ],
  [
    "mdi-panda",
    "Numpy/ Pandas",
    "Crucial data structure libraries used in all ML projects.",
    "https://github.com/lewis-jardine/vehicle-detection/blob/main/simple_detector/detector.py",
  ],
  [
    "mdi-image-search",
    "OpenCV",
    "Important CV functions, used in all object detect projects.",
    "https://github.com/lewis-jardine/uav-metadata-extraction/blob/main/text_extractor.py",
  ],
  [
    "mdi-chart-timeline-variant-shimmer",
    "SciKit-Learn",
    "Regression/ classification functions used throughout module 4.",
    "https://gist.github.com/lewis-jardine/0a9da409f550ba0f79a978fb9eccf9ca",
  ],
]);

const networking = ref([
  [
    "mdi-lan-connect",
    "IP Stack and HTTP",
    "TCP/ IP model and HTTP covered in CCNA Networks module",
    "https://www.instituteforapprenticeships.org/apprenticeship-standards/unified-communications-technician-v1-0",
  ],
  [
    "mdi-vpn",
    "Wiregaurd",
    "Created Wiregaurd sever on RPi, connected phone to internet through it.",
    "",
  ],
  [
    "mdi-server-security",
    "Harden a Server",
    "Covered in cyber foundation pathway module 2.",
    "https://dle.ice.mod.gov.uk/course/view.php?id=22285",
  ],
]);

const frontend = ref([
  [
    "mdi-language-html5",
    "HTML",
    "Used inside <template> tag in this VueJS website.",
    "https://github.com/lewis-jardine/portfolio/blob/master/client/src/views/WelcomeView.vue",
  ],
  [
    "mdi-language-css3",
    "CSS",
    "Used inside <style> tag in this VueJS website.",
    "https://github.com/lewis-jardine/portfolio/blob/master/client/src/views/WelcomeView.vue",
  ],
  [
    "mdi-language-javascript",
    "JavaScript",
    "Used inside <script tag in this VueJS website.",
    "https://github.com/lewis-jardine/portfolio/blob/master/client/src/components/ObjectDetect/UploadFile.vue",
  ],
  [
    "mdi-vuejs",
    "VueJS 3",
    "This website is created with VueJS, using new V3 composition API.",
    "https://github.com/lewis-jardine/portfolio/blob/master/client/src/App.vue",
  ],
  [
    "mdi-vuetify",
    "Vuetify 3",
    "Common components in this website are created with vuetify 3.",
    "https://github.com/lewis-jardine/portfolio/blob/master/client/src/components/UI/LoadingSpinner.vue",
  ],
  ["mdi-map", "OpenLayers Mapping", "to implement", ""],
]);
</script>

<style scoped>
.v-list-group {
  --prepend-width: 10px;
}
</style>
