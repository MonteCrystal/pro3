<template>
  <el-col>
    <h5>目录</h5>
    <el-menu :router=true
             :default-active="this.$route.path"
             active-text-color="#fff">
      <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
        {{ item.navItem }}
      </el-menu-item>
    </el-menu>
  </el-col>
</template>

<script >
export default {
  name: "ReportManu",
  data() {
    return {
      navList:[
        {name:'/main', navItem:'我的报告'},
        {name:'/main/datalist',navItem:'我的数据'},
        {name:'/main/personal',navItem:'个人中心'},
      ]
    };
  },
  methods: {
  }
}
</script>

<style scoped>

.el-menu{
  color: #000;
  background-color: #CAD5FD;
}

.el-menu-item.is-active{
  background-color: #B6CBE3;
}

</style>