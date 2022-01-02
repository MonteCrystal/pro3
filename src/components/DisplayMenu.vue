<template>
  <div>
    <p>目录</p>
    <el-menu :router=true>
      <el-menu-item index='/main'>我的报告</el-menu-item>
      <el-menu-item index='/main/datalist' @click="openData">我的数据</el-menu-item>
      <el-menu-item index='/main/history' disabled>历史记录</el-menu-item>
      <el-menu-item index='/main/personal' disabled>个人中心</el-menu-item>
    </el-menu>
  </div>
</template>

<script >
export default {
  name: "ReportManu",
  data() {
    return {
      activeIndex: '/main'
    };
  },
  methods: {
    openData(){
      this.activeIndex = '/main/datalist'
    }
  }
}
</script>

<style scoped>

</style>