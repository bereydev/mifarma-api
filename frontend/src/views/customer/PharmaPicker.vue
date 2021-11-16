<template>
  <body>
    <div v-if="selectedPharmacy">
      <pharma-info-vue :pharmacy="selectedPharmacy"></pharma-info-vue>
      <button-vue v-if="pharmacyChanged" v-on:click="pickPharmacy()">Confimar</button-vue>
    </div>
    <div class="indication">
      <span class="material-icons-outlined infoIcon"> info </span>
      Seleccione su farmacia de confianza, podrá modificar su selección más
      tarde en ajustes de cuenta
    </div>
    <div class="pharmaRow">
      <pharma-widget-vue
        v-for="pharmacy in pharmacies"
        :key="pharmacy.public_id"
        :pharmacy="pharmacy"
        v-on:click="select(pharmacy)"
      ></pharma-widget-vue>
    </div>
  </body>
</template>

<script>
import PharmaWidgetVue from "@/components/PharmaCard.vue";
import PharmaInfoVue from "@/components/PharmaInfo.vue";
import ButtonVue from "@/components/Button.vue";
export default {
  name: "Cart",
  data() {
    return {
      selectedPharmacy: this.$store.state.pharmacy,
      currentPharmacy: this.$store.state.pharmacy,
    };
  },
  components: {
    PharmaWidgetVue,
    PharmaInfoVue,
    ButtonVue,
  },
  computed: {
    pharmacies() {
      return this.$store.state.activePharmacies;
    },
    pharmacyChanged() {
      return this.currentPharmacy.id !== this.selectedPharmacy.id;
    }
  },
  methods: {
    select(pharmacy) {
      this.selectedPharmacy = pharmacy;
    },
    async pickPharmacy() {
      await this.$store.dispatch("pickPharmacy", this.selectedPharmacy.id);
      this.$router.push("/customer/dashboard");
    },
  },
  async created() {
    await this.$store.dispatch("updateActivePharmacies");
  },
};
</script>

<style scoped>
body {
  display: flex;
  flex-direction: column;
  padding: 1% 2.5% 2.5% 2.5%;
}

#confirmButton {
  width: 15%;
  align-self: flex-end;
}

.pharmaRow {
  display: flex;
  margin: 1em 0 1em 0;
  gap: 2em;
  justify-content: center;
  align-items: center;
}
.indication {
  display: flex;
  border-radius: 20px;
  background-color: #e8e1dd;
  margin: 1em 0 1em 0;
  font-size: 1.15em;
  padding: 1em;
  gap: 1em;
  justify-content: flex-start;
  align-items: center;
}

.infoIcon {
  font-size: 1.5em !important;
}
</style>
