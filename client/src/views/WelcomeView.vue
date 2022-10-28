<template>
  <div id="welcome-content">
    <div class="flex-column-centered" id="welcome-message">
      <h1>WELCOME</h1>
      <p>to my portfolio</p>
    </div>
    <div class="flex-column-centered" id="scroll">
      <a href="#key-topics">
        <h2>Scroll to see more</h2>
      </a>
      <a href="#key-topics">
        <v-img
          :width="50"
          :src="require('../assets/down-arrow.svg')"
          alt="down arrow"
        />
      </a>
    </div>
  </div>
  <v-parallax
    id="key-topics"
    src="../assets/more-content-parallax.jpg"
    height="1000"
  >
    <div class="flex-column-centered" id="key-topics-container">
      <h2>Key Topics I've Learnt</h2>
      <div id="key-topics-content">
        <p>Sample text</p>
      </div>
    </div>
  </v-parallax>
  <div id="footer">
    <div class="flex-column-centered" id="footer-content">
      <router-link to="/od">
        <h2 class="flex-column-centered" id="footer-title">Click Here</h2>
      </router-link>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
#welcome-content {
  height: calc(100vh - 4rem);
}
#welcome-message {
  top: 30%;
  width: 80%;
  margin-left: 20%;
  background: transparent;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset,
    rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;
  color: white;
}
#welcome-message h1 {
  font-size: 4rem;
}
#welcome-message p {
  font-size: 2rem;
  font-weight: 350;
}

#scroll {
  top: 60%;
}
#scroll a {
  text-decoration: none;
  color: white;
}
#scroll h2 {
  font-weight: 450;
}

#key-topics-container {
  top: 10%;
  gap: 5rem;
}
#key-topics-container h2 {
  font-size: 2.75rem;
  color: white;
}
#key-topics-content {
  background-color: white;
  width: 50%;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: rgba(240, 46, 170, 0.4) 5px 5px, rgba(240, 46, 170, 0.3) 10px 10px,
    rgba(240, 46, 170, 0.2) 15px 15px, rgba(240, 46, 170, 0.1) 20px 20px,
    rgba(240, 46, 170, 0.05) 25px 25px;
}
#footer {
  height: 100vh;
}
#footer a {
  text-decoration: none;
  color: black;
}
#footer-content {
  top: 30%;
}
#footer-content h2 {
  font-size: 2rem;
}
</style>
