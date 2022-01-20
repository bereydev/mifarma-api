<template>
  <div>
    <form @submit.prevent="onSubmit">
      <h1>Crear pharma</h1>
      <input
        class="text-field"
        type="text"
        v-model="name"
        name="city"
        placeholder="Name"
      />
      <input
        class="text-field"
        type="text"
        v-model="address"
        name="city"
        placeholder="Adresse"
      />
      <input
        class="text-field"
        type="text"
        v-model="address2"
        name="city"
        placeholder="Adresse 1"
      />
      <input
        class="text-field"
        type="text"
        v-model="country"
        name="city"
        placeholder="Country"
      />
      <input
        class="text-field"
        type="text"
        v-model="city"
        name="city"
        placeholder="City"
      />
      <Button type="submit">Create</Button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import Button from "../../components/CustomButton.vue";

const DEFAULT_SCHEDULE = {
  Lunes: ["09:00-14:30", "17:30-21:00"],
  Martes: ["09:00-14:30", "17:30-21:00"],
  Miercoles: ["09:00-14:30", "17:30-21:00"],
  Jueves: ["09:00-14:30", "17:30-21:00"],
  Viernes: ["09:00-14:30", "17:30-21:00"],
  Sabado: ["09:00-14:30", "17:30-21:00"],
  Domingo: ["09:00-14:30", "17:30-21:00"],
};

export default {
  name: "CreatePharma",
  data() {
    return {
      name: "",
      address: "",
      address2: "",
      country: "",
      city: "",
      schedule: "",
    };
  },
  components: {
    Button,
  },
  methods: {
    async onSubmit() {
      try {
        await this.$store.dispatch('createPharmacy', {
          name: this.name,
          address: this.address,
          address2: this.address2,
          country: this.country,
          city: this.city,
          schedule: this.schedule,
        })
        this.$router.push("/pro/dashboard");
      } catch (error) {
        console.log(error)
      }
    },
  },
};
</script>

<style lang="scss">
form {
  margin: 2.5% 33% 10% 33%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.15em;
}
</style>
