<template>
	<body>
		<NavBarIn />

		<div class="panels">
			<div class="dashboard">
				<HomeSelector />
				<Order :status="0" />
			</div>
			<div class="pharma-info">
				<span>Mi Farmacia</span>
			</div>
		</div>
	</body>
</template>

<script>
	import NavBarIn from "../../components/NavBarIn.vue";
	import HomeSelector from "../../components/HomeSelector.vue";
	import Order from "../../components/Order.vue";

	export default {
		name: "Register",
		components: {
			NavBarIn,
			HomeSelector,
			Order,
		},
	};
</script>


<style scoped>
	body {
		margin: 0;
		font-family: Roboto;
		font-size: 1em;
		color: #2e2931;
	}

	.small-text {
		padding: 0.75em 0em 1.5em 0em;
		font-size: 0.8em;
		color: #766b69;
		text-decoration: underline;
	}

	.panels {
		display: flex;
		width: 100%;
		padding: 1.5% 1% 5% 1%;
	}

	.dashboard {
		display: flex;
		flex-direction: column;
		width: 65%;
	}

	.pharma-info {
		width: 40%;
	}
</style>