<template>
  <el-container id="outmost_container">
    <el-aside>
      <ReportMenu></ReportMenu>
    </el-aside>
    <el-container>
      <el-header>
        <DisplayHeader></DisplayHeader>
      </el-header>
      <el-main>
      </el-main>
      <el-footer>
        <DisplayFooter></DisplayFooter>
      </el-footer>
    </el-container>
  </el-container>
</template>
<script>
import ReportMenu from "../components/DisplayMenu";
import DisplayFooter from "../components/DisplayFooter";
import DisplayHeader from "../components/DisplayHeader";
export default {
  name: "DataPage",
  components: {DisplayHeader, DisplayFooter, ReportMenu},
  methods:{
  }
}
</script>

<style>

</style>