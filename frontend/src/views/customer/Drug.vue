<template>
	<body>
		<div class="drug-info">
			<img
				src="https://images.unsplash.com/photo-1587854692152-cbe660dbde88?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1769&q=80"
				alt="Foto Medicamento"
			/>
			<div class="text-div">
				<h1>{{drug.name}}</h1>
				<h2>Descripción</h2>
				<p>
					{{drug.description}}
				</p>
        <p>
					{{drug.pharma_indications}}
				</p>
			</div>
			<div class="buy-div">
				<div style="display: flex; gap: 1em">
					<h2 class="price">{{drug.price}} $</h2>
				</div>

				<button class="green-button addButton">
					Añadir al carrito
					<div class="material-icons" id="navBarCart">shopping_cart</div>
				</button>
			</div>
		</div>
	</body>
</template>

<script>
import axios from "axios";

	export default {
    

		name: "Drug",
    data() {
			return {
				drug: null,
			};
		},
		async created() {
      try {
        const response = await axios.get('/products/ean/' + this.$route.query.ean);
        this.drug = response.data; 
      } catch (error) {
        console.error(error);
      }
		},
	};
</script>

<style scoped>
	body {
		display: flex;
		flex-direction: column;
		padding: 3.5% 2.5% 2.5% 2.5%;
	}
	img {
		border-radius: 10%;
		object-fit: cover;
		width: 180px;
		height: 180px;
		margin-bottom: 0.25em;
		box-shadow: 0px 3px 3px 1.5px rgb(211, 211, 211);
	}
	span {
		width: 100px;
		white-space: pre-wrap;
	}
	p,
	h1,
	h2 {
		margin: 0 0 0.5em 0;
		padding: 0;
		text-align: justify;
	}
	.price {
		font-size: 1.5em;
	}
	.addButton {
		padding: 0.5em;
		justify-content: space-evenly;
		width: 100%;
	}
	.drug-info {
		display: flex;
		gap: 2em;
		width: 100%;
	}
	.buy-div {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		width: 20%;
		margin-left: auto;
		margin-right: auto;
	}
	.text-div {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		justify-content: flex-start;
		width: 50%;
	}
</style>
