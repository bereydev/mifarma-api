<template>
  <button style>{{content}}</button>
</template>

<script>

export default {
  name: Button,
  props: ['content', 'color'],
};
</script>

<style scoped>
button {
  padding: 0.5em 1em 0.5em 1em;
  background-color: #00dd7c;
  border-radius: 38px;
  color: #2e2931;
  justify-content: center;
  box-shadow: 0px 3px 6px -3.5px grey;
}
</style>
