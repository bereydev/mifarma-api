<template>
	<div class="content">
		<img
			src="https://images.pexels.com/photos/5699982/pexels-photo-5699982.jpeg?cs=srgb&dl=pexels-markus-winkler-5699982.jpg&fm=jpg"
			alt="Foto Farmacia"
		/>
		<div class="info">
			<div v-for="(value, name) in $store.state.pharmacy.schedule" :key="name">
				<span
					><b>{{ name }}</b> :
					{{ value.join(", ") }}
				</span>
			</div>
		</div>

		<div class="info">
			<span> <b>Dirección: </b>Camino de Ronda 158</span>
			<span><b>Ciudad: </b>Granada</span>
			<span><b>País: </b>España</span>
			<span><b>Email: </b>farmaciadelacalle@gmail.com</span>
			<span><b>tlfo: </b>+34 609 45 67 89</span>
		</div>
	</div>
    
</template>

<script>
	export default {
		name: "UnverifiedPharmaInfo",
	};
</script>

<style scoped>
	img {
		border-radius: 10%;
		object-fit: cover;
		width: 12em;
		height: 12em;
	}

    p{
        width: 60%;
        margin: none; 
        padding: none; 
    }

	span {
		text-align: start;
	}
	.content {
		display: flex;
		gap: 1em;
	}
	.info {
		display: flex;
		flex-direction: column;
		text-align: left;
		justify-content: flex-start;
		gap: 0.25em;
		margin: 0 1em 0 1em;
	}
</style>