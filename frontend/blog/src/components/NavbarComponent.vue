
<script setup>

</script>


<template>
  <header class="header">
    <nav class="navbar">
      <div class="nav-container">
        <div class="nav-item">Posts</div>
        <div class="nav-item">My Blog</div>
        <div class="nav-item">Profile</div>
      </div>
    </nav>

  </header>

</template>


<style scoped>

.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 9vh;
  z-index: 100;
  background-color: white;
  -webkit-box-shadow: 10px 10px 16px -19px rgba(0,0,0,0.75);
  -moz-box-shadow: 10px 10px 16px -19px rgba(0,0,0,0.75);
  box-shadow: 10px 10px 16px -19px rgba(0,0,0,0.75);
}
.navbar {
  height: 100%;
  padding: 0 15px 0 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: end;
  -webkit-box-shadow: 10px 10px 16px -19px rgba(0,0,0,0.75);
  -moz-box-shadow: 10px 10px 16px -19px rgba(0,0,0,0.75);
  box-shadow: 10px 10px 16px -19px rgba(0,0,0,0.75);
}
.nav-container {
  width: auto;
  display: flex;
  flex-direction: row;
}
.nav-item {
  background-color: whitesmoke;
  padding: 10px 20px;
  height: 20px;
  margin: 0 5px;
  line-height: 20px;
  color: black;
  font-weight: bold;
  letter-spacing: 1px;
  font-size: 1em;
  text-align: center;
  transition: background-color 200ms;
}
.nav-item:hover {
  background-color: lightgrey;
  cursor: pointer;
  border-bottom: 1px solid black;
  height: 19px;
}


</style>