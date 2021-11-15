<template>
    <div class="unverified-pharma">
        <unverified-pharma-doc> </unverified-pharma-doc>
        <unverified-pharma-info/>
         <p>
			Contrary to popular belief, Lorem Ipsum is not simply random text. It has
			roots in a piece of classical Latin literature from 45 BC, making it over
			2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney
			College in Virginia, looked up one of the more obscure Latin words,
			consectetur, from a Lorem Ipsum passage, and going through the cites of
			the word in classical literature, discovered the undoubtable source. Lorem
			Ipsum comes from sections 1.10.32.
		</p>
        <div class="buttons"> 

            <Button color='red'>Eliminar</Button>
            <Button color='green'>Validar</Button>
        </div>
        
    </div>
    
</template>

<script>

import UnverifiedPharmaDoc from "../components/UnverifiedPharmaDoc.vue"
import Button from './Button.vue';
import UnverifiedPharmaInfo from './UnverifiedPharmaInfo.vue';
export default {
    name: 'UnverifiedPharma', 
    components: {
        UnverifiedPharmaDoc,
        UnverifiedPharmaInfo,
        Button,
    }
}
</script>

<style scoped>

.unverified-pharma{
    display: flex;
    flex-direction: column;
    background-color: #f5f5f5;
    padding: 1% 1.5% 1% 1.5%; 
    border-radius: 15px;
    gap: .5em; 
    width: 60%; 
}
.buttons{
    display: flex;
    align-items: center;
    justify-content: space-evenly;
}

p{width: 80%;}

</style>