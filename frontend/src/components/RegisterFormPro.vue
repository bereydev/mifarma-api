<template>
  <form @submit.prevent="onSubmit" class="register">
    <h1>Crear cuenta</h1>
    <router-link id="login" to="/login" class="small-text"
      >¿Ya tiene cuenta? Acceda aquí</router-link
    >
    <div>
      <i class="material-icons">person</i>
    </div>
    <div class="double-field">
      <input
        class="text-field"
        type="text"
        v-model="first_name"
        name="first_name"
        placeholder="Nombre"
      />
      <input
        class="text-field"
        type="text"
        v-model="last_name"
        name="last_name"
        placeholder="Apellidos"
      />
    </div>
    <input
      class="text-field"
      type="email"
      v-model="email"
      name="email"
      placeholder="Email"
    />
    <input
      class="text-field"
      type="text"
      v-model="pharmacist_number"
      name="pharmacist_number"
      placeholder="Your pharmacist identification number"
    />
    <div class="double-field">
      <input
        class="text-field"
        type="password"
        v-model="password"
        name="password"
        placeholder="Contraseña"
      />
      <input
        class="text-field"
        type="password"
        v-model="confirmPassword"
        name="confirmPassword"
        placeholder="Confirmar contraseña"
      />
    </div>
    <input
      class="text-field"
      type="file"
      name="confirmPassword"
      placeholder="Confirmar contraseña"
    />

    <input type="submit" value="Confirmar" class="green-button" />
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: "RegisterForm",
  data() {
    return {
      first_name: "",
      last_name: "",
      email: "",
      pharmacist_number: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    async onSubmit() {

      await this.$store.dispatch("registerOwner", {
        first_name: this.first_name,
        last_name: this.last_name,
        pharmacist_number: this.pharmacist_number,
        email: this.email,
        password: this.password,
      });
      this.$router.push("/create-pharma");
    },
  },
};
</script>

<style scoped>
.material-icons {
  color: #2e2931;
  border: 2px solid #adadad;
  border-radius: 100%;
  padding: 0.05em;
  font-size: 6em !important;
}

.register {
  margin: 2.5% 33% 10% 33%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.15em;
}
</style>
