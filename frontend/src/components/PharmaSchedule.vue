<template>
  <div class="padding">
    <ul v-for="(value, name) in pharmacy.schedule" :key="name">
      <li>
        <b>{{ name }}</b> :
        {{ value.join(", ") }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "PharmaSchedule",
  props: ["pharmacy"],
};
</script>

<style lang="scss" scoped>

.padding{
  padding-left: 2.5em;
}

</style>