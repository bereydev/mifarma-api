<template>
	<div class="topNavBar">
		<div class="group">
			<img class="logo-img" src="../assets/logo.png" alt="MiFarmacia logo" />
			<div id="brandName">MiFarmacia</div>
		</div>

		

		<div  class="group">
            
			<div class="navBarElement">Soy una farmacia</div>
			<div class="navBarElement">Contacto</div>

			<router-link class="navBarElement" id="access" v-show="access" to="/login"
				>Acceder</router-link
			>
			<router-link
				class="navBarElement"
				id="register"
				v-show="!access"
				to="/register"
				>Registrarse</router-link
			>
		</div>
	</div>
</template>


<script>
	export default {
		name: "NavBarPresentation",
		props: {
			searchBar: {
				type: Boolean,
				default: false,
			},
			access: {
				type: Boolean,
				default: false,
			},
            identified: {
				type: Boolean,
				default: false,
			},
		},
	};
</script>


<style scoped>
	.group {
		display: flex;
	}
	.logo-img {
		height: 2em;
		width: auto;
		align-self: center;
	}
	#brandName {
		font-size: 1.25em;
		font-weight: bold;
		margin: 0 0 0 0.25em;
		padding: 0.25em 0 0 0;
		align-self: center;
	}

	.navBarElement {
		color: #2e2931;
		align-self: center;
		justify-self: center;
		font-size: 1em;
		flex: 1 0 auto;
		margin: 0 0.5em 0 0.5em;
	}

	.material-icons {
		color: #2e2931;
		border: 2px solid #adadad;
		border-radius: 100%;
		padding: 0.05em;
		font-size: 6em !important;
	}

	#access {
		padding: 0.5em 1em 0.5em 1em;
		background-color: #2e2931;
		border-radius: 38px;
		color: white;
		justify-content: center;
		box-shadow: 0px 3px 6px -3.5px grey;
	}
	#register {
		padding: 0.5em 1em 0.5em 1em;
		background-color: #00dd7c;
		border-radius: 38px;
		color: #2e2931;
		justify-content: center;
		box-shadow: 0px 3px 6px -3.5px grey;
	}

	spacer {
		flex: 100 100 auto;
	}

	.topNavBar {
		box-sizing: border-box;
		padding: 0.25em 1.5em 0.25em 1.5em;
		font-size: 1.15em;
		height: 3.5em;
		width: 100%;
		background: #f5f5f5;
		display: flex;
		align-content: center;
		justify-content: space-between;
	}

	
	.searchBar:focus {
		outline: 1px solid #00dd7c;
	}

	.searchBar:hover {
		outline: 1px solid #00dd7c;
	}
</style>
