<template>
  <el-container id="outmost_container">
    <el-aside>
      <DisplayMenu></DisplayMenu>
    </el-aside>
    <el-container>
      <el-header>
        <DisplayHeader></DisplayHeader>
      </el-header>
      <el-main>
        <AlgorithmForm></AlgorithmForm>
      </el-main>
      <el-footer>
        <DisplayFooter></DisplayFooter>
      </el-footer>
    </el-container>

  </el-container>
</template>

<script>
import DisplayMenu from "../components/DisplayMenu";
import DisplayFooter from "../components/DisplayFooter";
import DisplayHeader from "../components/DisplayHeader";
import AlgorithmForm from "@/components/AlgorithmForm";
export default {
  name: "AlgorithmPage",
  components: {AlgorithmForm, DisplayHeader, DisplayFooter, DisplayMenu}
}
</script>

<style>

</style>