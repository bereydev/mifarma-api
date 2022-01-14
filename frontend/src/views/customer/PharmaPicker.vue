<template>
  <body>
    <div class="indication">
      <span class="material-icons infoIcon center">info</span>
      Seleccione su farmacia de confianza, podrá modificar su selección más
      tarde en ajustes de cuenta
    </div>
    <div v-if="(selectedPharmacy != currentPharmacy) && selectedPharmacy!=null" class="longRow">
      <div class="row">
        <pharma-image-vue :pharmacy="selectedPharmacy"></pharma-image-vue>
        <pharma-contacts-vue :pharmacy="selectedPharmacy"></pharma-contacts-vue>
      </div>

      <button-vue v-on:click="pickPharmacy()"
        >Confirmar <span class="material-icons infoIcon">chevron_right</span>
      </button-vue>
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
import PharmaContactsVue from "@/components/PharmaContacts.vue";
import ButtonVue from "@/components/Button.vue";
import PharmaImageVue from "@/components/PharmaImage.vue";
export default {
  name: "Cart",
  data() {
    return {
      selectedPharmacy: null,
      currentPharmacy: this.$store.state.pharmacy,
    };
  },
  components: {
    PharmaWidgetVue,
    PharmaContactsVue,
    PharmaImageVue,
    ButtonVue,
  },
  computed: {
    pharmacies() {
      return this.$store.state.activePharmacies;
    },
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
.row {
  display: flex;
  flex-direction: row;
  gap: 1em;
}

.longRow {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding-right: 5em;
}

.center{
  align-self: center;
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
  font-size: 1em;
  padding: 1em;
  gap: 1em;
  justify-content: flex-start;
  align-items: center;
}

.infoIcon {
  font-size: 1.5em !important;
  align-self: center;
}
</style>
