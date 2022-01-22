<template>
  <body>
    <div v-if="this.$store.getters.cartItemCount==0" class="center">
      <i class="material-icons icon" >shopping_cart</i>
      <span class="warning">Su carrito está vacío</span>
    </div>
     
    <div class="panels">
     
      <div class="dashboard">
        <h1 v-if="this.$store.getters.cartItemCount>0">Mi carrito</h1>
        <div class="scroll">
          <div v-if="this.$store.getters.prescriptedCount>0" class="offers">Sin receta</div>
          <div
            style="margin: 0.15em 0 0.15em 0"
            v-for="order in this.$store.getters.nonPrescriptedDrugs"
            :key="order.id"
          >
            <Drug :order="order"/>
          </div>
          <div v-if="this.$store.getters.nonPrescriptedCount>0" class="offers" style="background-color: #a6ffd8">
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
      <div v-if="this.$store.getters.cartItemCount>0" class="order-pannel">
        <checkout-pannel/>
      </div>
    </div>
  </body>
</template>

<script>
import CheckoutPannel from '@/components/CheckoutPannel.vue';
import Drug from "../../components/Drug.vue";

export default {
  name: "Cart",
  
  components: {
    Drug,
    CheckoutPannel, 
  },
  async created() {

    await this.$store.dispatch("updateCart");
    this.prescripted = this.$store.state.cart; 
    this.nonPrescripted = this.$store.state.cart; 
  },
};
</script>

<style scoped>

.order-pannel{
  padding-top: 3em;
  width: 30%;
}
.scroll {
  display: flex;
  flex-direction: column;
  gap: 0.5em;
}
.center{
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 75%;
  align-items: center;
  justify-content: center;
}
.warning{
  font-size: 1.5em;
   color: #00DD7C; 
}
.icon{
  
  font-size: 7.5em !important;
  color: #00DD7C !important;

}
.panels {
  display: flex;
  width: 100%;
  height: 100%;
  padding: 2.5% 2.5% 5% 2.5%;
  gap: 1%;
  background-color: white;
}
body {
  background-color: white;
  height: 100vh;
}

.dashboard {
  display: flex;
  flex-direction: column;
  width: 70%;
  gap: 0;
}
h1 {
  align-self: flex-start;
  font-size: 1.5em;
  margin: 0; 
  padding: 0;
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
