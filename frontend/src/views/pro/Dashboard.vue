<template>
  <div class="principal-pannel"> 
    <customer-history-list :customers="oldCustomers"/>
    <customer-schedule-list :customers="oldCustomers"/>
    <pharma-pro/>

  </div>
</template>

<script>
import CustomerHistoryList from "../../components/CustomerHistoryList.vue"
import CustomerScheduleList from "../../components/CustomerScheduleList.vue"
import PharmaPro from "../../components/PharmaPro.vue"

export default {
  name: "DashboardPro",
  components: {
    CustomerHistoryList,
    CustomerScheduleList, 
    PharmaPro
  },
  computed: {
    oldCustomers() {
      return this.$store.state.customers;
    },
  },
  async created() {
    await this.$store.dispatch("updateCurrentUser");
    await this.$store.dispatch("updatePharmacy");
    await this.$store.dispatch("updateEmployees");
    await this.$store.dispatch("updateCustomers");
  },
};
</script>

<style scoped>
.principal-pannel{
  display: flex;
  gap: 1.5%; 
  padding: 1.5%;
}
</style>
