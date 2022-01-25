<template>
	<body>
		<div class="drug-info">
			<div class="image-price">
				<img
					src="https://images.unsplash.com/photo-1587854692152-cbe660dbde88?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1769&q=80"
					alt="Foto Medicamento"
				/>
				<div class="price">
					<p class="price-tag">{{ drug.price }}€</p>
					<p class="price-tag">-</p>
					<p class="price-tag">
						<s> {{ drug.price }} </s>€
					</p>
				</div>
			</div>

			<div class="text-div">
				<h1>{{ drug.name }}</h1>
				<h2>Descripción</h2>
				<p class="description">
					{{
						drug.description
							? drug.description
							: "Este medicamento o producto no tiene descripción"
					}}
				</p>
				<p class="warning">
					{{
						drug.pharma_indications
							? drug.pharma_indications
							: "Este medicamento o producto no tiene contra indicaciones o advertencias"
					}}
				</p>
			</div>
			<div class="buy-div">
				<div class="itemCount">
					<button v-on:click="remove()" class="material-icons customButton">
						remove
					</button>
					<b>{{ this.amount }}</b>
					<button v-on:click="add()" class="material-icons customButton">
						add
					</button>
				</div>
				<button-vue size="medium" @click.prevent="addToCart"
					>{{ buttonText }}
					<div v-bind:class="{ activeCart: isActive }" class="material-icons">
						shopping_cart
					</div>
				</button-vue>
			</div>
		</div>
		<div style="display: flex; flex-direction: column; padding-top: 3em">
			<p class="similar">Productos similares</p>
			<div class="drugRow">
				<DrugWidget
					:drug="drug"
					v-for="drug in $store.state.catalog"
					:key="drug.ean"
				/>
			</div>
			<div class="drugRow">
				<DrugWidget
					:drug="drug"
					v-for="drug in $store.state.catalog"
					:key="drug.ean"
				/>
			</div>
		</div>
	</body>
</template>

<script>
	import axios from "axios";
	import ButtonVue from "../../components/CustomButton.vue";
	import DrugWidget from "@/components/DrugWidget.vue";

	export default {
		name: "Drug",
		components: {
			ButtonVue,
			DrugWidget,
		},
		data() {
			return {
				//Add a load screen or something because this is ugly
				//TODO
				amount: 1,
				isActive: false,
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
				buttonText: "Añadir al carrito",
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
			async remove() {
				if (this.amount > 1) this.amount--;
			},
			async add() {
				this.amount++;
			},
			async addToCart() {
				try {
					await axios.post(
						"/shop/add-to-cart/" + this.drug.id + "?amount=" + this.amount
					);
					await this.$store.dispatch("updateCart");
					this.isActive = !this.isActive;
					setTimeout(() => {
						this.isActive = !this.isActive;
					}, 1500);
				} catch (error) {
					console.error(error);
				}
			},
		},
	};
</script>

<style lang="scss" scoped>
	@import "../../assets/styles/colors.scss";

	.drugRow {
		display: flex;
		margin: 1em 0 1em 0;
		gap: 1em;
		flex-direction: row;
		overflow: auto;
	}
	.similar {
		font-size: 1.25em;
		background-color: $green-light;

		display: flex;
		padding: 0.15em 0 0.15em 1em;
		border-radius: 20px;
		justify-items: flex-start;
		margin: 0;
	}

	body {
		display: flex;
		flex-direction: column;
		padding: 3.5% 2.5% 2.5% 2.5%;
	}
	.activeCart {
		transform: translateX(100px);
		color: white !important;
		transition: all 1s;
	}
	.customButton {
		padding: 0;
		background-color: white;
		border: none;
		color: #afafaf;
		font-size: 1.75em !important;
		justify-self: center;
		align-self: center;
		border-radius: 50%;
		cursor: pointer;
	}
	.itemCount {
		display: flex;
		justify-content: space-between;
		align-items: center;
		width: 50%;
		margin: 0 0 0.75em 0;
	}
	.image-price {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		gap: 0.75em;
	}
	h1 {
		font-size: 1.85em;
		padding: 0;
		margin: 0;
	}
	h2 {
		font-size: 1.35em;
		padding: 0;
		margin: 0;
		color: #adadad;
	}
	.description {
		font-size: 1em;
		padding: 0 0 1em 0.25em;
	}
	.warning {
		font-size: 1em;
		margin: 0 0 1em 0.25em;
		color: #ffa192;
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
		display: flex;
		align-items: center;
		gap: 1em;
	}
	.price-tag {
		font-size: 1.5em;
		color: $black;
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
