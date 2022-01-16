<template>
  <body>
    <div class="panels">
      <div class="dashboard">
        <h1>Mi carrito</h1>
        <div class="scroll">
          <div class="offers">Sin receta</div>
          <div
            style="margin: 0.15em 0 0.15em 0"
            v-for="order in this.$store.getters.nonPrescriptedDrugs"
            :key="order.id"
          >
            <Drug :order="order"/>
          </div>
          <div class="offers" style="background-color: #a6ffd8">
            Con receta
          </div>
          <div
            style="margin: 0.15em 0 0.15em 0"
            v-for="order in this.$store.getters.prescriptedDrugs"
            :key="order.id"
          >
            <Drug :order="order"/>
          </div>
        </div>
      </div>
      <div class="orderPannel"></div>
    </div>
  </body>
</template>

<script>
import Drug from "../../components/Drug.vue";

export default {
  name: "Cart",
  
  components: {
    Drug,
  },
  async created() {
    await this.$store.dispatch("updateCart");
    this.prescripted = this.$store.state.cart; 
    this.nonPrescripted = this.$store.state.cart; 
  },
};
</script>

<style scoped>
.scroll {
  display: flex;
  flex-direction: column;
  gap: 0.5em;
}
.panels {
  display: flex;
  width: 100%;
  padding: .5% 2.5% 5% 2.5%;
  gap: 2.5%;
  background-color: white;
}
body {
  background-color: white;
  height: 100vh;
}

.dashboard {
  display: flex;
  flex-direction: column;
  width: 65%;
  gap: 0;
}
h1 {
  align-self: flex-start;
}
.offers {
  display: flex;
  padding: 0.15em 0 0.15em 1em;
  border-radius: 20px;
  justify-items: flex-start;
  background-color: #e8e1dd;
  margin: 1em 0 0.5em 0;

  width: 100%;
  font-size: 1.25em;
}
</style>
