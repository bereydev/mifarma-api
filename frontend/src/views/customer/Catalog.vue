<template>
  <CatalogPharmaInfo />
  <div class="offers">Ofertas</div>
  <div class="drugRow"></div>
  <div class="offers" style="background-color: #a6ffd8">Ofertas</div>
  <div class="drugRow">
    <DrugWidget
      v-for="i in [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
      ]"
      :key="i"
    />
  </div>
  <div class="drugRow">
    <DrugWidget
      v-for="i in [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
      ]"
      :key="i"
    />
  </div>
  <div class="drugRow">
    <DrugWidget
      v-for="i in [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
      ]"
      :key="i"
    />
  </div>
</template>

<script>
import CatalogPharmaInfo from "../../components/CatalogPharmaInfo.vue";
import DrugWidget from "../../components/DrugWidget.vue";
import axios from "axios";

export default {
  name: "Catalog",
  data() {
    return {
      products: [],
    };
  },
  methods: {
    filterName(text) {
      console.log(text);
    },
  },
  components: {
    CatalogPharmaInfo,
    DrugWidget,
  },
  async created() {
    const response = await axios.get("shop/catalog");
    this.products = response.data;
    console.log(response.data);
    return null;
  },
};
</script>

<style scoped>
.offers {
  display: flex;
  padding: 0.15em 0 0.15em 1em;
  border-radius: 20px;
  justify-items: flex-start;
  margin: 1em 0 1em 2.5%;
  background-color: #ffee97;
  width: 95%;
  font-size: 1.25em;
}

.drugRow {
  display: flex;
  margin: 1em 0 1em 3%;
  gap: 1em;
  flex-direction: row;
  overflow: auto;
}
</style>
