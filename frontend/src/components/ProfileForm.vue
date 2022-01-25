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
				v-model= "this.first_name"
				name="first_name"
				:placeholder= "this.user.first_name"
			/>
			<input
				class="text-field"
				type="text"
				v-model= "this.last_name"
				name="last_name"
				:placeholder= "this.user.last_name"
			/>
		</div>
		<input
			class="text-field"
			type="email"
			v-model= "this.email"
			name="email"
			:placeholder= "this.user.email"
		/>
		<input
			class="text-field"
			type="text"
			v-model= "this.address"
			name="address"
			:placeholder= "this.user.address"
		/>
		<div class="double-field">
			<input
				class="text-field"
				type="number"
				v-model= "this.postcode"
				name="postcode"
				:placeholder= "this.user.postcode"
			/>
			<input
				class="text-field"
				type="text"
				v-model= "this.city"
				name="city"
				:placeholder= "this.user.city"
			/>
		</div>

		<div style="padding-top: 1em">
			<Button size="medium" type="submit">Guardar cambios</Button>
		</div>
	</form>
</template>

<script>
	import axios from "axios";
	import Button from "./CustomButton.vue";

	export default {
		name: "ProfileForm",
		data() {
			return {
				first_name : "", 
                last_name : "", 
                email : "", 
                address: "",
                postcode : "", 
                city : "", 
                
                user : null, 
			};
		},
		components: {
			Button,
		},
		async created() {
			this.user = this.$store.state.currentUser;
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
