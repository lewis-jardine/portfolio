<template>
  <div id="navbarBase">
    <RouterLink to="/">Welcome</RouterLink>
    <RouterLink to="/od">Object Detector</RouterLink>
    <RouterLink to="/projects">Other Projects</RouterLink>
    <div id="login">
      <v-avatar color="secondary" size="44">LJ</v-avatar>
      <RouterLink to="/login">Login</RouterLink>
    </div>
  </div>
</template>

<style scoped>
#navbarBase {
  position: fixed;
  top: 0;
  width: 100%;
  display: flex;
  background-image: linear-gradient(to right, #8d0780e6, #f09819);
  justify-content: center;
  align-items: center;
  height: 4rem;
  z-index: 1;
}
a {
  margin: 0 1rem;
  color: white;
  text-decoration: none;
}
.router-link-active {
  text-decoration: underline;
}

#login {
  position: absolute;
  right: 2rem;
}
</style>
