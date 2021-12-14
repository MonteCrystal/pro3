<template>
  <el-container>
    <el-aside  width="200px" style="background-color: rgb(238, 241, 246)">
      <DisplayMenu></DisplayMenu>
    </el-aside>
    <el-container>
      <el-header height="60px">
        <DisplayHeader></DisplayHeader></el-header>
      <el-main>
        <DisplayReport></DisplayReport>
      </el-main>
      <el-footer>
        <DisplayFooter></DisplayFooter>
      </el-footer>
    </el-container>

  </el-container>
</template>

<script>
import DisplayReport from "../components/DisplayReport";
import DisplayMenu from "../components/DisplayMenu";
import DisplayFooter from "../components/DisplayFooter";
import DisplayHeader from "../components/DisplayHeader";
export default {
  name: "Display",
  components: {DisplayHeader, DisplayFooter, DisplayMenu, DisplayReport}
}
</script>

<style>
.el-header, .el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
  font-size: 26px;
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