<template>
	<body>

        <NavBarIn/>
		

		<div class="panels">
			<div class="dashboard">
				<div class="selector">
					<h1>Mis pedidos</h1>
					<div class="button-panel">
						<i class="material-icons selectorIcon" id="icon1"
							>event_available</i
						>
						<i class="material-icons selectorIcon">watch_later</i>
						<i class="material-icons selectorIcon">close</i>
						<i class="material-icons selectorIcon">hourglass_bottom</i>
					</div>
				</div>

				<div class="order">
					<img
						class="profile-pic"
						src="https://images.unsplash.com/photo-1618397306947-68dd11e97812?crop=entropy&cs=srgb&fm=jpg&ixid=MnwxNDU4OXwwfDF8cmFuZG9tfHx8fHx8fHx8MTYzNDg2MjE3Mg&ixlib=rb-1.2.1&q=85"
						alt="Foto de perfil"
					/>
					<span>Nombre del Medicamento</span>
					<div class="order-time">
						<span>MisPedidos</span>
						<div>icon</div>
					</div>
					<div>icon</div>
				</div>
			</div>
			<div class="pharma-info">
				<span>Mi Farmacia</span>
			</div>
		</div>
	</body>
</template>

<script>
	import NavBarIn from '../../components/NavBarIn.vue';

	export default {
		name: "Register",
		components: {
			NavBarIn,
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

	img {
		width: 3em;
	}

	

	#icon1 {
		background-color: #00dd7c;
		color: white;
	}
	#icon2 {
		background-color: #00dd7c;
		color: white;
	}
	#icon3 {
		background-color: #00dd7c;
		color: white;
	}
	#icon4 {
		background-color: #00dd7c;
		color: white;
	}

	.profile-pic {
		border-radius: 100%;
		width: 3em;
		height: 3em;
		border: 3px solid #00dd7c;
	}

	spacer {
		flex: 1 1 auto;
	}

	h1 {
		font-size: 1.5em;
		padding: 0;
		margin-block-start: 0px;
		margin-block-end: 0px;
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
		flex: 1.5 1 auto;
	}
	.selector {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 10%;
		width: 30%;
		padding: 0 0 5% 2.5%;
	}

	.button-panel {
		display: flex;
		align-items: center;
		justify-content: flex-start;
		gap: 20%;
	}

	.order {
		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.order-time {
		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.pharma-info {
		flex: 1 1 auto;
	}
</style>