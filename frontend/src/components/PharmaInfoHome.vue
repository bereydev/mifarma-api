<template>
  <div class="pharma-pannel">
    <h2>Mi Farmacia</h2>
    <div class="pharma">
      <img
        src="https://images.pexels.com/photos/5699982/pexels-photo-5699982.jpeg?cs=srgb&dl=pexels-markus-winkler-5699982.jpg&fm=jpg"
        alt="Foto Farmacia"
      />
      <ul>
        <li>{{ $store.state.pharmacy.name }}</li>
        <li>{{ $store.state.pharmacy.address }}</li>
        <li>{{ $store.state.pharmacy.address2 }}</li>
        <li>{{ $store.state.pharmacy.city }}</li>
        <li>{{ $store.state.pharmacy.country }}</li>
        <li>{{ $store.state.pharmacy.email }}</li>
        <li>{{ $store.state.pharmacy.phone }}</li>
      </ul>
    </div>
    <div class="btn-group">
      <router-link to="/customer/pharma-picker">
        <button-vue color="dark">Cambiar de Farmacia</button-vue>
      </router-link>
      <router-link to="/customer/Catalog">
        <button-vue size="medium">Catálogo</button-vue>
      </router-link>
    </div>
    <p>
      {{ $store.state.pharmacy.description }}
    </p>
    <div class="schedule">
      <ul v-for="(value, name) in $store.state.pharmacy.schedule" :key="name">
        <li>
          <b>{{ name }}</b> :
          {{ value.join(", ") }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import ButtonVue from "./Button.vue";

export default {
  name: "PharmaInfoHome",
  components: {
    ButtonVue,
  },
};
</script>

<style lang="scss" scoped>
ul {
  list-style: none;
  margin-block-start: 0px;
  margin-block-end: 0px;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 0px;
}

.btn-group {
  display: flex;
  gap: 1em;
}

.pharma {
  display: flex;
  gap: 1em;
}

img {
  border-radius: 10%;
  object-fit: cover;
  width: 12em;
  height: 12em;
  margin-bottom: 0.5em;
}

.pharma-pannel {
  display: flex;
  flex-direction: column;
  gap: 0.5em;
}
</style>
