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
        <PersonalForm></PersonalForm>
      </el-main>
      <el-footer>
        <DisplayFooter></DisplayFooter>
      </el-footer>
    </el-container>
  </el-container>
</template>

<script>
import DisplayHeader from "@/components/DisplayHeader";
import DisplayFooter from "@/components/DisplayFooter";
import ReportMenu from "@/components/DisplayMenu";
import PersonalForm from "@/components/PersonalForm"
export default {
  name: "PersonalPage",
  components: {DisplayHeader, DisplayFooter, ReportMenu, PersonalForm},
}
</script>

<style scoped>

</style>