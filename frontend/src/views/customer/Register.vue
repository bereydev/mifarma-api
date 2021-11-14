<template>
  <body>
    <RegisterForm />
  </body>
</template>

<script>
import RegisterForm from "../../components/RegisterForm.vue";

export default {
  name: "Register",
  components: {
    RegisterForm,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body {
  margin: 0;
}
</style>
