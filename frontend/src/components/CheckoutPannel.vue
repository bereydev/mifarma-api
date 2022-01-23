<template>
	<body>
		<h1>Resumen de pago</h1>
		<div class="sub-total">
			<div class="price-div">
				<h2>SUB TOTAL</h2>
				<h2>{{this.$store.getters.cartSubTotal}} €</h2>
			</div>
			<div class="price-div">
				<h2>IVA</h2>
				<h2>{{this.$store.getters.cartTaxes}} €</h2>
			</div>
		</div>
		<div class="price-div">
			<h2>TOTAL DE COMPRA</h2>
			<h2>{{this.$store.getters.cartTotal}} €</h2>
		</div>
		<div class="confirm-button">
			<button-vue size="small" @click.prevent="confirmOrder"
			>Confirmar pedido
			</button-vue
		>
		</div>
		
	</body>
</template>

<script>
	import axios from "axios";
	import ButtonVue from "./CustomButton.vue";
	export default {
		components: { ButtonVue },
		emits: ['orderConfirmed'], 
		props: ["order"],
		methods: {
			async confirmOrder() {
				try {
					await axios.post(
						"/shop/place-order"
					);
					this.$emit('orderConfirmed');
					console.log("emitted")
					await this.$store.dispatch("updateCart");
					await this.$store.dispatch("updateOrders");
				} catch (error) {
					console.log(error);
				}
			},
		},
	};
</script>

<style scoped>
	body {
		display: flex;
		flex-direction: column;
		border: 0.1em solid #a6ffd8;
		border-radius: 25px;
		padding: 0.5em 5em 1em 1.5em;
		max-height: 75%;
		height: 100%;
	}
	.sub-total {
		padding-bottom: 7.5em;
	}
	.confirm-button{
		display: flex;
		flex-direction: row;
		padding-top: 3em;
	}
	.price-div {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding-left: 1em;
	}

	h1 {
		font-size: 1.15em;
		font-weight: normal;
		padding-bottom: 1em;
	}
	h2 {
		font-size: 1em;
		font-weight: normal;
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
		width: 30%;
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
