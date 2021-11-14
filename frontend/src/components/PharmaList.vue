<template>
  <div>
    <div v-for="(pharmacy, index) in pharmacies" :key="index">
      <pharma-item :pharmacy="pharmacy"></pharma-item>
    </div>
  </div>
</template>

<script>
import PharmaItem from "./PharmaItem.vue";
export default {
  name: "PharmaList",
  props: ["pharmacies"],
  components: {
    PharmaItem,
  },
};
</script>

<style></style>
