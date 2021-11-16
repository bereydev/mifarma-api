<template>
  <div class="unverified-pharma">
    <owner-info :owner="owner"> </owner-info>
    <pharma-info :pharmacy="pharmacy"></pharma-info>
    <p>
      {{ pharmacy.description }}
    </p>
    <div class="buttons">
      <Button color="red">Eliminar</Button>
      <Button v-on:click="verifyOwner" color="green">Validar</Button>
    </div>
  </div>
</template>

<script>
import OwnerInfo from "./OwnerInfo.vue";
import Button from "./Button.vue";
import PharmaInfo from "./PharmaInfo.vue";

export default {
  name: "PharmaInfoContainer",
  components: {
    PharmaInfo,
    OwnerInfo,
    Button,
  },
  props: ["pharmacy", "owner"],
  methods: {
    async verifyOwner() {
      this.$store.dispatch("verifyOwner", this.owner.id);
      this.$emit("close");
    },
  },
};
</script>

<style scoped>
.unverified-pharma {
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
  padding: 1% 1.5% 1% 1.5%;
  border-radius: 15px;
  gap: 0.5em;
  width: 60%;
}
.buttons {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

p {
  width: 80%;
}
</style>