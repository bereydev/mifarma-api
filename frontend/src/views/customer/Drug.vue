<template>
	<body>
		<div class="drug-info">
			<img
				src="https://images.unsplash.com/photo-1587854692152-cbe660dbde88?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1769&q=80"
				alt="Foto Medicamento"
			/>
			<div class="text-div">
				<h1>{{ drug.name }}</h1>
				<h2>Descripción</h2>
				<p>
					{{ drug.description }}
				</p>
				<p>
					{{ drug.pharma_indications }}
				</p>
			</div>
			<div class="buy-div">
				<div style="display: flex; gap: 1em">
					<h2 class="price">{{ drug.price }} $</h2>
				</div>
				<button-vue size="medium" @click.prevent="addToCart"
					>Añadir al carrito
					<div class="material-icons" id="cart">shopping_cart</div></button-vue
				>
				<h2 class="price">ADD A COUNTER</h2>
			</div>
		</div>
	</body>
</template>

<script>
	import axios from "axios";
	import ButtonVue from "../../components/CustomButton.vue";

	export default {
		name: "Drug",
		components: {
			ButtonVue,
		},
		data() {
			return {
				//Add a load screen or something because this is ugly 
				//TODO 
				drug: {
					ean_code: "000",
					classification_number: "000",
					name: "Loading",
					description:
						"This is a test drug made by the developer team to see if everything looks like it should. If it doesn't well too bad. We'll have to work harder on the hlmnl/css and pray to the code gods",
					price: 0,
					pharma_indications:
						"Do not take this drug unless you're an admin and want to get lots of bugs",
					type_of_material: 0,
					magnitude: 10,
					laboratory: "Test Lab Inc",
					id: "212e5daf-b94c-4ea1-ac8f-e855a1a1057b",
					type: "drugs",
					image_filename: null,
				},
				amount: 1, //TODO with counter
			};
		},
		async created() {
			try {
				const response = await axios.get(
					"/products/ean/" + this.$route.query.ean
				);
				this.drug = response.data;
			} catch (error) {
				console.error(error);
			}
		},
		methods: {
			async addToCart() {
				try {
					await axios.post(
						"/shop/add-to-cart/" + this.drug.id + "?amount=" + this.amount
					);
					await this.$store.dispatch("updateCart");
				} catch (error) {
					console.error(error);
				}
			},
		},
	};
</script>

<style lang="scss" scoped>
	body {
		display: flex;
		flex-direction: column;
		padding: 3.5% 2.5% 2.5% 2.5%;
	}
	img {
		border-radius: 10%;
		object-fit: cover;
		width: 180px;
		height: 180px;
		margin-bottom: 0.25em;
		box-shadow: 0px 3px 3px 1.5px rgb(211, 211, 211);
	}
	span {
		width: 100px;
		white-space: pre-wrap;
	}
	.price {
		font-size: 1.5em;
	}
	.addButton {
		padding: 0.5em;
		justify-content: space-evenly;
		width: 100%;
	}
	.drug-info {
		display: flex;
		gap: 2em;
		width: 100%;
	}
	.buy-div {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		width: 20%;
		margin-left: auto;
		margin-right: auto;
	}
	.text-div {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		justify-content: flex-start;
		width: 50%;
	}
</style>
