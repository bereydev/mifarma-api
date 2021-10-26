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
  <div class="register">
    <h1>Mi perfil</h1>
    <div class="small-text">¿Ya tiene cuenta? Acceda aquí </div>
    <div>
      <i class="material-icons">person</i>
    </div>
    <div class="double-field">
      <div class="text-field">Nombre</div>
      <div class="text-field">Apellido</div>
    </div>
    <div class="text-field">Email</div>
    <div class="text-field">Dirección</div>
    <div class="double-field">
      <div class="text-field">Código Postal</div>
      <div class="text-field">Ciudad</div>
    </div>
    <div class="double-field">
      <div class="text-field">Contraseña</div>
      <div class="text-field">Repita la contraseña</div>
    </div>
    <div class="green-button">Confirmar</div>
  </div>
</body>

</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body{
  margin:0; 
  font-family: Roboto;
  font-size:1em; 
  color: #2E2931; 
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



.small-text{
  padding: 0.75em 0em 1.5em 0em; 
  font-size:0.8em; 
  color:#766B69; 
  text-decoration: underline;
}


.register{
  margin: 2.5% 33% 10% 33%; 
  display: flex; 
  flex-direction:column; 
  align-items: center;
  justify-content: center;
  gap:0.25em; 
}

.double-field{
  box-sizing: border-box;
  padding:0; 
  margin:0; 
  display:flex; 
  gap:5%; 
  width: 100%; 
  align-items: center;
  justify-content: center;
}

.text-field{
  box-sizing: border-box;
  margin: 0.35em 0em 0.35em 0em; 
  padding: 0.5em 1em 0.5em 1em; 
  border-radius: 30px;
  background-color:white; 
  border: 2px solid #ADADAD;
  justify-content:flex-start; 
  text-align: start;
  color: #B1B1B1; 
  width: 100%; 
}

.green-button{
   
  display:flex; 
  margin: 1em 0em 0.5em 0em; 
  padding: 0.5em 1em 0.5em 1em; 
  border-radius: 30px;
  justify-content: center;
  align-items: center;
  width: 50%; 
  font-size: 1.25em; 
  background-color: #00DD7C; 
  box-shadow: 0px 3px 6px -3.5px gray;
  
}


</style>