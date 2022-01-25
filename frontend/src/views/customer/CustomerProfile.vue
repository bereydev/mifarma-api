<template>
	<div class="profile">
		<profile-form />
	</div>
</template>



<script>
	import ProfileForm from "@/components/ProfileForm.vue";

	export default {
		name: "CustomerProfile",
		components: {
			ProfileForm,
		},
	};
</script>

<style lang="scss" scoped>
	.profile {
		width: 30%;
		margin: auto;
	}
</style>
