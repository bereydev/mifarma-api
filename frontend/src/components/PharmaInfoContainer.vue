<template>
  <div class="unverified-pharma">
    <owner-info :owner="owner"> </owner-info>
    <pharma-contacts-vue :pharmacy="pharmacy"></pharma-contacts-vue>
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
import Button from "./CustomButton.vue";
import PharmaContactsVue from './PharmaContacts.vue';

export default {
  name: "PharmaInfoContainer",
  components: {
    OwnerInfo,
    Button,
    PharmaContactsVue
  },
  props: ["pharmacy", "owner"],
  methods: {
    async verifyOwner() {
      try {
        await this.$store.dispatch("verifyOwner", this.owner.id);
      this.$emit("close");
      } catch (error) {
        console.error(error);
      }
      
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
  width: 100%;
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