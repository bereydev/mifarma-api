<template>
  <div class="customer-item">
    <div class="pic-name">
      <img
        class="user-pic"
        src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2960&q=80"
        alt="Foto usuario"
      />

      <span id="name">{{ customer.first_name }} {{ customer.last_name }}</span>
      <div class="date-time">
        <span>12/01/2024</span>
        <span>11:11</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CustomerScheduleWidget",
  props: ["customer"],
};
</script>

<style scoped>
.customer-item {
  display: flex;
  gap: 5em;
  background-color: white;
  padding: 1em;
  justify-content: start;
  align-items: center;
  border-radius: 20px;
  box-shadow: 0px 3px 3px 1px rgb(200, 200, 200);
}
.pic-name {
  display: flex;
  gap: 1.5em;
  justify-content: start;
  align-items: center;
}
#name {
  width: 200px;
  text-align: start;
}
.chevron {
  border: none;
  background-color: transparent;
}
.user-pic {
  border-radius: 50%;
  width: 2.5em;
  height: 2.5em;
  border: 1px solid white;
}
.date-time {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  text-align: start;
  width: 150px;
}
</style>
