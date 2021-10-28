<template>
	<body>
		<NavBarOut :access="true" />
		<RegisterForm />
	</body>
</template>

<script>
	import RegisterForm from "../components/RegisterForm.vue";
	import NavBarOut from "../components/NavBarOut.vue";

	export default {
		name: "Register",
		components: {
			RegisterForm,
			NavBarOut,
		},
	};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	body {
		margin: 0;
	}
</style>