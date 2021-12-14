<template>
  <div>
    <el-descriptions title="A功能信息" column="1">
      <el-descriptions-item label="功能概述"></el-descriptions-item>
      <el-descriptions-item label="主输入模态"></el-descriptions-item>
      <el-descriptions-item label="次输入模态"></el-descriptions-item>
      <el-descriptions-item label="输出模态"></el-descriptions-item>
    </el-descriptions>

    <el-descriptions title="B功能信息" column="1">
      <el-descriptions-item label="功能概述"></el-descriptions-item>
      <el-descriptions-item label="主输入模态"></el-descriptions-item>
      <el-descriptions-item label="次输入模态"></el-descriptions-item>
      <el-descriptions-item label="输出模态"></el-descriptions-item>
    </el-descriptions>

    <el-divider></el-divider>
    <el-button @click="reportList">确认生成报告</el-button>
  </div>
</template>

<script>
export default {
  name: "AlgorithmForm",
  methods:{
    reportList(){
      this.$router.push('/main')
    }
  }
}
</script>

<style scoped>

</style>