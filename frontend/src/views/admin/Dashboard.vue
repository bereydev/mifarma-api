<template>
  <div class="pannels">
    <owner-list :owners="owners"></owner-list>
    <div class="data">
      <h1>Datos</h1>
      <span><b>Usuarios: </b>42069</span>
      <span><b>Farmacias verificadas: </b>420</span>
    </div>
  </div>
</template>

<script>
import OwnerList from "@/components/OwnerList";

export default {
  name: "DashboardAdmin",
  components: {
    OwnerList,
  },
  computed: {
    owners() {
      return this.$store.state.unverifiedOwners;
    },
  },
  methods: {},
  async created() {
    await this.$store.dispatch("updateCurrentUser");
    await this.$store.dispatch("updateUnverifiedOwners");
    await this.$store.dispatch("updatePharmacies");
  },
};
</script>

<style  scoped>
.pannels {
  display: flex;
  flex-direction: row;
  padding: 1.5%;
  gap : 5%; 
}
.data {
  width: 20%;
  height: 20%;
  padding: 0.5em;
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  text-align: justify;
  border-radius: 20px;
}
h1 {
  font-size: 1.5em;
}
</style>
