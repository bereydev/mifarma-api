<template>
	<form @submit.prevent="onSubmit" class="register">
		<div class="head">
			<h2>Crear cuenta</h2>
			<router-link class="small-text" to="/login"
				>¿Ya tiene cuenta? Acceda aquí</router-link
			>
			<div>
				<i class="material-icons">person</i>
			</div>
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
			v-model="address"
			name="address"
			placeholder="Dirección"
		/>
		<div class="double-field">
			<input
				class="text-field"
				type="number"
				v-model="postcode"
				name="postcode"
				placeholder="Código postal"
			/>
			<input
				class="text-field"
				type="text"
				v-model="city"
				name="city"
				placeholder="Ciudad"
			/>
		</div>
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
    <div style="padding-top:1em;">
      <Button  size="large" type="submit">Confirmar</Button>
    </div>
		
	</form>
</template>

<script>
	import axios from "axios";
	import Button from "./CustomButton.vue";

	export default {
		name: "RegisterForm",
		data() {
			return {
				first_name: "",
				last_name: "",
				email: "",
				address: "",
				postcode: "",
				city: "",
				password: "",
				confirmPassword: "",
			};
		},
		components: {
			Button,
		},
		methods: {
			async onSubmit() {
				try {
					await this.$store.dispatch("registerCustomer", {
						first_name: this.first_name,
						last_name: this.last_name,
						email: this.email,
						address: this.address,
						postcode: this.postcode,
						city: this.city,
						password: this.password,
					});
					this.$router.push("/customer/pharma-picker");
				} catch (error) {
					console.error(error);
				}
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

	.small-text {
		font-size: .9em;
    margin-bottom: 2em;

	}

  .head{
    display: flex;
    flex-direction: column;
    align-items: center;
		justify-content: center;
    margin: .5em 0 1em 0;
  }

	h2 {
		margin:0;
		padding: 0;
	}

	form {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 0.1em;
	}
</style>
