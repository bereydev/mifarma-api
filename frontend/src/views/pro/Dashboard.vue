<template>
  <form @submit.prevent="onSubmit">
    <h1>Enter your verification number</h1>
    <input type="text" />
    <Button type="submit">Login</Button>
    <p>{{ $store.state.currentUser.first_name }}</p>
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
  async created() {
    await this.$store.dispatch("updateCurrentUser");
    await this.$store.dispatch("updatePharmacy");
    await this.$store.dispatch("updateEmployees");
    await this.$store.dispatch("updateCustomers");
  },
};
</script>
