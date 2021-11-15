<template>
	<div class="owner-list">
    <h1>Unverified owners</h1>
		<div v-for="(owner, index) in owners" :key="index">
			<owner-item :owner="owner"></owner-item>
		</div>
	</div>
</template>

<script>
	import OwnerItem from "./OwnerItem.vue";
	export default {
		name: "OwnerList",
		props: ["owners"],
		components: {
			OwnerItem,
		},
	};
</script>

<style>
	.owner-list {
		display: flex;
		flex-direction: column;
		gap: 0.5em;
    align-items: flex-start;
	width: 17%;
	}
	h1{
		font-size: 1.5em;
	}
</style>
