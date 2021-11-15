<template>
  <div>
    <h1>List of all the new pharmacies</h1>
    <owner-list :owners="$store.state.unverifiedOwners"></owner-list>
    <p>Number of active pharmacies : {{ $store.getters.activePharmaciesCount }}</p>
    <p>Number of inactive pharmacies : {{ $store.getters.inactivePharmaciesCount }}</p>
  </div>
</template>

<script>
import OwnerList from "../../components/OwnerList";

export default {
  name: "DashboardAdmin",
  components: {
    OwnerList,
  },
  methods: {},
  async created() {
    this.$store.dispatch("updateCurrentUser");
    this.$store.dispatch("updateUnverifiedOwners");
    this.$store.dispatch("updatePharmacies");
  },
};
</script>

<style></style>
