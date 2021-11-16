<template>
  <div class="col">
    <pharma-image :pharmacy="pharmacy"></pharma-image>
    <span>{{pharmacy.name}}</span>
  </div>
</template>

<script>
import PharmaImage from './PharmaImage.vue';
export default {
  name: "PharmaCard",
  props: ["pharmacy"],
  components: {
    PharmaImage,
  }
};
</script>

<style scoped>
img {
  border-radius: 10%;
  object-fit: cover;
  width: 180px;
  height: 180px;
  margin-bottom: 0.5em;
  box-shadow: 0px 3px 3px 1.5px rgb(211, 211, 211);
}
span {
  width: 100px;
  white-space: pre-wrap;
  text-align: center;
}
.col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.05em;
}
</style>
