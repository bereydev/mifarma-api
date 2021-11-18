<template>
	<CatalogPharmaInfo />
	<div class="offers">Ofertas</div>
	<div class="drugRow">
		<DrugWidget
			:drug="drug"
			v-for="drug in $store.state.catalog"
			:key="drug.ean"
		/>
	</div>
	<div class="drugRow"></div>
	<div class="offers" style="background-color: #a6ffd8">Productos</div>

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
</template>

<script>
	import CatalogPharmaInfo from "../../components/CatalogPharmaInfo.vue";
	import DrugWidget from "../../components/DrugWidget.vue";
	import axios from "axios";

	export default {
		name: "Catalog",
		data() {
			return {
				products: [],
			};
		},
   
		components: {
			CatalogPharmaInfo,
			DrugWidget,
		},
		async created() {
			await this.$store.dispatch("updateCatalog");
		},
	};
</script>

<style scoped>
	.offers {
		display: flex;
		padding: 0.15em 0 0.15em 1em;
		border-radius: 20px;
		justify-items: flex-start;
		margin: 1em 0 1em 2.5%;
		background-color: #ffee97;
		width: 95%;
		font-size: 1.25em;
	}

	.drugRow {
		display: flex;
		margin: 1em 0 1em 3%;
		gap: 1em;
		flex-direction: row;
		overflow: auto;
	}
</style>
