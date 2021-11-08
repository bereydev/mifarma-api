<template>
  <router-link class="nav-tab" :to="link">
    <slot />
  </router-link>
</template>

<script>
export default {
  name: "NavTab",
  props: {
    link: { type: String, default: "/" },
  },
};
</script>

<style lang="scss" >
.nav-tab {
  color: #2e2931;
  align-self: center;
  justify-self: center;
  font-size: 1em;
  flex: 1 0 auto;
  margin: 0 0.5em 0 0.5em;
}
</style>