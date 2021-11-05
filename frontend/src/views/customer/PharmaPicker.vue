<template>
	<body>
		<button class="green-button" id="confirmButton">Confimar</button>

		<div class="indication">
			<span class="material-icons-outlined infoIcon"> info </span>

			Seleccione su farmacia de confianza, podrá modificar su selección más
			tarde en ajustes de cuenta
		</div>
		<div class="pharmaRow">
			<PharmaWidget v-for="i in [1, 2, 3, 4, 5, 6]" :key="i" />
		</div>
        <div class="pharmaRow">
			<PharmaWidget v-for="i in [1, 2, 3, 4, 5, 6]" :key="i" />
		</div>
        <div class="pharmaRow">
			<PharmaWidget v-for="i in [1, 2, 3, 4, 5, 6]" :key="i" />
		</div>
	</body>
</template>


<script>
	import PharmaWidget from "../../components/PharmaWidget.vue";

	export default {
		name: "Cart",
		data() {
			return {
				pharmacies: [],
				filtered: [],
			};
		},
		components: {
			PharmaWidget,
		},
		methods: {
			filterName(text) {
				text = text
					.normalize("NFD")
					.replace(/[\u0300-\u036f]/g, "")
					.toLowerCase();
				if (text === "") this.filtered = this.pharmacies;
				else
					this.filtered = this.pharmacies.filter((o) =>
						o.product.name
							.normalize("NFD")
							.replace(/[\u0300-\u036f]/g, "")
							.toLowerCase()
							.includes(text)
					);
			},
		},

		async created() {
			/*let url =
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
						this.filtered = this.orders;*/
			return null;
		},
	};
</script>


<style scoped>
	body {
		display: flex;
		flex-direction: column;
		padding: 1% 2.5% 2.5% 2.5%;
	}

	#confirmButton {
		width: 15%;
		align-self: flex-end;
	}

	.pharmaRow {
		display: flex;
        margin : 1em 0 1em 0; 
		gap: 2em;
		justify-content: center;
		align-items: center;
	}
	.indication {
		display: flex;
		border-radius: 20px;
		background-color: #e8e1dd;
		margin: 1em 0 1em 0;
		font-size: 1.15em;
		padding: 1em;
		gap: 1em;
		justify-content: flex-start;
		align-items: center;
	}

	.infoIcon {
		font-size: 1.5em !important;
	}
</style>