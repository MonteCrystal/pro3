<template>
  <el-container>
    <el-table
        :data="queryList"
        stripe
        style="width: 100%">
      <el-table-column label="输入">
        <template slot-scope="scope">
          <div class="demo-image__preview">
            <el-image
              :src="scope.row.input_addr"
              :preview-src-list="srcList">
            </el-image>
          </div>
<!--          <img :src="scope.row.input_addr"/>-->
        </template>
      </el-table-column>
      <el-table-column label="输出">
        <template slot-scope="scope">
          <div class="demo-image__preview">
            <el-image
              :src="scope.row.output_addr"
              :preview-src-list="srcList">
            </el-image>
          </div>
<!--          <img :src="scope.row.output_addr"/>-->
        </template>
      </el-table-column>
      <el-table-column
          prop="algo_link"
          label="科普链接">
        <template slot-scope="scope">
          <el-link type="primary" :href="scope.row.algo_link">疾病科普链接</el-link>
        </template>
      </el-table-column>
    </el-table>
  </el-container>
</template>

<script>
export default {
  name: "QueryList",
  props:{
    record_id:{
      type: String,
      required: true
    }
  },
  data() {
    this.getQueryList()
    return {
      queryList: this.queryList,
      srcList: []
    }
  },
  methods:{
    getQueryList(){
      let that = this
      that.axios({
        method: 'post',
        url: '/main/record/getQueryList',
        data:{
          recordId: this.record_id,
        }})
      .then(res=>{
        that.queryList = res.data['queryList']
        that.queryList.forEach((query)=>{
          that.srcList.push(query.input_addr)
          that.srcList.push(query.output_addr)
        })
      }).catch(function(error){
        console.log(error)
      })
    },
  }
}
</script>

<style scoped>

</style>

<!--<div class="set">-->
<!--    <el-row :gutter="10">-->
<!--      <el-col :span="10">-->
<!--        <img src="../assets/1.png" height="355" width="355"/>-->
<!--      </el-col>-->
<!--      <el-col :span="11">-->
<!--        <img src="../assets/img_1.png" height="380" width="355"/></el-col>-->
<!--      <el-col :span ="3">-->
<!--        <el-row >-->
<!--          <el-link href="https://h5.baike.qq.com/mobile/home.html?VNK=6ba27963">疾病科普链接</el-link>-->
<!--        </el-row>-->
<!--      </el-col>-->
<!--    </el-row>-->
<!--    <el-divider></el-divider>-->
<!--  </div>-->


<!--'algo_name': algo.name,-->
<!--'algo_desc': algo.description,-->
<!--'algo_link': algo.link,-->
<!--'input_addr': -->
<!--'output_addr': -->

<!--<img :src="`data:image/png;base64,${scope.row.output_addr}`" width="40" height="40"/>-->