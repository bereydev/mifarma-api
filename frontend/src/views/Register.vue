<template>
<body>
 <div class="topNavBar">
    <img src="https://images.unsplash.com/photo-1566710601154-5e04b1a63536?crop=entropy&cs=srgb&fm=jpg&ixid=MnwxNDU4OXwwfDF8cmFuZG9tfHx8fHx8fHx8MTYzNDU3ODk1MA&ixlib=rb-1.2.1&q=85" alt="MiFarmacia logo">

    <div id="brandName" class="navBarElement">MiFarmacia</div>
    <spacer></spacer>
    <div class="navBarElement">Soy una farmacia</div>
    <div class="navBarElement">Contacto</div>
    <div id="access" class="navBarElement">Acceso</div>
  </div>

  <RegisterForm/>
  
</body>

</template>

<script>

import RegisterForm from '../components/RegisterForm.vue'

export default {
  name: 'Register', 
  components: {
    RegisterForm
  }, 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body{
  margin:0; 
  
}
  #brandName{
    font-size: 1.5em;
    font-weight: bold; 
    
  }

  .navBarElement{
    color: #2E2931; 
    align-self: center; 
    justify-self:center; 
    font-size: 1em;
    flex: 1 0 auto; 
    
  }

.material-icons{
  color: #2E2931; 
  border: 2px solid #ADADAD; 
  border-radius: 100%; 
  padding: 0.05em; 
  font-size:6em !important; 
}

  #access{
    padding: 0.5em 1em 0.5em 1em; 
    background-color: #2E2931; 
    border-radius: 38px;
    color: white; 
    justify-content:center; 
    box-shadow: 0px 3px 6px -3.5px grey;
  }

spacer{
  flex: 100 100 auto; 
}


  .topNavBar {
    box-sizing: border-box;
    padding: 0.25em 1.5em 0.25em 1em; 
    font-size:1.15em; 
    height: 3.5em;
    width: 100%;
    background: #F5F5F5;
    display: flex; 
    gap: 1em; 
    align-content:center; 
  }



h1{
  font-size:2em; 
  margin-block-start: 0px;
  margin-block-end: 0px;
}




</style>