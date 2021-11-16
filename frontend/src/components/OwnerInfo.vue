<template>
  <div class="pannel">
    <img
      class="user-pic"
      src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2960&q=80"
      alt="Foto usuario"
    />
    <div class="infos">
      <span><b>Nombre</b>: {{ owner.first_name }}</span>
      <span><b>Apellidos</b>: {{ owner.last_name }}</span>
      <span
        ><b>Número de identificación</b>: {{ owner.pharmacist_number }}</span
      >
      <span><b>Email: </b>{{ owner.email }}</span>
      <span><b>tlfo: </b>{{ owner.phone }}</span>
      <span><b>Documento de identidad</b>:LINK_TO_ADD</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "OwnerInfo",
  props: ["owner"],
};
</script>

<style scoped>
.user-pic {
  border-radius: 50%;
  width: 6em;
  height: 6em;
  border: 1px solid #2e2931;
}
.pannel {
  display: flex;
  flex-direction: row;
  gap: 1em;
  padding-bottom: 1em;
}
.infos {
  display: flex;
  flex-direction: column;
  gap: 0.25em;
  text-align: justify;
}
</style>