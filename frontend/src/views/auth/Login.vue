<template>
  <div class="login">
    <login-form-vue />
  </div>
</template>

<script>
import LoginFormVue from "@/components/LoginForm.vue";

export default {
  name: "Login",
  components: {
    LoginFormVue,
  },
};
</script>

<style lang="scss" scoped>
.login {
  width: 30%;
  margin: auto;
}
</style>
