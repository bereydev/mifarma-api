<template>
	<div class="pannel">
		<img
			class="user-pic"
			src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2960&q=80"
			alt="Foto usuario"
		/>
		<div class="infos">
			<span><b>Nombre</b>: María</span>
			<span><b>Apellidos</b>: De Los Santos</span>
			<span><b>Número de identificación</b>: 00742069</span>
			<span><b>Documento de identidad</b>:</span>
		</div>
	</div>
</template>

<script>
	export default {
		name: "UnverifiedPharmaDoc",
	};
</script>

<style scoped>
	.user-pic {
		border-radius: 50%;
		width: 6em;
		height: 6em;
		border: 1px solid #2e2931;
	}
	.pannel {
		display: flex;
		flex-direction: row;
		gap: 1em;
		padding-bottom: 1em;
	}
	.infos {
		display: flex;
		flex-direction: column;
		gap: 0.25em;
		text-align: justify;
	}
</style>