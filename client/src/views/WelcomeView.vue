<template>
  <div id="welcome-content">
    <div class="flex-column-centered" id="welcome">
      <h1>WELCOME</h1>
      <p>to my portfolio</p>
    </div>
    <div class="flex-column-centered" id="scroll">
      <h2>Scroll to see more</h2>
      <v-img
        :width="50"
        :src="require('../assets/down-arrow.svg')"
        alt="down arrow"
      />
    </div>
  </div>
  <div id="more-content">
    <p>More!</p>
  </div>
</template>

<style scoped>
.flex-column-centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: absolute;
  right: 50%;
  transform: translate(50%, -50%);
}

#welcome {
  top: 40%;
}
#welcome h1 {
  font-size: 4rem;
}
#welcome p {
  font-size: 2rem;
  font-weight: 350;
}

#scroll {
  top: 90%;
}
#scroll h2 {
  font-weight: 450;
}

#welcome-content {
  height: calc(100vh - 4rem);
  background-color: white;
}
#more-content {
  background-color: grey;
}
</style>
