<template>
	<router-link :to="{ path: '/customer/Drug', query: { ean } }">
		<div class="col">
			<img
				src="https://images.unsplash.com/photo-1587854692152-cbe660dbde88?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1769&q=80"
				alt="Foto Medicamento"
			/>
			<span class="drug-name">{{ drug.name }}</span>
			<span>{{drug.price}} €</span>
		</div>
	</router-link>
</template>

<script>
	export default {
		name: "DrugWidget",
		props: ["drug"],
		data() {
			return {
				ean: this.drug.ean_code,
			};
		},
	};
</script>

<style scoped>
	img {
		border-radius: 10%;
		object-fit: cover;
		width: 125px;
		height: 125px;
		margin-bottom: 5px;
		box-shadow: 0px 3px 3px 1.5px rgb(211, 211, 211);
		transition: opacity 0.5s ease-out;
		-moz-transition: opacity 0.5s ease-out;
		-webkit-transition: opacity 0.5s ease-out;
		-o-transition: opacity 0.5s ease-out;
		opacity: 1;
	}
	.drug-name {
		width: 125px;
		white-space: pre-wrap;
		text-align: center;
		overflow: hidden;
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-line-clamp: 1; /* number of lines to show */
		line-clamp: 1;
		-webkit-box-orient: vertical;
	}
	.col {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.05em;
	}

	img:hover {
		opacity: 0.8;
	}
</style>
