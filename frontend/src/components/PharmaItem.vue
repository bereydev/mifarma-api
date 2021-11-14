<template>
  <div class="pharma-item">
    <h2>{{ pharmacy.name }}</h2>
    <Button v-on:click="validatePharma">Validate {{ pharmacy.name }}</Button>
  </div>
</template>

<script>
import axios from "axios";
import Button from "./Button.vue";
export default {
  name: "PharmaItem",
  props: ["pharmacy"],
  components: {
    Button,
  },
  methods: {
    async validatePharma() {
      //Valiate the owner in the back
      const response = await axios.get(
        `/admin/pharmacy/${this.pharmacy.id}/owner`
      );
      const owner = response.data;
      console.log(owner);
      await axios.put(`/admin/verify-owner/${owner.id}`);
      //Display a modal with all the informations from the user
      //Display the token to send
    },
  },
};
</script>

<style></style>
