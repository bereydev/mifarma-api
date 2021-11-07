<template>
	<router-link :to="{ path: '/customer/Drug', query: { ean: '69420' } }">
		<div class="col">
			<img
				src="https://images.unsplash.com/photo-1587854692152-cbe660dbde88?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1769&q=80"
				alt="Foto Medicamento"
			/>
			<span>No</span>
			<span>No</span>
		</div>
	</router-link>
</template>

<script>
	export default {
		name: "DrugWidget",
		props:{
			drug: {
				name: 'Nombre del medicamento',
				price: '5.00'
			}, 
		}
	};
</script>

<style scoped>
	img {
		border-radius: 10%;
		object-fit: cover;
		width: 125px;
		height: 125px;
		margin-bottom: 0.25em;
		box-shadow: 0px 3px 3px 1.5px rgb(211, 211, 211);
	}
	span {
		width: 100px;
		white-space: pre-wrap;
		text-align: center;
	}
	.col {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.05em;
	}
</style>