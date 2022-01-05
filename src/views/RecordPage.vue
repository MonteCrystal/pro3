<template>
  <el-container id="outmost_container">
    <el-aside>
      <DisplayMenu></DisplayMenu>
    </el-aside>
    <el-container>
      <el-header>
        <DisplayHeader></DisplayHeader></el-header>
      <el-main>
        <RecordBody v-bind:record_id="record_id"></RecordBody>
      </el-main>
      <el-footer>
        <DisplayFooter></DisplayFooter>
      </el-footer>
    </el-container>
  </el-container>
</template>

<script>
import RecordBody from "../components/RecordBody";
import DisplayMenu from "../components/DisplayMenu";
import DisplayFooter from "../components/DisplayFooter";
import DisplayHeader from "../components/DisplayHeader";
export default {
  name: "RecordPage",
  components: {DisplayHeader, DisplayFooter, DisplayMenu, RecordBody},
  data(){
    return{
        record_id: this.$route.query.record_id
    }
  }
}
</script>

<style>

</style>