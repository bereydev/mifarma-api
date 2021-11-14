<template>
  <div>
    <div v-for="(owner, index) in owners" :key="index">
      <owner-item :owner="owner"></owner-item>
    </div>
  </div>
</template>

<script>
import OwnerItem from "./OwnerItem.vue";
export default {
  props: ["owners"],
  components: {
    OwnerItem,
  },
};
</script>

<style></style>
