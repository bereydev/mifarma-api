<template>
	<div class="col">
		<img
			src="https://images.unsplash.com/photo-1531076226985-ee33c0d85b21?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1776&q=80"
			alt="Foto Farmacia"
		/>
		<span>Nombre de la Farmacia</span>
	</div>
</template>

<script>
	export default {
		name: "PharmaWidget",
	};
</script>

<style scoped>
	img {
		border-radius: 10%;
		object-fit: cover;
		width: 180px;
		height: 180px;
		margin-bottom: 0.5em;
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