<template>
<div class="pannels">
  <div class="owner-list">
    <h1>Unverified owners</h1>
    <div v-for="owner in owners" :key="owner.public_id">
      <owner-item v-on:click="select(owner)" :owner="owner"></owner-item>
    </div>
  </div>
  <unverified-pharma @close="closeInfo" v-if="selectedPharmacy" :pharmacy="selectedPharmacy" :owner="selectedOwner"></unverified-pharma>
</div>

</template>

<script>
import OwnerItem from "./OwnerItem";
import UnverifiedPharma from "./PharmaInfoContainer.vue";

export default {
  name: "OwnerList",
  props: ["owners"],
  components: {
    OwnerItem,
    UnverifiedPharma,
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

<style>
.pannels {
  display: flex;
  flex-direction: row;
  padding: 1.5% 2.5% 1.5% 2.5%;
  gap: 2%;
}
.owner-list {
  display: flex;
  flex-direction: column;
  gap: 0.5em;
  align-items: flex-start;
  width: 17%;
}
h1 {
  font-size: 1.5em;
}
</style>
