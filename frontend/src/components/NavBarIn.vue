
<template>
	<div class="topNavBar">
		<div class="row-left">
			<router-link to="/customer/Home"
				><img class="logo-img" src="../assets/logo.png" alt="MiFarmacia logo"
			/></router-link>
			<router-link to="/customer/Home"
				><div id="brandName" class="navBarElement">MiFarmacia</div></router-link
			>
		</div>
		<div class="row-center">
			<input
				v-show="searchBar"
				@input="$emit('search-input', searchText)"
				v-model="searchText"
				class="searchBar"
				placeholder="Buscar producto"
				type="text"
				id="name"
				name="name"
			/>
		</div>
		<div class="row-right">
			<router-link style="position: relative" to="/customer/Cart">
				<i class="material-icons" id="navBarCart">shopping_cart</i>
				<div class="notif">3</div></router-link
			>

			<img
				class="profile-pic"
				src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2960&q=80"
				alt="Foto de perfil"
			/>
		</div>
	</div>
</template>

<script>
	export default {
		name: "NavBarPresentation",
		data() {
			return {
				searchText: "",
			};
		},
		props: {
			searchBar: {
				type: Boolean,
				default: true,
			},
		},
	};
</script>

<style scoped>
	.searchBar {
		border: none;
		width: 25em;
		border-radius: 30px;
		padding: 0.5em 1em 0.5em 1em;
		font-size: 1em;
	}
	input:focus {
		outline: 1px solid #00dd7c;
	}

	input:hover {
		outline: 1px solid #00dd7c;
	}

	.searchBar {
		border: none;
		align-self: center;
		width: 25em;
		border-radius: 30px;
		padding: 0.5em 1em 0.5em 1em;
		font-size: 1em;
	}

	.row-left {
		display: flex;
		gap: 0.15em;
		width: 10%;
		align-items: center;
		justify-content: flex-start;
	}
	.row-center {
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.row-right {
		display: flex;
		gap: 1.5em;
		width: 10%;
		align-items: center;
		justify-content: flex-end;
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

	.profile-pic {
		border-radius: 100%;
		width: 3em;
		height: 3em;
		border: 3px solid #00dd7c;
	}

	.notif {
		display: flex;
		align-items: center;
		justify-content: center;
		position: absolute;
		left: 2em;
		bottom: 0em;
		width: 1em;
		height: 1em;
		padding: 0.15em;
		border-radius: 100%;
		background-color: #ffd500;
	}

	.topNavBar {
		box-sizing: border-box;
		padding: 0.25em 1.5em 0.25em 1.5em;
		font-size: 1.15em;
		height: 3.5em;
		width: 100%;
		background-color: #f5f5f5;
		display: flex;
		align-content: center;
		justify-content: space-between;
	}

	#navBarCart {
		display: flex;
		justify-items: center;
		align-content: center;
		color: #2e2931;
		border: 3px solid #2e2931;
		font-size: 1.75em !important;
		padding: 0.2em;
		color: #2e2931;
		border-radius: 100%;
		background-color: white;
	}

	.navBarElement {
		color: #2e2931;
		font-size: 1em;
	}
</style>