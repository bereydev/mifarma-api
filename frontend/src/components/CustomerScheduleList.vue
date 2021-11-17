<template>
<div class="pannel">
  <div class="customer-list">
    <h1>Citas</h1>
    <div v-for="customer in customers" :key="customer.public_id">
      <customer-schedule-widget v-on:click="select(customer)" :customer="customer"></customer-schedule-widget>
    </div>
  </div>
 </div>

</template>

<script>
import CustomerScheduleWidget from "./CustomerScheduleWidget.vue";

export default {
  name: "CustomerScheduleList",
  props: ["customers"],
  components: {
    CustomerScheduleWidget
  },
  
  
};
</script>

<style scoped>
.pannel {
  display: flex;
  flex-direction: row;
  padding: 1em .75em 2em .75em;
  background-color: #f5f5f5;
  border-radius: 20px;
}
.customer-list {
  display: flex;
  flex-direction: column;
  gap: .75em;
  align-items: flex-start;
  width: 60%;
}
h1 {
  font-size: 1.5em;
  white-space: nowrap;
  padding: 0 0 0 1em;
  margin: none; 
  width: 100%; 
  text-align: start;
}
</style>
