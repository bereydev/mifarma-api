<template>
  <div class="panels">
    <div class="order-pannel">
      <HomeSelector @selector-click="filterStatus" />
      <div class="scroll">
        <div
          style="margin: 0.15em 0 0.15em 0"
          v-for="order in cart"
          :key="order.id"
        >
          <Order :order="order" />
        </div>
      </div>
    </div>
    <div class="pharmacy-pannel">
      <h2>Mi Farmacia</h2>
      <div class="pharma">
        <pharma-image-vue :pharmacy="pharmacy"></pharma-image-vue>
        <pharma-contacts-vue :pharmacy="pharmacy"></pharma-contacts-vue>
      </div>
      <div class="btn-group">
        <router-link to="/customer/pharma-picker">
          <button-vue color="dark">Cambiar de Farmacia</button-vue>
        </router-link>
        <router-link to="/customer/catalog">
          <button-vue >Acceder al catálogo</button-vue>
        </router-link>
      </div>
      <p v-if="pharmacy.description">
        {{ pharmacy.description }}
      </p>
      <pharma-schedule-vue :pharmacy="pharmacy"></pharma-schedule-vue>
    </div>
  </div>
</template>

<script>
import HomeSelector from "@/components/HomeSelector.vue";
import Order from "@/components/Order.vue";
import ButtonVue from "@/components/CustomButton.vue";
import PharmaContactsVue from "@/components/PharmaContacts.vue";
import PharmaImageVue from "@/components/PharmaImage.vue";
import PharmaScheduleVue from "@/components/PharmaSchedule.vue";

export default {
  name: "Register",
  data() {
    return {
      cart: [],
    };
  },
  computed: {
    pharmacy() {
      return this.$store.state.pharmacy
    }
  },
  methods: {
    filterStatus(id) {
      if (id === -1) this.cart = this.$store.state.orders;
      else this.cart = this.$store.state.orders.filter((e) => e.status === id);
    },
  },
  components: {
    HomeSelector,
    Order,
    ButtonVue,
    PharmaContactsVue,
    PharmaImageVue,
    PharmaScheduleVue,
  },
  async created() {
    await this.$store.dispatch("updatePharmacy");
    await this.$store.dispatch("updateCurrentUser");
    await this.$store.dispatch("updateOrders");
    this.cart = this.$store.state.orders;
  },
};
</script>

<style lang="scss" scoped>
.panels {
  display: flex;
  padding: 1em;
  gap: 1em;
}

h2{
  font-size: 1.5em;
  padding: 0;
  margin-block-start: 0px;
  margin-block-end: 0px;
}

.order-pannel {
  display: flex;
  flex-direction: column;
  width: 60%;
  gap: 0.5em;
}
.pharmacy-pannel {
  width: 40%;
  display: flex;
  flex-direction: column;
  gap: 1em;
}
.btn-group {
  display: flex;
  gap: 3em;
}

p{
  padding-right: 5em;
}

.pharma {
  display: flex;
  gap: 1em;
}


</style>
