<template>
  <form @submit.prevent="onSubmit">
    <h2>Acceso</h2>
    <router-link to="/register"
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
    <button-vue type="submit"> Entrar </button-vue>
    <router-link to="/password-recovery">
        ¿Se olvidó la contraseña? Pinche aquí
    </router-link>
  </form>
</template>

<script>
import ButtonVue from "./Button.vue";
import { Role } from "@/_helpers/Role";

export default {
  components: {
    ButtonVue,
  },
  data() {
    return {
      password: "",
      username: "",
    };
  },
  methods: {
    async onSubmit() {
      try {
        await this.$store.dispatch("login", {
          username: this.username,
          password: this.password,
        });
        const currentUser = this.$store.state.currentUser;
        const role = currentUser.role.name;

        if (role === Role.Admin) {
          this.$router.push("/admin/dashboard");
        } else if (role === Role.Owner || role === Role.Employee) {
          if (!currentUser.pharmacy_id) {
            this.$router.push("/create-pharma");
          }
          this.$router.push("/pro/dashboard");
        } else if (role === Role.Customer) {
          if (!currentUser.pharmacy_id) {
            this.$router.push("/customer/pharma-picker");
          }
          this.$router.push("/customer/dashboard");
        } else {
          throw new Error("The current user has no compatible role");
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style lang="scss" scoped>

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.25em;
}
</style>