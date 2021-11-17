<template>
<div class="pannel">
  <div class="owner-list">
    <h1>Unverified owners</h1>
    <div v-for="owner in owners" :key="owner.public_id">
      <owner-item v-on:click="select(owner)" :owner="owner"></owner-item>
    </div>
  </div>
  <pharma-info-container @close="closeInfo" v-if="selectedPharmacy" :pharmacy="selectedPharmacy" :owner="selectedOwner"></pharma-info-container>
</div>

</template>

<script>
import OwnerItem from "./OwnerItem";
import PharmaInfoContainer from "./PharmaInfoContainer.vue";

export default {
  name: "OwnerList",
  props: ["owners"],
  components: {
    OwnerItem,
    PharmaInfoContainer,
  },
  data() {
    return {
      selectedPharmacy: null,
      selectedOwner: null,
    }
  },
  methods: {
    select(owner) {
      this.selectedOwner = owner
      this.selectedPharmacy = this.$store.getters.getInactivePharmacyById(owner.pharmacy_id)
    },
    closeInfo() {
      this.selectedPharmacy = null;
      this.selectedOwner = null;
    }
  },
};
</script>

<style scoped>
.pannel {
  display: flex;
  flex-direction: row;
  padding: none;
  gap : 1.5%; 
}
.owner-list {
  display: flex;
  flex-direction: column;
  gap: 0.5em;
  align-items: flex-start;
  width: 60%;
}
h1 {
  font-size: 1.5em;
  white-space: nowrap;
  padding: none;
  margin: none; 
  width: 100%; 
  text-align: start;
}
</style>
