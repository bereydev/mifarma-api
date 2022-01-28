<template>
	<form @submit.prevent="onSubmit" class="register">
		<div class="head">
			<h2>Mi perfil</h2>
			<div>
				<i class="material-icons">person</i>
			</div>
		</div>

		<div class="double-field">
			<input
				class="text-field"
				type="text"
				v-model="this.first_name"
				name="first_name"
				:placeholder="this.user.first_name"
			/>
			<input
				class="text-field"
				type="text"
				v-model="this.last_name"
				name="last_name"
				:placeholder="this.user.last_name"
			/>
		</div>
		<input
			class="text-field"
			type="email"
			v-model="this.email"
			name="email"
			:placeholder="this.user.email"
		/>
		<input
			class="text-field"
			type="text"
			v-model="this.address"
			name="address"
			:placeholder="this.user.address"
		/>
		<input
			class="text-field"
			type="number"
			v-model="this.phone"
			name="email"
			:placeholder="this.user.phone"
		/>
		<div class="double-field">
			<input
				class="text-field"
				type="number"
				v-model="this.postcode"
				name="postcode"
				:placeholder="this.user.postcode"
			/>
			<input
				class="text-field"
				type="text"
				v-model="this.city"
				name="city"
				:placeholder="this.user.city"
			/>
		</div>
		<div class="checkbox">
			<span>Consumo de alcohol : </span>
			<select v-model="this.user.alcohol">
				<option>Sí</option>
				<option>No</option>
				<option>No especificar</option>
			</select>
		</div>
		<div class="checkbox">
			<span>Sexo : </span>
			<select v-model="this.user.gender">
				<option>Hombre</option>
				<option>Mujer</option>
				<option>No binario</option>
				<option>No especificar</option>
			</select>
		</div>
		<div class="checkbox">
			<span>Fumador(a) : </span>
			<select v-model="this.user.smoker">
				<option>Sí</option>
				<option>No</option>
				<option>No especificar</option>
			</select>
		</div>
		<div class="checkbox">
			<span>Embarazada : </span>
			<select v-model="this.user.pregnant">
				<option>Sí</option>
				<option>No</option>
				<option>No especificar</option>
			</select>
		</div>

		<div style="padding-top: 1em">
			<Button size="medium" type="submit">Guardar cambios</Button>
		</div>
	</form>
</template>


<script>
	import Button from "./CustomButton.vue";

	export default {
		name: "ProfileForm",
		data() {
			return {
				first_name: "",
				last_name: "",
				email: "",
				address: "",
				postcode: "",
				city: "",
				phone: "",
				user: null,
			};
		},
		components: {
			Button,
		},
		async created() {
			this.user = this.$store.state.currentUser;
			if (!this.user.alcohol) this.user.alcohol = "No especificar";
			if (!this.user.gender) this.user.gender = "No especificar";
			if (!this.user.smoker) this.user.smoker = "No especificar";
		},
		methods: {
			async onSubmit() {
				console.log(this.$store.currentUser.first_name);
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
	.checkbox {
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.head {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin: 0.5em 0 1em 0;
	}

	h2 {
		margin: 0;
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
