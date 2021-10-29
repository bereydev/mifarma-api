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
		created() {
			this.orders = [ { pharmacy_id: '90550ff5-15d7-4bce-838f-03a437ba2bd8',
    user_id: '8de69c90-df9a-4c70-8525-bd4192077e06',
    product_id: '04486d18-8b60-4e37-85ad-b1d8ea49b233',
    amount: 1,
    status: 1,
    delivery_date: null,
    order_date: '2021-08-26T20:05:41.722854',
    id: '5efd98f5-c171-4a17-9698-972ea5628e22',
    product:
     { ean_code: '001',
       classification_number: '000',
       name: 'Test Drug 1',
       description:
        'Description of the test drug. This drug is here for our dev to test out the app.',
       price: 10,
       pharma_indications: 'Please do not take this drug, might have bugs.',
       type_of_material: 0,
       magnitude: 10,
       laboratory: 'Testing Labs',
       id: '04486d18-8b60-4e37-85ad-b1d8ea49b233',
       type: 'drugs' } },
  { pharmacy_id: '90550ff5-15d7-4bce-838f-03a437ba2bd8',
    user_id: '8de69c90-df9a-4c70-8525-bd4192077e06',
    product_id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
    amount: 5,
    status: 1,
    delivery_date: null,
    order_date: '2021-08-26T20:05:41.707249',
    id: 'f21cebcb-8033-4f44-82e6-dc736165266f',
    product:
     { ean_code: '420',
       classification_number: '420',
       name: 'Medicinal Marihuana',
       description: 'DESCRIPTION',
       price: 0,
       pharma_indications: 'INDICATIONS',
       type_of_material: 0,
       magnitude: 0,
       laboratory: 'LABORATORY',
       id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
       type: 'drugs' } },
  { pharmacy_id: '90550ff5-15d7-4bce-838f-03a437ba2bd8',
    user_id: '8de69c90-df9a-4c70-8525-bd4192077e06',
    product_id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
    amount: 1,
    status: 1,
    delivery_date: null,
    order_date: '2021-08-26T20:05:41.648224',
    id: '7a47e454-3323-4d7c-8194-719b77cad1e9',
    product:
     { ean_code: '420',
       classification_number: '420',
       name: 'Medicinal Marihuana',
       description: 'DESCRIPTION',
       price: 0,
       pharma_indications: 'INDICATIONS',
       type_of_material: 0,
       magnitude: 0,
       laboratory: 'LABORATORY',
       id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
       type: 'drugs' } },
  { pharmacy_id: '90550ff5-15d7-4bce-838f-03a437ba2bd8',
    user_id: '8de69c90-df9a-4c70-8525-bd4192077e06',
    product_id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
    amount: 2,
    status: 1,
    delivery_date: null,
    order_date: '2021-08-26T20:05:41.648224',
    id: '1140fb64-966f-479b-bbe6-af30148b7315',
    product:
     { ean_code: '420',
       classification_number: '420',
       name: 'Medicinal Marihuana',
       description: 'DESCRIPTION',
       price: 0,
       pharma_indications: 'INDICATIONS',
       type_of_material: 0,
       magnitude: 0,
       laboratory: 'LABORATORY',
       id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
       type: 'drugs' } },
  { pharmacy_id: '90550ff5-15d7-4bce-838f-03a437ba2bd8',
    user_id: '8de69c90-df9a-4c70-8525-bd4192077e06',
    product_id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
    amount: 1,
    status: 1,
    delivery_date: null,
    order_date: '2021-08-03T11:16:25.350444',
    id: 'f2b3e6a9-60f9-400b-ba79-c51aeb80c11c',
    product:
     { ean_code: '420',
       classification_number: '420',
       name: 'Medicinal Marihuana',
       description: 'DESCRIPTION',
       price: 0,
       pharma_indications: 'INDICATIONS',
       type_of_material: 0,
       magnitude: 0,
       laboratory: 'LABORATORY',
       id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
       type: 'drugs' } },
  { pharmacy_id: '90550ff5-15d7-4bce-838f-03a437ba2bd8',
    user_id: '8de69c90-df9a-4c70-8525-bd4192077e06',
    product_id: '3a0870e1-44da-477e-a159-a10b7ea47715',
    amount: 1,
    status: 1,
    delivery_date: null,
    order_date: '2021-08-26T20:05:41.648224',
    id: '36792e15-a338-440a-a748-19fbcbd78938',
    product:
     { ean_code: '000',
       classification_number: '000',
       name: 'Test Drug 0',
       description:
        'Description of the test drug. This drug is here for our dev to test out the app.',
       price: 10,
       pharma_indications: 'Please do not take this drug, might have bugs.',
       type_of_material: 0,
       magnitude: 10,
       laboratory: 'Testing Labs',
       id: '3a0870e1-44da-477e-a159-a10b7ea47715',
       type: 'drugs' } },
  { pharmacy_id: '90550ff5-15d7-4bce-838f-03a437ba2bd8',
    user_id: '8de69c90-df9a-4c70-8525-bd4192077e06',
    product_id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
    amount: 1,
    status: 1,
    delivery_date: null,
    order_date: '2021-08-26T20:05:41.707249',
    id: 'd4da54ee-e834-4aca-affb-cb7906cf68fb',
    product:
     { ean_code: '420',
       classification_number: '420',
       name: 'Medicinal Marihuana',
       description: 'DESCRIPTION',
       price: 0,
       pharma_indications: 'INDICATIONS',
       type_of_material: 0,
       magnitude: 0,
       laboratory: 'LABORATORY',
       id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
       type: 'drugs' } },
  { pharmacy_id: '90550ff5-15d7-4bce-838f-03a437ba2bd8',
    user_id: '8de69c90-df9a-4c70-8525-bd4192077e06',
    product_id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
    amount: 1,
    status: 1,
    delivery_date: null,
    order_date: '2021-08-26T20:05:41.648224',
    id: '2273ea67-1e07-4b05-ab09-de05269cba0a',
    product:
     { ean_code: '420',
       classification_number: '420',
       name: 'Medicinal Marihuana',
       description: 'DESCRIPTION',
       price: 0,
       pharma_indications: 'INDICATIONS',
       type_of_material: 0,
       magnitude: 0,
       laboratory: 'LABORATORY',
       id: '8c40a6b2-8fdd-4d9c-af7d-db6686433607',
       type: 'drugs' } } ]
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