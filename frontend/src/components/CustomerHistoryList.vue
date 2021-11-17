<template>
<div class="pannel">
  <div class="customer-list">
    <h1>Historial de clientes</h1>
    <div v-for="customer in customers" :key="customer.public_id">
      <customer-widget v-on:click="select(customer)" :customer="customer"></customer-widget>
    </div>
  </div>
 </div>

</template>

<script>
import CustomerWidget from "./CustomerWidget.vue";

export default {
  name: "CustomerHistoryList",
  props: ["customers"],
  components: {
    CustomerWidget
  },
  
  
};
</script>

<style scoped>
.pannel {
  display: flex;
  flex-direction: row;
  padding: none;
}
.customer-list {
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
