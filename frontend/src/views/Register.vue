<template>
	<body>
		<NavBarComponent :access="true"/>
		<RegisterForm />
	</body>
</template>

<script>
	import RegisterForm from "../components/RegisterForm.vue";
	import NavBarComponent from "../components/NavBarComponent.vue";

	export default {
		name: "Register",
		components: {
			RegisterForm,
			NavBarComponent,
		},
	};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	body {
		margin: 0;
	}
</style>