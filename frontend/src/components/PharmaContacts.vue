<template>
  <ul>
    <li>Nombre: {{ pharmacy.name }}</li>
    <li>Dirección:{{ pharmacy.address }}, {{ pharmacy.address2 }}</li>
    <li>Ciudad: {{ pharmacy.city }}</li>
    <li>País: {{ pharmacy.country }}</li>
    <li>Email: {{ pharmacy.email }}</li>
    <li>Phone: {{ pharmacy.phone }}</li>
  </ul>
</template>

<script>
export default {
  name: "PharmaContacts",
  props: ["pharmacy"],
};
</script>

<style>
</style>