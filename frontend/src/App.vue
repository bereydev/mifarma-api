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

<style lang="scss">
@import "@/assets/styles/colors.scss";
@import "@/assets/styles/fonts.scss";
@import "@/assets/styles/lists.scss";
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
  text-decoration: none;
}
html, body {
    padding:0;
    margin:0;
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

a, a:link, a:visited, a:focus, a:hover, a:active{
  text-decoration:none; 
  font-size: unset;
}

/* ALL OF THE ABOVE ARE COMPLICATED CSS RULES DEFINED TO OVERRIDE THE BROWSER PRESETS */

* {
  font-family: Roboto;
  font-size: 1em;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
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
</style>
