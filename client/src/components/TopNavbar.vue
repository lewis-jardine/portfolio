<template>
  <div id="navbarBase">
    <RouterLink to="/">Welcome</RouterLink>
    <RouterLink to="/ml">ML</RouterLink>
    <RouterLink to="/other">Other Projects</RouterLink>
    <RouterLink id="login" to="/login">Login</RouterLink>
  </div>
</template>

<style scoped>
#navbarBase {
  position: fixed;
  top: 0;
  width: 100%;
  background-color: black;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 4rem;
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
