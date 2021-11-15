<template>
  <div class="pannels">
     <owner-list :owners="[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6)]"></owner-list>
     <unverified-pharma> </unverified-pharma>
     <div class="data">
       <h1>Datos</h1>
       <span><b>Usuarios: </b>42069</span>
       <span><b>Farmacias verificadas: </b>420</span>

     </div>
    </div> 
</template>

<script>
import OwnerList from "../../components/OwnerList";
import UnverifiedPharma from "../../components/UnverifiedPharma";


export default {
  name: "DashboardAdmin",
  components: {
    OwnerList,
    UnverifiedPharma,
  },
  methods: {},
  async created() {
    this.$store.dispatch("updateCurrentUser");
    this.$store.dispatch("updateUnverifiedOwners");
    this.$store.dispatch("updatePharmacies");
  },
};
</script>

<style  scoped>

.pannels{
  display: flex;
  flex-direction: row;
  padding: 1.5% 2.5% 1.5% 2.5%;
  gap: 2%;
}
.data{
  width: 20%; 
  height: 20%;
  padding: .5em; 
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  text-align: justify;
  border-radius: 20px;
}
h1{
		font-size: 1.5em;
	}
</style>
