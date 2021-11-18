<template>
  <body>
    <div class="panels">
      <div class="dashboard">
        <HomeSelector @selector-click="filterStatus" />
        <div class="scroll">
          <div
            style="margin: 0.15em 0 0.15em 0"
            v-for="order in filtered"
            :key="order.id"
          >
            <Order :order="order" />
          </div>
        </div>
      </div>
      <PharmaInfoHome />
    </div>
  </body>
</template>

<script>
import HomeSelector from "../../components/HomeSelector.vue";
import Order from "../../components/Order.vue";
import PharmaInfoHome from "../../components/PharmaInfoHome.vue";

export default {
  name: "Register",
  data() {
    return {
      orders: [],
      filtered: [],
    };
  },
  methods: {
    filterStatus(id) {
      if (id === -1) this.filtered = this.orders;
      else this.filtered = this.orders.filter((e) => e.status === id);
    },
    filterName(text) {
      text = text
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toLowerCase();
      if (text === "") this.filtered = this.orders;
      else
        this.filtered = this.orders.filter((o) =>
          o.product.name
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .toLowerCase()
            .includes(text)
        );
    },
  },
  components: {
    HomeSelector,
    Order,
    PharmaInfoHome,
  },
  async created() {
    await this.$store.dispatch("updatePharmacy");
    await this.$store.dispatch("updateCurrentUser");
  },
};
</script>

<style scoped>
.panels {
  display: flex;
  width: 100%;
  padding: 1.5% 1% 5% 1%;
  gap: 2.5%;
}

.dashboard {
  display: flex;
  flex-direction: column;
  width: 65%;
  gap: 0.75em;
}
</style>
