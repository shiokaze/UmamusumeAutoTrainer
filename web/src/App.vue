<template>
  <div id="app" >
    <div class="container-fluid">
      <div id="nav">
      </div>
      <router-view/>
    </div>
  </div>
</template>
<script>
export default {
  name: 'App',
  components: {},
  data:function(){
    return{
      error:'',
      success:'',
      info:'',
    }
  },
  mounted (){

  },
  watch:{

  }
}
</script>
<style>
html,body{
  height: 100%;
}
.card-title{
  margin-bottom: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  color: #2c3e50;
}

#nav {
  padding: 8px;
  text-align: center;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #0faedf;
}

body{
  background-color: #f0f1f5;
  font-size: 16px !important;
  color: #495057;
}

.card{
  border:0 !important;
}

.card-body{
  padding: 10px;
}

.auto-btn{
  background-color: #0faedf;
  color: white;
  cursor: pointer;
  opacity: 0.8;
  transition:opacity .3s;
}


.btn{
  padding: 0.2rem 0.4rem !important;
  font-size: 0.75rem !important;
}



.auto-btn:hover{
  color: white;
  cursor: pointer;
  opacity: 1.0;
}

.auto-btn-red{
  background-color: #dc3545;
  opacity: 0.8;
  color: white;
  cursor: pointer;
  transition:opacity .3s;
}

.auto-btn-red:hover{
  color: white;
  cursor: pointer;
  opacity: 1.0;
}

.auto-btn-orange{
  background-color: #fd7e14;
  opacity: 0.8;
  color: white;
  cursor: pointer;
  transition:opacity .3s;
}

.auto-btn-orange:hover{
  color: white;
  cursor: pointer;
  opacity: 1.0;
}

.auto-btn-green{
  background-color: #28a745;
  opacity: 0.8;
  color: white;
  cursor: pointer;
  transition:opacity .3s;
}

.auto-btn-green:hover{
  color: white;
  cursor: pointer;
  opacity: 1.0;
}

.form-control:focus,
.form-control:active:focus,
.form-control.active:focus,
.form-control.focus,
.form-control:active.focus,
.form-control.active.focus{
  outline: none;
  box-shadow:none;
}

.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: none;
  box-shadow:none
}

a{
  color: inherit;
  font-size: inherit;
  text-decoration: none;
}
a:hover{
  cursor: pointer;
  color: #1e88e5 !important;
  text-decoration: none;
}

.modal-footer{
  border-top: 0;
}

.auto-hide-toast{
  top: -70px;
  opacity: 1;
}
.auto-show-toast{
  top:0;
  opacity: 1;
}
.part+.part{
  margin-top: 10px;
}
.card-title{
  /*font-weight: 600;*/
  text-align: center;
}

</style>
