<template>
  <div class="principal-pannel"> 
    <customer-history-list class="customer-history" :customers="oldCustomers"/>
    <customer-schedule-list class="customer-schedule" :customers="oldCustomers"/>
    <div class="pharma-pannel">
    <h1>Mi Farmacia</h1>
    <pharma-image-vue :pharmacy="pharmacy"></pharma-image-vue>
    <div class="btn-group">
      <router-link to="/customer/pharma-picker">
        <button-vue color="dark"> Catálogo </button-vue>
      </router-link>
      <router-link to="/customer/catalog">
        <button-vue style="position: absolute; bottom: 0; right: 0"
          >Actualizar datos
        </button-vue>
      </router-link>
      <pharma-contacts-vue :pharmacy="pharmacy"></pharma-contacts-vue>
      <pharma-schedule-vue :pharmacy="pharmacy"></pharma-schedule-vue>
    </div>
  </div>

  </div>
</template>

<script>
import CustomerHistoryList from "../../components/CustomerHistoryList.vue"
import CustomerScheduleList from "../../components/CustomerScheduleList.vue"

export default {
  name: "DashboardPro",
  components: {
    CustomerHistoryList,
    CustomerScheduleList, 
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

.pharma-pannel {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 1em;
  width: 35%;
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
