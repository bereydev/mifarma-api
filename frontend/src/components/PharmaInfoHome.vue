<template>
	<div class="pharma-pannel">
		<h1>Mi Farmacia</h1>
		<div class="picture-text">
			<div class="picture-button">
				<img
					src="https://images.pexels.com/photos/5699982/pexels-photo-5699982.jpeg?cs=srgb&dl=pexels-markus-winkler-5699982.jpg&fm=jpg"
					alt="Foto Farmacia"
				/>
				<router-link to="/customer/pharma-picker">
					<button-vue  color="dark">Cambiar de Farmacia</button-vue>
				</router-link>
			</div>
			<div class="pharma-info">
				<span>{{ $store.state.pharmacy.name }}</span>
				<span>{{ $store.state.pharmacy.address }}</span>
				<span>{{ $store.state.pharmacy.address2 }}</span>
				<span>{{ $store.state.pharmacy.city }}</span>
				<span>{{ $store.state.pharmacy.country }}</span>
				<span>{{ $store.state.pharmacy.email }}</span>
				<span>{{ $store.state.pharmacy.phone }}</span>
				<router-link to="/customer/Catalog">
					<button-vue size="medium" class="abs-center-x">Catálogo</button-vue>
				</router-link>
			</div>
		</div>
		<p>
			{{ $store.state.pharmacy.description }}
		</p>
		<div class="schedule">
			<div v-for="(value, name) in $store.state.pharmacy.schedule" :key="name">
				<span
					><b>{{ name }}</b> :
					{{ value.join(", ") }}
				</span>
			</div>
		</div>
	</div>
</template>

<script>
	import ButtonVue from "./Button.vue";

	export default {
		name: "PharmaInfoHome",
		components: {
			ButtonVue,
		},
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
	.abs-center-x {
		position: absolute;
		bottom: 0;
		left: 50%;
		transform: translate(-50%, 0);
	}

	.picture-text {
		display: flex;
		justify-content: flex-start;
	}

	img {
		border-radius: 10%;
		object-fit: cover;
		width: 12em;
		height: 12em;
		margin-bottom: 1em;
	}
	.pharma-info {
		position: relative;
		display: flex;
		flex-direction: column;
		text-align: justify;
		justify-content: flex-start;
    padding: auto;
		width: 50%;
		gap: 0.25em;
	}
	.schedule {
		display: flex;
		flex-direction: column;
		text-align: justify;
		justify-content: flex-end;
		align-items: flex-start;
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
		gap: .75em;
		width: 35%;
	}
</style>
