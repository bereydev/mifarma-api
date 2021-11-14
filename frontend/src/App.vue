<template>
  <div>
    <NavBar />
    <router-view />
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
  },
};
</script>

<style>
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
textarea:-webkit-autofill,
textarea:-webkit-autofill:hover,
textarea:-webkit-autofill:focus,
select:-webkit-autofill,
select:-webkit-autofill:hover,
select:-webkit-autofill:focus {
  appearance: menulist-button;
  -webkit-text-fill-color: #b1b1b1 !important;
  -webkit-box-shadow: 0 0 0 30px white inset !important;
  box-shadow: 0 0 0 30px white inset !important;
  background-image: none !important;
  background-color: white !important;
  color: #b1b1b1 !important;
}

::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: #b1b1b1;
  opacity: 1; /* Firefox */
}

:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: #b1b1b1;
}

::-ms-input-placeholder {
  /* Microsoft Edge */
  color: #b1b1b1;
}

/* ALL OF THE ABOVE ARE COMPLICATED CSS RULES DEFINED TO OVERRIDE THE BROWSER PRESETS */

* {
  font-family: Roboto;
  font-size: 1em;
  color: #2e2931;
  box-sizing: border-box;
}

span {
  white-space: nowrap;
}
p {
  text-align: start;
}

body {
  margin: 0 !important;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

h1 {
  font-size: 2em;
  margin-block-start: 0px;
  margin-block-end: 0px;
}

.small-text {
  padding: 0.75em 0em 1.5em 0em;
  font-size: 0.8em;
  color: #766b69;
  text-decoration: underline;
}

.double-field {
  padding: 0;
  margin: 0;
  display: flex;
  gap: 5%;
  width: 100%;
  align-items: center;
  justify-content: center;
}

.text-field {
  margin: 0.35em 0em 0.35em 0em;
  padding: 0.6em 1em 0.6em 1em;
  border-radius: 30px;
  background-color: white;
  border: 2px solid #adadad;
  justify-content: flex-start;
  text-align: start;
  width: 100%;
}
.text-field:focus {
  border: 2px solid #00dd7c;
  outline: none;
}

.text-field:hover {
  border: 2px solid #00dd7c;
  outline: none;
}

.green-button {
  display: flex;
  margin: 1em 0em 0.5em 0em;
  padding: 0.5em 1em 0.5em 1em;
  border-radius: 30px;
  justify-content: center;
  align-items: center;
  width: 50%;
  font-size: 1.25em;
  background-color: #00dd7c;
  color: #2e2931;
  box-shadow: 0px 3px 6px -3.5px gray;
  border: none;
}

a {
  text-decoration: none;
}

#nav {
  padding: 30px;
  position: absolute;
  right: 50%;
  bottom: 0;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
