<template>
	<body>
		<NavBarIn />

		<div class="panels">
			<div class="dashboard">
				<HomeSelector />
				<div class="orders" v-for="order in orders" :key="order.id"> 
					<Order :order="order"/>
				</div>
			</div>
			<div class="pharma-info">
				<span>Mi Farmacia</span>
			</div>
		</div>
	</body>
</template>

<script>
	import NavBarIn from "../../components/NavBarIn.vue";
	import HomeSelector from "../../components/HomeSelector.vue";
	import Order from "../../components/Order.vue";

	export default {
		name: "Register",
		data() {
			return {
				orders:[],
			};
		},
		components: {
			NavBarIn,
			HomeSelector,
			Order,
		},
		async created() {
      let url = 'https://stag.mifarmacia.app/api/v1/shop-pro/placed-orders-by-customer/8de69c90-df9a-4c70-8525-bd4192077e06'; 
      const response = await fetch(url, {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzYxODU4MjIsInN1YiI6ImRkZTIwNTNlLWNmNDItNDliOS1iNzMxLTA5YjhiYWE1ZDg0NiJ9.uIIGvC9sqlnwW5SpKMgDcDgALAvekN0kreEG9CwI-lI'
    },
    //body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  this.orders = await response.json(); 
			
		},
	};
</script>


<style scoped>


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
		width: 65%;
		gap: .75em; 
	}

	.pharma-info {
		width: 40%;
	}
</style>