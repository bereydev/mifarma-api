<template>
	<form @submit.prevent="onSubmit" class="register">
		<div class="head">
			<h2>Mi Perfil</h2>
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
		<div class="checks">
			<div
				class="text-field"
				style="
					display: flex;
					justify-content: center;
					align-items: center;
					width: 25%;
					padding: 0.5em 0em 0.5em 0.6em;
				"
			>
				<input
					type="number"
					v-model="this.weight"
					name="weight"
					:placeholder="this.user.weight"
				/>
				<span>kilos</span>
			</div>

			<div
				class="text-field"
				style="
					display: flex;
					justify-content: center;
					align-items: center;
					width: 25%;
					padding: 0.5em 0em 0.5em 0.6em;
				"
			>
				<input
					type="number"
					v-model="this.height"
					name="height"
					:placeholder="this.user.height"
				/>
				<span>cm</span>
			</div>
			<span>Add diseases</span>
			<span>Add allergies</span>
			<div class="checkbox">
				<select v-model="this.user.alcoholic">
					<option value="true">Consumo alcohol con frecuencia</option>
					<option value="false">No consumo alcohol</option>
					<option value="null">No especificar mi consumo de alcohol</option>
				</select>
			</div>
			<div class="checkbox">
				<select v-model="this.user.gender">
					<option value="null" disabled>Especificar sexo</option>
					<option value="0">Hombre</option>
					<option value="1">Mujer</option>
					<option value="2">No binario</option>
					<option value="3">No especificar mi sexo</option>
				</select>
			</div>
			<div class="checkbox">
				<select v-model="this.user.smoker">
					<option value="true">Fumo con frencuencia</option>
					<option value="false">No fumo</option>
					<option value="null">No especificar si fumo</option>
				</select>
			</div>
			<div class="checkbox">
				<select v-model="this.user.pregnant">
					<option value="true">Embarazada</option>
					<option value="false">No embarazada</option>
					<option value="null">No especificar emabarazo</option>
				</select>
			</div>
			<div class="checkbox">
				<span>Fecha de nacimiento:</span>
				<input type="date" v-model="dateString" />
			</div>
		</div>

		<div style="padding-top: 1em">
			<Button size="medium" type="submit">Guardar cambios</Button>
		</div>
	</form>
</template>


<script>
	import Button from "./CustomButton.vue";

	import { computed, ref } from "vue";

	function completeZero(value) {
		return (value < 10 ? "0" : "") + value;
	}

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
				weight: "",
				height: "",
				user: null,
				dateString: null,
			};
		},
		components: {
			Button,
		},
		async created() {
			this.user = this.$store.state.currentUser;
			if (!this.user.phone) this.user.phone = "Número de teléfono";

			const now = new Date();

			this.dateString = ref(
				`${now.getFullYear()}-${completeZero(now.getMonth() + 1)}-${completeZero(
					now.getDate()
				)}`
			);
		},

		methods: {
			async onSubmit() {
				console.log(this.$store.currentUser.first_name);
			},
		},
	};
</script>

<style lang="scss" scoped>
	@import "@/assets/styles/colors.scss";
	.material-icons {
		color: #2e2931;
		border: 2px solid #adadad;
		border-radius: 100%;
		padding: 0.05em;
		font-size: 6em !important;
	}
	.register {
		padding-bottom: 5em;
	}
	.checkbox {
		margin: 0.35em 0em 0.35em 0em;
		padding: 0.6em 0.5em 0.6em 1em;
		border-radius: 30px;
		background-color: white;
		border: 2px solid $light-grey;
		justify-content: flex-start;
		text-align: start;
		width: 100%;
	}

	.checks {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.head {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin: 0.5em 0 1em 0;
	}

	h2 {
		margin: 0 0 0.5em 0;
		padding: 0;
	}

	select {
		border: none;
		color: #adadad;
		text-align: start;
		padding-right: 5em;
		width: 100%;
		outline: none !important;
	}
	span {
		padding-right: 1em;
		color: $light-grey;
		margin: 0;
	}
	.date-picker {
		display: flex;
		flex-direction: row;
		margin: 0.35em 0em 0.35em 0em;
		padding: 0.6em 1em 0.6em 1em;
		border-radius: 30px;
		background-color: white;
		border: 2px solid #adadad;
		justify-content: space-between;
		text-align: start;
		gap: 2em;
	}

	form {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 0.1em;
	}
</style>
