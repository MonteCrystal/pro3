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
        <RecordList></RecordList>
        <div style="margin: 15px 0;"></div>
        <el-button id="create_report" type="primary" @click="genRecord">创建报告</el-button>
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
import RecordList from "@/components/RecordList";
export default {
  name: "MainPage",
  components: {RecordList, DisplayHeader, DisplayFooter, ReportMenu},
  methods:{
    genRecord(){
      this.$router.push('/main/upload')
    }
  }
}
</script>

<style>

#create_report{
  border-radius: 100px;
  background-color: #B6E3E3;
  border: 0px;
}

</style>