<template>
  <button :class="styles">
    <slot />
  </button>
</template>

<script>
export default {
  name: "Button",
  props: {
    color: { type: [String], default: "green" },
  },
  computed: {
    styles() {
      return `btn btn-${this.color}`;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/styles/colors.scss";

.btn {
  padding: 0.5em 2em 0.5em 2em;
  border-radius: 38px;
  border: none;
  justify-content: center;
  box-shadow: 0px 3px 6px -3.5px grey;
  font-size: 18px;
}

.btn-green {
  background-color: $accent-green;
  color: $black;
}

.btn-red {
  background-color: $accent-red;
  color: $black;
}

.btn-dark {
  background-color: $black;
  color: white;
}
</style>
