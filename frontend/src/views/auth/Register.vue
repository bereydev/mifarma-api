<template>
  <div class="register-customer">
    <RegisterForm />
  </div>
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
.register-customer {
  margin: auto;
  width: 40%;
}
</style>
