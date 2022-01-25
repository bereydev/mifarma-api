<template>
	<nav>
		<div class="row-left">
			<router-link to="/customer/dashboard"
				><img class="logo-img" src="../assets/logo.png" alt="MiFarmacia logo"
			/></router-link>
			<router-link to="/customer/dashboard"
				><div id="brandName" class="navBarElement">MiFarmacia</div></router-link
			>
		</div>
		<div v-if="isAuth" class="row-center">
			<input
				v-debounce:500="updateSearchText"
				class="searchBar"
				placeholder="Buscar"
				type="text"
				id="name"
				name="name"
			/>
		</div>
		<div v-if="isAuth" class="row-right">
			<router-link style="position: relative" to="/customer/cart">
				<i class="material-icons" id="navBarCart">shopping_cart</i>
				<div v-if="this.$store.getters.cartItemCount > 0" class="notif">
					{{ this.$store.getters.cartItemCount }}
				</div></router-link
			>

			<router-link style="display:flex; justify-content:center; align-items:center" to="/customer/profile">
				<img
					class="profile-pic"
					src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2960&q=80"
					alt="Foto de perfil"
				/>
			</router-link>
		</div>

		<div v-if="!isAuth" class="group">
			<NavTab link="/pro/welcome">Soy una farmacia</NavTab>
			<NavTab>Contacto </NavTab>
			<NavTab :link="buttonLink">
				<Button :color="buttonColor">{{ buttonText }}</Button>
			</NavTab>
		</div>
	</nav>
</template>

<script>
	import Button from "./CustomButton.vue";
	import NavTab from "./NavTab.vue";

	export default {
		name: "NavBar",
		data() {
			return {
				search: "",
			};
		},
		methods: {
			async updateSearchText(text) {
				this.search = text.toLowerCase().replace(/\p{Diacritic}/gu, "");

				await this.$store.dispatch("updateSearchText", { text: this.search });

				if (this.$route.name === "PharmaPicker")
					await this.$store.dispatch("updateActivePharmacies", {
						filter: this.search,
					});

				if (this.$route.name === "Catalog")
					await this.$store.dispatch("updateCatalog", { filter: this.search });
			},
		},
		computed: {
			isAuth() {
				return !(
					this.$route.name === "Login" ||
					this.$route.name === "Register" ||
					this.$route.name === "RegisterPro" ||
					this.$route.name === "Welcome" ||
					this.$route.name === "WelcomePro"
				);
			},
			buttonText() {
				return this.$route.name === "Login" ? "Registrarse" : "Acceder";
			},
			buttonColor() {
				return this.$route.name === "Login" ? "green" : "dark";
			},
			buttonLink() {
				return this.$route.name === "Login" ? "/register" : "/login";
			},
		},
		props: {},
		components: {
			Button,
			NavTab,
		},
	};
</script>

<style lang="scss" scoped>
	nav {
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
		color: #2e2931;
	}

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

	.profile-pic {
		border-radius: 50%;
		width: 3em;
		height: 3em;
		border: 3px solid #00dd7c;
	}

	.notif {
		display: flex;
		align-items: center;
		justify-content: center;
		position: absolute;
		left: 2.5em;
		bottom: 0em;
		width: 1em;
		height: 1em;
		padding: 0.75em;
		border-radius: 100%;
		background-color: #ffd500;
		font-size: 0.75em;
		font-weight: bold;
		color: #2e2931;
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

	.material-icons {
		color: #2e2931;
		border: 2px solid #adadad;
		border-radius: 100%;
		padding: 0.05em;
		font-size: 6em !important;
	}

	spacer {
		flex: 100 100 auto;
	}

	.searchBar:focus {
		outline: 1px solid #00dd7c;
	}

	.searchBar:hover {
		outline: 1px solid #00dd7c;
	}
</style>
