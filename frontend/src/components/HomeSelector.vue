<template>
  <div class="selector">
    <h1>Mis pedidos</h1>
    <div class="button-panel">
      <button
        @click="onClick(2)"
        :class="[
          selected == '2' ? 'selected' : '',
          'material-icons selectorIcon',
        ]"
      >
        event_available
      </button>
      <button
        @click="onClick(1)"
        :class="[
          selected == '1' ? 'selected' : '',
          'material-icons selectorIcon',
        ]"
      >
        watch_later
      </button>
      <button
        @click="onClick(3)"
        :class="[
          selected == '3' ? 'selected' : '',
          'material-icons selectorIcon',
        ]"
      >
        hourglass_bottom
      </button>
      <button
        @click="onClick(4)"
        :class="[
          selected == '4' ? 'selected' : '',
          'material-icons selectorIcon',
        ]"
      >
        close
      </button>
      
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeSelector",
  data() {
    return {
      selected: "-1",
    };
  },
  methods: {
    onClick(id) {
      if (this.selected === id) {
        this.selected = -1;
        this.$emit("selector-click", -1);
      } else {
        this.selected = id;
        this.$emit("selector-click", id);
      }
    },
  },
};
</script>

<style scoped>
button {
  border: none;
}
h1 {
  font-size: 1.5em;
  padding: 0;
  margin-block-start: 0px;
  margin-block-end: 0px;
}
.selectorIcon {
  background-color: white;
  color: #2e2931;
  border-radius: 50%;
  font-size: 1.5em !important;
  padding: 7.5%;
  box-shadow: 0px 3px 5px #c0c0c0;
}

.selected {
  background-color: #00dd7c;
  color: white;
}
.selector {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10%;
  width: 35%;
  padding: 0 0 1.5% 2.5%;
}
.button-panel {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 20%;
}
</style>
