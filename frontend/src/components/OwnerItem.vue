<template>
  <div class="owner-item">
    <div class="pic-name">
      <img
        class="user-pic"
        src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2960&q=80"
        alt="Foto usuario"
      />
      <span>{{ owner.first_name }} {{ owner.last_name }}</span>
    </div>

    <button class="material-icons chevron">chevron_right</button>
  </div>
</template>

<script>
export default {
  name: "PharmaItem",
  props: ["owner"],
};
</script>

<style scoped>
.owner-item {
  display: flex;
  gap: 5em;
  background-color: #f5f5f5;
  padding: 0.25em;
  justify-content: start;
  align-items: center;
  border-radius: 20px;
}
.pic-name {
  display: flex;
  gap: 1.5em;
  justify-content: start;
  align-items: center;
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
</style>
