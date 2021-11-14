<template>
  <div>
    <h1>List of all the new pharmacies</h1>
    <owner-list :owners="$store.state.unverifiedOwners"></owner-list>
  </div>
</template>

<script>
import OwnerList from "../../components/OwnerList.vue"

export default {
  name: "DashboardAdmin",
  components: {
    OwnerList,
  },
  methods: {},
  async created() {
    this.$store.dispatch('updateUnverifiedOwners');
    console.log(this.$store.state.unverifiedOwners)
  },
};
</script>

<style></style>
