<template>
  <div id="app" @click="clicked" class="bg" :style="bg">
    <router-view/>
  </div>
</template>

<script>
// import {jQuery} from '../jquery-3.6.0'
import $ from 'jquery'
export default {
  name: 'App',
  components: {},
  data() {
    return{
      bg:{
        backgroundImage: "url(" + require("/imed_bg.png") + ")",
        backgroundRepeat: "no-repeat",
        backgroundSize: "100% 100%",
      }
    }
  },
  methods:{
    clicked(){
    }
  },
  mounted(){
    const that = this;
    let lastTime = new Date().getTime();
    let currentTime = new Date().getTime(); // 单位是毫秒
    const HOUR_OUT = 1; // 1小时后过期
    const timeOut = HOUR_OUT * 60 * 60 * 1000;
    $(function (){
      $(document).mouseover(function (){
        lastTime = new Date().getTime();
      });
    });

    function testTime(){
      currentTime = new Date().getTime();
      if(currentTime - lastTime > timeOut){
        localStorage.removeItem('Authorization');
        console.log('timeout')
        that.$router.push('/login'); // redundant navigation 不用管它，也可.catch(err=>err);
      }
    }

    window.setInterval(testTime, 1000);
  }
}
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  margin: -8px -8px auto;
  width: 100%;
  position: fixed;
}

.el-header, .el-footer{
  background-color: #D3EFF9;
  color: #000;
  line-height: 60px;
}

.el-aside {
  height: 230px;
  color: #000;
  background-color: #CAD5FD;
  max-width: 50%;
}

#outmost_container{
   min-height: 100%;
}

#record_table{
  padding: 10px;
  border: 1px double #B6CBE3;
  border-radius: 15px;
}

#personal_description{
  padding: 15px;
  border: 1px double #B6CBE3;
  border-radius: 15px;
}

</style>
