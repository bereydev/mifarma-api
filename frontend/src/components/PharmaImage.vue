<template>
  <img
    src="https://images.pexels.com/photos/5699982/pexels-photo-5699982.jpeg?cs=srgb&dl=pexels-markus-winkler-5699982.jpg&fm=jpg"
    alt="Foto Farmacia"
  />
</template>

<script>
export default {
  name: "PharmaImage",
  props: ["pharmacy"],
};
</script>

<style lang="scss" scoped>
img {
  border-radius: 10%;
  object-fit: cover;
  width: 12em;
  height: 12em;
}
</style>