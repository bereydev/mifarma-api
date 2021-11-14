<template>
  <div class="order" :style="{ 'background-color': backgroundColor }">
    <div class="row-left">
      <img
        class="order-pic"
        src="https://images.pexels.com/photos/159211/headache-pain-pills-medication-159211.jpeg?cs=srgb&dl=pexels-pixabay-159211.jpg&fm=jpg"
        alt="Foto de perfil"
      />
      <div class="order-name">{{ this.order.product.name }}</div>
    </div>
    <div class="row-right">
      <div class="order-time">
        <span>{{ deliveryStatus }}</span>
        <i class="material-icons time-icon">{{ deliveryIcon }}</i>
      </div>
      <button class="material-icons dots">more_vert</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Order",
  props: {
    order: {
      name: "",
      status: "",
      delivery_date: "",
      order_date: "",
    },
  },
  computed: {
    backgroundColor() {
      if (this.order.status === 2) return "#A6FFD8";
      if (this.order.status === 1) return "#FFEE97";
      if (this.order.status === 3) return "#FFA192";
      else return "#ADADAD";
    },
    deliveryStatus() {
      if (this.order.status === 2) return "Disponible";
      if (this.order.status === 1 && this.order.delivery_date == null)
        return "Disponible próximamente";
      if (this.order.status === 1 && this.order.delivery_date != null)
        return "Disponible el " + this.order.delivery_date;
      if (this.order.status === 3) return "Indisponible por el momento";
      else return "Comprado el " + this.order.order_date;
    },
    deliveryIcon() {
      if (this.order.status === 2) return "event_available";
      if (this.order.status === 1) return "watch_later";
      if (this.order.status === 3) return "close";
      else return "hourglass_bottom";
    },
  },
};
</script>

<style scoped>
.order-name {
  font-size: 1.25em;
}
.order {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.5em 1em 0.5em 1em;
  border-radius: 25px;
}
.order-pic {
  border-radius: 50%;
  width: 2.5em;
  height: 2.5em;
  border: 1px solid #2e2931;
}

.dots {
  background-color: white;
  color: #2e2931;
  border-radius: 50%;
  font-size: 1.75em !important;
  padding: 0.3em;
  border: none;
}

.time-icon {
  color: #2e2931;
  font-size: 1.75em !important;
  border: none;
}

.order-time {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.6em;
  border-radius: 12px;
  background-color: white;
  gap: 2.5em;
}
.row-left {
  display: flex;
  gap: 1em;
  width: 30%;
  align-items: center;
  justify-content: flex-start;
}
.row-right {
  display: flex;
  gap: 0.15em;
  align-items: center;
  width: 60%;
  gap: 1em;
  justify-content: flex-end;
}
</style>
