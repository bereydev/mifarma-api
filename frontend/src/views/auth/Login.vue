<template>
  <form @submit.prevent="onSubmit" class="login">
    <h1>Mi cuenta</h1>
    <router-link class="small-text" to="/register"
      >¿No tiene cuenta? Regístrese aquí</router-link
    >
    <input
      class="text-field"
      type="email"
      v-model="username"
      name="email"
      placeholder="Email"
    />
    <input
      class="text-field"
      type="password"
      v-model="password"
      name="password"
      placeholder="Contraseña"
    />
    <input type="submit" value="Entrar" class="green-button" />
    <div class="small-text">¿Se olvidó la contraseña? Pinche aquí</div>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      password: "",
      username: "",
    };
  },
  components: {},
  methods: {
    async onSubmit() {
      const params = new URLSearchParams();
      params.append("username", this.username);
      params.append("password", this.password);
      const response = await axios.post("login/access-token", params);
      localStorage.setItem("token", response.data.access_token);
      //Check if is Customer or pharmacist 
      //if(customer) => Check if has adopted a pharmacy 
      // Send to pharmacy picker page 
      // Send to dashboard 
      this.$router.push("/customer/dashboard");
    },
  },
};
</script>‚

<style scoped>
.text-field,
.green-button {
  width: 60%;
}

.login {
  margin: 10% 30% 0% 30%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.25em;
}
</style>