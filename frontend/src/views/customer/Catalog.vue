<template>
  <div class="pharma-info">
    <pharma-image-vue :pharmacy="pharmacy"></pharma-image-vue>
    <pharma-contacts-vue :pharmacy="pharmacy"></pharma-contacts-vue>
    <pharma-schedule-vue :pharmacy="pharmacy"></pharma-schedule-vue>
  </div>

  <div class="offers">Ofertas</div>
  <div class="drugRow">
    <DrugWidget
      :drug="drug"
      v-for="drug in $store.state.catalog"
      :key="drug.ean"
    />
  </div>
  <div class="drugRow"></div>
  <div class="offers" style="background-color: #a6ffd8">Productos</div>

  <div class="drugRow">
    <DrugWidget
      :drug="drug"
      v-for="drug in $store.state.catalog"
      :key="drug.ean"
    />
  </div>
  <div class="drugRow">
    <DrugWidget
      :drug="drug"
      v-for="drug in $store.state.catalog"
      :key="drug.ean"
    />
  </div>
</template>

<script>
import DrugWidget from "@/components/DrugWidget.vue";
import PharmaContactsVue from "@/components/PharmaContacts.vue";
import PharmaImageVue from "@/components/PharmaImage.vue";
import PharmaScheduleVue from "@/components/PharmaSchedule.vue";

export default {
  name: "Catalog",
  data() {
    return {
      products: [],
    };
  },
  computed: {
    pharmacy() {
      return this.$store.state.pharmacy;
    },
  },

  components: {
    DrugWidget,
    PharmaContactsVue,
    PharmaImageVue,
    PharmaScheduleVue,
  },
  async created() {
    await this.$store.dispatch("updateCatalog", {filter:""});
  },
};
</script>

<style scoped>
.pharma-info {
  display: flex;
  flex-direction: row;
  gap: 1em;
  padding: 1.25em 2.5em .5em 2.5em ;
}
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
