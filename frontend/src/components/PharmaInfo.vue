<template>
  <div class="content">
    <pharma-image :pharmacy="pharmacy"></pharma-image>
    <div class="info">
      <div v-for="(value, name) in pharmacy.schedule" :key="name">
        <span
          ><b>{{ name }}</b> :
          {{ value.join(", ") }}
        </span>
      </div>
    </div>

    <div class="info">
      <span> <b>Nombre: </b>{{ pharmacy.name }}</span>
      <span>
        <b>Dirección: </b>{{ pharmacy.address }}, {{ pharmacy.address2 }}
      </span>
      <span><b>Ciudad: </b>{{ pharmacy.city }}</span>
      <span><b>País: </b>{{ pharmacy.state }}</span>
    </div>
  </div>
</template>

<script>
import PharmaImage from "./PharmaImage.vue";
export default {
  name: "PharmaInfo",
  props: ["pharmacy"],
  components: {
    PharmaImage,
  },
};
</script>

<style scoped>
img {
  border-radius: 10%;
  object-fit: cover;
  width: 12em;
  height: 12em;
}

p {
  width: 60%;
  margin: none;
  padding: none;
}

span {
  text-align: start;
}
.content {
  display: flex;
  gap: 1em;
}
.info {
  display: flex;
  flex-direction: column;
  text-align: left;
  justify-content: flex-start;
  gap: 0.25em;
  margin: 0 1em 0 1em;
}
</style>