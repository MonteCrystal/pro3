<template>
  <div id="app" @click="clicked">
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
  margin-top: 10px;
  height: 100%;
}

.boundary {
  /*border-style: dashed;*/
  border-style: solid;
  border-color: #d3dce6;
  border-width: 0.5px;
  border-radius: 100px;
}
</style>
