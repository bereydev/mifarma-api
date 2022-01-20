<template>
	<button :class="styles">
		<slot />
	</button>
</template>

<script>
	export default {
		name: "CustomButton",
		props: {
			color: { type: [String], default: "green" },
			size: { type: [String], default: "" },
		},
		computed: {
			styles() {
				return `btn ${this.size} btn-${this.color}`;
			},
		},
	};
</script>

<style lang="scss" scoped>
	@import "../assets/styles/colors.scss";

	.btn {
		display: flex;
		padding: 0.5em 1em 0.5em 1em;
		border-radius: 38px;
		border: none;
		justify-content: center;
		align-items: center;
		gap: .5em;
		box-shadow: 0px 3px 6px -3.5px grey;
		font-size: 18px;
		-webkit-transition: all 0.3s ease-in-out;
		-moz-transition: all 0.3s ease-in-out;
		transition: all 0.3s ease-in-out;
		cursor: pointer;
	}
	.large {
		padding: 0.5em 5em 0.5em 5em !important;
	}
	.medium {
		padding: 0.5em 3em 0.5em 3em !important;
	}
	.small{
		width: 75%;
		padding: 0.5em .5em 0.5em .5em !important;
	}
	.btn-green:hover {
		background-color: $accent-green-hover;
	}

	.btn-green {
		background-color: $accent-green;
		color: $black;
	}

	.btn-red {
		background-color: $accent-red;
		color: $black;
	}

	.btn-red:hover {
		background-color: $accent-red-hover;
	}

	.btn-dark:hover {
		background-color: $black-hover
	}
	.btn-dark {
		background-color: $black;
		color: white;
	}
</style>
