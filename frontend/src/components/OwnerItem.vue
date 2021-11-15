<template>
  <div class="owner-item">
    <h2 v-on:click="pharmacyById" >{{ owner.first_name }}</h2>
    <Button v-on:click="$store.dispatch('verifyOwner', owner.id)"
      >Validate {{ owner.first_name }}</Button
    >
  </div>
</template>

<script>
import Button from "./Button.vue";
export default {
  name: "PharmaItem",
  props: ["owner"],
  components: {
    Button,
  },
  methods: {
    pharmacyById() {
      return this.$store.getters.getInactivePharmacyById(this.owner.pharmacy_id);
    },
  },
};
</script>

<style></style>
