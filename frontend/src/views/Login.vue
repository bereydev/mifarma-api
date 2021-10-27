<template>
	<NavBarComponent :access="false" />
	<form class="login">
		<h1>Mi cuenta</h1>
    <router-link class="small-text" to="/register">¿No tiene cuenta? Regístrese aquí</router-link>
		<input
			class="text-field"
			type="email"
			v-model="email"
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
		<div class="green-button">Entrar</div>
		<div class="small-text">¿Se olvidó la contraseña? Pinche aquí</div>
	</form>
</template>

<script>
	import NavBarComponent from "../components/NavBarComponent.vue";

	export default {
		name: "Login",
		components: {
			NavBarComponent,
		},
		data() {
			return {
				email: "",
				password: "",
			};
		},
		methods: {
			onSubmit(e) {
				e.preventDefault();
				const newUser = {
					email: this.email,
					password: this.password,
				};
				console.log(newUser);
			},
		},
	};
</script>

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