<template>
  <el-container id="outmost_container">
    <el-aside>
      <ReportMenu></ReportMenu>
    </el-aside>
    <el-container>
      <el-header>
        <DisplayHeader></DisplayHeader></el-header>
      <el-main>
        <el-container direction="vertical"
                      style="border: 2px dashed #fff;
                             border-radius: 10px">
          <ImageUploader @filearr="$refs['getfiles'].reload()"></ImageUploader>

          <div style="margin: 5px 0;"></div>

          <UploadedList ref="getfiles"></UploadedList>
        </el-container>
        <div style="margin: 15px 0;"></div>

        <el-container style="border: 2px dashed #fff;
                             border-radius: 10px">
          <AlgorithmList ref="getalgos"></AlgorithmList>
        </el-container>

        <el-button type="primary" @click="generateRecord">生成报告</el-button>
      </el-main>
      <el-footer>
        <DisplayFooter></DisplayFooter>
      </el-footer>
    </el-container>

  </el-container>
</template>

<script>
import ReportMenu from "../components/DisplayMenu";
import DisplayHeader from "@/components/DisplayHeader";
import DisplayFooter from "@/components/DisplayFooter";
import ImageUploader from "@/components/ImageUploader";
import UploadedList from "@/components/UploadedList";
import AlgorithmList from "@/components/AlgorithmList";
export default {
  name: "UploadedPage",
  components: {UploadedList,DisplayHeader, DisplayFooter, ReportMenu, ImageUploader,AlgorithmList},
  methods:{
    generateRecord(){
      this.axios({method: 'post', url:'/main/upload/genrec', data:{
        'images': this.$refs.getfiles.checkedImages,
        'algos': this.$refs.getalgos.checkedAlgorithms
      }}).then(res=>{
        this.$router.push({ path: '/main/record', query: { record_id: res.data['record_id'] }});
      }).catch((err)=>{
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>