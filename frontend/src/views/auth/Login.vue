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
    <Button type="submit" style="width: 60%">Entrar</Button>
    <div class="small-text">¿Se olvidó la contraseña? Pinche aquí</div>
  </form>
</template>

<script>
import Button from "@/components/Button.vue";
import { Role } from "@/_helpers/Role";

export default {
  name: "Login",
  data() {
    return {
      password: "",
      username: "",
    };
  },
  components: {
    Button,
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
‚

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
