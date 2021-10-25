<template>
  <div id="nav">
    <router-link to="/">Dashboard</router-link> |
    <router-link to="/profile">Profile</router-link> |
    <router-link to="/login">Login</router-link> |
    <router-link to="/password-recovery">Recover pswd</router-link> |
    <router-link to="/reset-password">Reset pswd</router-link> |
    <router-link to="/register">Register</router-link>
  </div>
  <router-view />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
