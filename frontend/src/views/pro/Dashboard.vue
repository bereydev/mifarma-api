<template>
  <div class="principal-pannel"> 
    <customer-history-list class="customer-history" :customers="oldCustomers"/>
    <customer-schedule-list class="customer-schedule" :customers="oldCustomers"/>
    <pharma-pro class="pharma-info"/>

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
  gap: 1.5em; 
  padding: 1.5em;
}

.customer-history {
  width: 30%;
}
.customer-schedule {
  width: 30%;
}
.pharma-info {
  width: 40%;
}
</style>
