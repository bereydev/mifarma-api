<template>
	<div class="order">
		<div class="row-left">
			<img
				class="order-pic"
				src="https://images.pexels.com/photos/159211/headache-pain-pills-medication-159211.jpeg?cs=srgb&dl=pexels-pixabay-159211.jpg&fm=jpg"
				alt="Foto de perfil"
			/>
			<div class="order-name">{{ order.product.name }}</div>
		</div>
		<div class="itemCount">
			<button v-on:click="remove()" class="material-icons customButton">
				remove
			</button>
			<b>{{ order.amount }}</b>
			<button v-on:click="add()" class="material-icons customButton">add</button>
		</div>

		<div class="row-right">
			<div class="price">{{ order.product.price }} $</div>
			<button v-on:click="clear()" class="material-icons customButton">clear</button>
		</div>
	</div>
</template>

<script>
import axios from "axios";
	export default {
		props: ["order"],
		methods: {
			async remove() {
				try {
					await axios.delete(
						"/shop/delete-from-cart/" + this.order.id + "?amount=1"
					);
					await this.$store.dispatch("updateCart");
				} catch (error) {
					console.log(error);
				}
			},
      async clear() {
				try {
					await axios.delete(
						"/shop/delete-from-cart/" + this.order.id + "?amount=" + this.order.amount
					);
					await this.$store.dispatch("updateCart");
				} catch (error) {
					console.log(error);
				}
			},
			async add() {
				try {
					await axios.post(
						"/shop/add-to-cart/" + this.order.product_id + "?amount=1"
					);
					await this.$store.dispatch("updateCart");
				} catch (error) {
					console.log(error);
				}
			},
		},
	};
</script>

<style scoped>
	.order-name {
		font-size: 1em;
		width: 150%;
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
		width: 12.5%;
	}

	.order {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 0.5em 1em 0.5em 1em;
		background-color: white;
		border-radius: 25px;
		border: 1px solid #a6ffd8;
	}
	.order-pic {
		border-radius: 50%;
		width: 2.5em;
		height: 2.5em;
		border: 1px solid #2e2931;
	}

	.row-left {
		display: flex;
		gap: 1em;
		width: 50%;
		align-items: center;
		justify-content: flex-start;
	}
	.row-right {
		padding: 0.5em;
		display: flex;
		font-weight: bold;
		justify-content: space-between;
		align-items: center;
		width: 15%;
	}
</style>
