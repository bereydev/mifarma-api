
<template>
	<form @submit="onSubmit" class="register">
		<h1>Crear cuenta</h1>
		<div class="small-text">¿Ya tiene cuenta? Acceda aquí</div>
		<div>
			<i class="material-icons">person</i>
		</div>
		<div class="double-field">
			<input
				class="text-field"
				type="text"
				v-model="name"
				name="name"
				placeholder="Nombre"
			/>
			<input
				class="text-field"
				type="text"
				v-model="surname"
				name="surname"
				placeholder="Apellidos"
			/>
		</div>
		<input
			class="text-field"
			type="text"
			v-model="email"
			name="email"
			placeholder="email"
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
				v-model="postCode"
				name="postCode"
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

		<input type="submit" value="Confirmar" class="green-button" />
	</form>
</template>

<script>
	export default {
		name: "RegisterForm",
		data() {
			return {
				name: "",
				surname: "",
				email: "",
				address: "",
				postCode: "",
				city: "",
				password: "",
				confirmPassword: "",
			};
		},
		methods: {
			onSubmit(e) {
				e.preventDefault();
				if (this.password === this.confirmPassword) {
					const newUser = {
						name: this.name,
						surname: this.surname,
						email: this.email,
						address: this.address,
						postCode: this.postCode,
						city: this.city,
						password: this.password,
					};
					console.log(newUser);
				}
			},
		},
	};
</script>


<style scoped>
	input:-webkit-autofill,
	input:-webkit-autofill:hover,
	input:-webkit-autofill:focus,
	textarea:-webkit-autofill,
	textarea:-webkit-autofill:hover,
	textarea:-webkit-autofill:focus,
	select:-webkit-autofill,
	select:-webkit-autofill:hover,
	select:-webkit-autofill:focus {
		appearance: menulist-button;
		-webkit-text-fill-color: #b1b1b1 !important;
		-webkit-box-shadow: 0 0 0 30px white inset !important;
		box-shadow: 0 0 0 30px white inset !important;
		background-image: none !important;
		background-color: white !important;
		color: #b1b1b1 !important;
	}

	::placeholder {
		/* Chrome, Firefox, Opera, Safari 10.1+ */
		color: #b1b1b1;
		opacity: 1; /* Firefox */
	}

	:-ms-input-placeholder {
		/* Internet Explorer 10-11 */
		color: #b1b1b1;
	}

	::-ms-input-placeholder {
		/* Microsoft Edge */
		color: #b1b1b1;
	}

	/* ALL OF THE ABOVE ARE COMPLICATED CSS RULES DEFINED TO OVERRIDE THE BROWSER PRESETS */

	input {
		border: none;
		color: #b1b1b1;
	}

	h1 {
		font-size: 2em;
		margin-block-start: 0px;
		margin-block-end: 0px;
	}
	.material-icons {
		color: #2e2931;
		border: 2px solid #adadad;
		border-radius: 100%;
		padding: 0.05em;
		font-size: 6em !important;
	}

	.small-text {
		padding: 0.75em 0em 1.5em 0em;
		font-size: 0.8em;
		color: #766b69;
		text-decoration: underline;
	}

	.register {
		margin: 2.5% 33% 10% 33%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 0.35em;
	}

	.double-field {
		box-sizing: border-box;
		padding: 0;
		margin: 0;
		display: flex;
		gap: 5%;
		width: 100%;
		align-items: center;
		justify-content: center;
	}

	.text-field {
		box-sizing: border-box;
		margin: 0.35em 0em 0.35em 0em;
		padding: 0.5em 1em 0.5em 1em;
		border-radius: 30px;
		background-color: white;
		border: 2px solid #adadad;
		justify-content: flex-start;
		text-align: start;
		width: 100%;
	}
	.text-field:focus {
		border: 2px solid #00dd7c;
		outline: none;
	}

	.text-field:hover {
		border: 2px solid #00dd7c;
		outline: none;
	}

	.green-button {
		display: flex;
		margin: 1em 0em 0.5em 0em;
		padding: 0.5em 1em 0.5em 1em;
		border-radius: 30px;
		justify-content: center;
		align-items: center;
		width: 50%;
		font-size: 1.25em;
		background-color: #00dd7c;
		color: #2e2931;
		box-shadow: 0px 3px 6px -3.5px gray;
	}
</style>