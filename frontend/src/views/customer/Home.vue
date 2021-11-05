<template>
	<body>
		<div class="panels">
			<div class="dashboard">
				<HomeSelector @selector-click="filterStatus" />
				<div class="scroll">
					<div
						style="margin: 0.15em 0 0.15em 0"
						v-for="order in filtered"
						:key="order.id"
					>
						<Order :order="order" />
					</div>
				</div>
			</div>
			<PharmaInfoHome />
		</div>
	</body>
</template>

<script>
	import HomeSelector from "../../components/HomeSelector.vue";
	import Order from "../../components/Order.vue";
	import PharmaInfoHome from "../../components/PharmaInfoHome.vue";

	export default {
		name: "Register",
		data() {
			return {
				orders: [],
				filtered: [],
			};
		},
		methods: {
			filterStatus(id) {
				if (id === -1) this.filtered = this.orders;
				else this.filtered = this.orders.filter((e) => e.status === id);
			},
			filterName(text) {
				text = text
					.normalize("NFD")
					.replace(/[\u0300-\u036f]/g, "")
					.toLowerCase();
				if (text === "") this.filtered = this.orders;
				else
					this.filtered = this.orders.filter((o) =>
						o.product.name
							.normalize("NFD")
							.replace(/[\u0300-\u036f]/g, "")
							.toLowerCase()
							.includes(text)
					);
			},
		},
		components: {
			HomeSelector,
			Order,
			PharmaInfoHome,
		},
		async created() {
			let url =
				"https://stag.mifarmacia.app/api/v1/shop-pro/placed-orders-by-customer/8de69c90-df9a-4c70-8525-bd4192077e06";
			const response = await fetch(url, {
				method: "GET", // *GET, POST, PUT, DELETE, etc.
				headers: {
					"Content-Type": "application/json",
					Authorization:
						"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzYxODU4MjIsInN1YiI6ImRkZTIwNTNlLWNmNDItNDliOS1iNzMxLTA5YjhiYWE1ZDg0NiJ9.uIIGvC9sqlnwW5SpKMgDcDgALAvekN0kreEG9CwI-lI",
				},
				//body: JSON.stringify(data) // body data type must match "Content-Type" header
			});
			this.orders = await response.json();
			this.filtered = this.orders;
		},
	};
</script>


<style scoped>

	.panels {
		display: flex;
		width: 100%;
		padding: 1.5% 1% 5% 1%;
		gap: 2.5%;
	}

	.dashboard {
		display: flex;
		flex-direction: column;
		width: 65%;
		gap: 0.75em;
	}
</style>