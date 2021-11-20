<template>
  <div class="register-pro">
    <RegisterFormPro />
  </div>
</template>

<script>
import RegisterFormPro from "../../components/RegisterFormPro.vue";

export default {
  name: "Register",
  components: {
    RegisterFormPro,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.register-pro {
  margin: auto;
  width: 40%;
}
</style>
