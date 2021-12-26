<template>
  <el-container>
    <el-aside  width="200px" style="background-color: rgb(238, 241, 246)">
      <DisplayMenu></DisplayMenu>
    </el-aside>
    <el-container>
      <el-header>
        <DisplayHeader></DisplayHeader>
      </el-header>
      <el-main>
        <DisplayAlgorithm></DisplayAlgorithm>
      </el-main>
      <el-footer>
        <DisplayFooter></DisplayFooter>
      </el-footer>
    </el-container>

  </el-container>
    
</template>

<script>
import DisplayHeader from "../components/DisplayHeader.vue"
import DisplayAlgorithm from "../components/DataForm.vue"
import DisplayFooter from "../components/DisplayFooter.vue"
import DisplayMenu from "@/components/DisplayMenu";

export default {
    name: "DataListPage",
    components: {DisplayHeader, DisplayAlgorithm, DisplayFooter,DisplayMenu}
}
</script>

<style>
.el-header, .el-footer {
  background-color: #B3C0D1;
  color: #333;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
}

body > .el-container {
  margin-bottom: 10px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 60px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>