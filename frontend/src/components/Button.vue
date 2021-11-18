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
    size: { type: [String], default: "" },

  },
  computed: {
    styles() {
      return `btn ${this.size} btn-${this.color}`;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/styles/colors.scss";

.btn {
  padding: 0.5em 1em 0.5em 1em;
  border-radius: 38px;
  border: none;
  justify-content: center;
  box-shadow: 0px 3px 6px -3.5px grey;
  font-size: 18px;
}
.large{
  padding: 0.5em 5em 0.5em 5em;
}
.medium{
  padding: 0.5em 3em 0.5em 3em;
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
