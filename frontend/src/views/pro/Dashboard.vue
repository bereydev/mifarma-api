<template>
  <form @submit.prevent="onSubmit">
    <h1>Enter your verification number</h1>
    <input type="text" />
    <Button type="submit">Login</Button>
    <p>{{ $store.state.user.first_name }}</p>
    <font-awesome-icon icon="user" />
  </form>
</template>

<script>
import Button from "../../components/Button.vue";

export default {
  name: "DashboardPro",
  components: {
    Button,
  },
  created() {
    this.$store.dispatch("updateCurrentUser");
    this.$store.dispatch("updatePharmacy");
    this.$store.dispatch("updateEmployees");
    this.$store.dispatch("updateCustomers");
  },
};
</script>
