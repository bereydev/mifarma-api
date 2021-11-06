<template>
	<div class="pharma-pannel">
		<h1>Mi Farmacia</h1>
		<div class="picture-text">
			<div class="picture-button">
				<img
					src="https://images.pexels.com/photos/5699982/pexels-photo-5699982.jpeg?cs=srgb&dl=pexels-markus-winkler-5699982.jpg&fm=jpg"
					alt="Foto Farmacia"
				/>
				<router-link
					style="color: white; background-color: #2e2931"
					id="button"
					class="green-button"
					to="/customer/pharma-picker"
					>Cambiar de Farmacia</router-link
				>
				
			</div>
			<div class="pharma-info">
				<span>Nombre Farmacia</span>
				<span>Dirección</span>
				<span>69420</span>
				<span>Granada</span>
				<span>España</span>
				<span>correofarmacia@gmail.com</span>
				<span>958556677</span>
				<router-link
					style="font-size: 1.25em"
					id="button"
					class="green-button"
					to="/customer/Catalog"
					>Catálogo</router-link
				>
			</div>
		</div>
		<p>
			Primera farmacia aprobada para venta online de medicamentos, Farmacia
			Campoamor es referente nacional en gestión de oficina de farmacia. Abierta
			desde 1978 por Lda. Margarita González, cuenta profesionales multilíngües
			centrados en proporcionar el mejor servicio a los mejores precios
			posibles.
		</p>
		<div class="schedule">
			<span><b>Lunes</b> : 08:30 - 14:00, 17:00 - 21:00</span>
			<span><b>Martes</b> : 08:30 - 14:00, 17:00 - 21:00</span>
			<span><b>Miércoles</b> : 08:30 - 14:00, 17:00 - 21:00</span>
			<span><b>Jueves</b> : 08:30 - 14:00, 17:00 - 21:00</span>
			<span><b>Viernes</b> : 08:30 - 14:00, 17:00 - 21:00</span>
			<span><b>Sábado</b> : 08:30 - 14:00</span>
			<span><b>Domingo</b> : Cerrado</span>
		</div>
	</div>
</template>

<script>
	export default {
		name: "PharmaInfoHome",
	};
</script>

<style scoped>
	.wrap-text {
		white-space: pre;
	}
	h1 {
		font-size: 1.75em;
		padding: 0 0 0 5%;
		margin-block-start: 0px;
		margin-block-end: 0px;
	}

	span {
		text-align: start;
	}

	#button {
		font-size: 1em;
		width: 100%;
		padding: 0.25em;
	}

	.picture-text {
		display: flex;
		justify-content: flex-start;
		gap: 2em;
	}

	img {
		border-radius: 10%;
		object-fit: cover;
		width: 12em;
		height: 12em;
	}
	.pharma-info {
		display: flex;
		flex-direction: column;
		text-align: left;
		justify-content: flex-end;
		width: 50%;
		gap: 0.25em;
	}
	.schedule {
		margin-top: 1em;
		display: flex;
		flex-direction: column;
		text-align: left;
		justify-content: flex-end;
		width: 100%;
		gap: 0.5em;
	}
	.picture-button {
		display: flex;
		flex-direction: column;
		justify-content: flex-end;

		gap: 0.25em;
	}
	span {
		display: inline-block;
	}

	.pharma-pannel {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		justify-content: flex-start;
		gap: 1em;
		width: 35%;
	}
</style>