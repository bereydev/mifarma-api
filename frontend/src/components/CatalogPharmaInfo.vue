<template>
	<div class="col">
		<h1>Farmacia San Vicente</h1>
		<div class="row">
			<img
				src="https://images.pexels.com/photos/5699982/pexels-photo-5699982.jpeg?cs=srgb&dl=pexels-markus-winkler-5699982.jpg&fm=jpg"
				alt="Foto Farmacia"
			/>
			<div class="info-row" >
				<div class="schedule">
					<span><b>Lunes</b> : 08:30 - 14:00, 17:00 - 21:00</span>
					<span><b>Martes</b> : 08:30 - 14:00, 17:00 - 21:00</span>
					<span><b>Miércoles</b> : 08:30 - 14:00, 17:00 - 21:00</span>
					<span><b>Jueves</b> : 08:30 - 14:00, 17:00 - 21:00</span>
					<span><b>Viernes</b> : 08:30 - 14:00, 17:00 - 21:00</span>
					<span><b>Sábado</b> : 08:30 - 14:00</span>
					<span><b>Domingo</b> : Cerrado</span>
				</div>
				<div class="schedule">
					<span>Dirección</span>
					<span>69420</span>
					<span>Sevilla</span>
					<span>España</span>
					<span>correo@gmail.com</span>
					<span>958424242</span>
				</div>
			</div>
		</div>
	</div>
</template>


<script>
	export default {
		name: "CatalogPharmaInfo",
	};
</script>


<style scoped>
	h1 {
		font-size: 1.5em;
		padding: 0em 0 0.75em 1.5em;
	}
	.row {
		display: flex;
		gap: 2em;
		width: 100%;
	}
    .info-row {
        padding: .5em .5em .5em 2em; 
		display: flex;
        width: 50%;
        background-color: #F5F5F5;
        border-radius: 25px;
        justify-content: flex-start;
        gap: 7.5em;
        box-shadow: 0px 3px 5px 1px rgb(211, 211, 211);
	}
	.col {
		padding: 1em 0 1em 2em;
		display: flex;
		flex-direction: column;
		align-items: flex-start;
        
	}
	img {
		border-radius: 10%;
		object-fit: cover;
		width: 180px;
		height: 180px;
	}
	.schedule {
        margin:0; 
		display: flex;
		flex-direction: column;
		text-align: left;
		justify-content: flex-start;
		width: 30%;
		gap: 0.15em;
	}
</style>