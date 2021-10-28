<template>
	<div class="order" :style="{ 'background-color': backgroundColor }">
		<div class="row-left">
			<img
				class="drug-pic"
				src="https://images.pexels.com/photos/159211/headache-pain-pills-medication-159211.jpeg?cs=srgb&dl=pexels-pixabay-159211.jpg&fm=jpg"
				alt="Foto de perfil"
			/>
			<span>Nombre del Medicamento</span>
		</div>
		<div class="row-right">
			<div class="order-time">
				<span>Disponible</span>
				<i class="material-icons time-icon">event_available</i>
			</div>
			<button class="material-icons dots">more_vert</button>
		</div>
	</div>
</template>

<script>
	export default {
		name: "Order",
		props: {
			status: Number,
		},
		computed: {
			backgroundColor() {
				if (this.status === 0) return "#A6FFD8";
				if (this.status === 1) return "#FFEE97";
				if (this.status === 2) return "#FFA192";
				else return "#ADADAD";
			},
		},
	};
</script>

<style scoped>
	.order {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 0.5em 1em 0.5em 1em;
		border-radius: 28px;
	}
	.drug-pic {
		border-radius: 50%;
		width: 2.5em;
		height: 2.5em;
		border: 1px solid #2e2931;
	}

    .dots {
		background-color: white;
		color: #2e2931;
		border-radius: 50%;
		font-size: 1.75em !important;
		padding: .3em;
        border: none; 
	}

    .time-icon {
		color: #2e2931;
		font-size: 1.75em !important;
        border: none; 
	}

    

	.order-time {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 80%;
        padding: .6em;
        border-radius: 12px;
        background-color: white;
	}
	.row-left {
		display: flex;
		gap: 1em;
		width: 30%;
		align-items: center;
		justify-content: flex-start;
	}
	.row-right {
		display: flex;
		gap: 0.15em;
		align-items: center;
        width: 40%;
        justify-content: space-between;
	}
</style>