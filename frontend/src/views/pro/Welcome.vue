<template>
  <div class="dashboard">
    <p>This is the welcome page for the pros</p>
    <router-link to="/pro/register">
      <Button id="register-pharma">Register a pharmacy</Button>
    </router-link>
  </div>
</template>

<script>
import Button from "../../components/Button.vue";

export default {
  components: {
    Button,
  },
};
</script>

<style lang="scss" scoped>
#register-pharma {
  position: fixed;
  bottom: 1em;
  right: 45%;
}
</style>
