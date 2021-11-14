<template>
  <div>
    <h1>List of all the new pharmacies</h1>
    <pharma-list :pharmacies="pharmacies"></pharma-list>
  </div>
</template>

<script>
import axios from "axios";
import PharmaList from "../../components/PharmaList.vue";

export default {
  name: "DashboardAdmin",
  data() {
    return {
      pharmacies: [],
    };
  },
  components: {
    PharmaList,
  },
  methods: {},
  async created() {
    const response = await axios.get("admin/pharmacies/inactive");
    console.log(response.data);
    this.pharmacies = response.data;
  },
};
</script>

<style></style>
