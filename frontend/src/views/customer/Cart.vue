<template>
	<body>
		<div class="panels">
			<div class="dashboard">
				<h1>Mi carrito</h1>
				<div class="scroll">
					<div class="offers">Sin receta</div>
					<div
						style="margin: 0.15em 0 0.15em 0"
						v-for="order in filtered"
						:key="order.id"
					>
						<Drug :drug="order" :color="red" :isCool="true" />
					</div>
					<div class="offers" style="background-color: #a6ffd8">
						Medicamento con receta
					</div>
					<div
						style="margin: 0.15em 0 0.15em 0"
						v-for="order in filtered"
						:key="order.id"
					>
						<Drug :drug="order" :color="red" :isCool="false" />
					</div>
				</div>
			</div>
			<div class="orderPannel"></div>
		</div>
	</body>
</template>

<script>
	import Drug from "../../components/Drug.vue";

	export default {
		name: "Cart",
		data() {
			return {
				products: [],
				filtered: [],
			};
		},
		methods: {
			filterName(text) {
				text = text
					.normalize("NFD")
					.replace(/[\u0300-\u036f]/g, "")
					.toLowerCase();
				if (text === "") this.filtered = this.products;
				else
					this.filtered = this.products.filter((o) =>
						o.product.name
							.normalize("NFD")
							.replace(/[\u0300-\u036f]/g, "")
							.toLowerCase()
							.includes(text)
					);
			},
		},
		components: {
			Drug,
		},
		async created() {
			//TODO
		},
	};
</script>


<style scoped>
	.scroll {
		display: flex;
		flex-direction: column;
		gap: 0.5em;
	}
	.panels {
		display: flex;
		width: 100%;
		padding: 1.5% 2.5% 5% 2.5%;
		gap: 2.5%;
		background-color: #f5f5f5;
	}
	body {
		background-color: #f5f5f5;
		height: 100vh;
	}

	.dashboard {
		display: flex;
		flex-direction: column;
		width: 65%;
		gap: 0;
	}
	h1 {
		align-self: flex-start;
	}
	.offers {
		display: flex;
		padding: 0.15em 0 0.15em 1em;
		border-radius: 20px;
		justify-items: flex-start;
		background-color: #e8e1dd;
		margin: 1em 0 0.5em 0;

		width: 100%;
		font-size: 1.25em;
	}
</style>