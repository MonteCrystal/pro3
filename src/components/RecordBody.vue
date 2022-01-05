<template xmlns:el-col="http://www.w3.org/1999/html">
  <div class = "report">
    <el-header>多疾病多模态辅助诊断报告</el-header>

    <p></p>
    <p></p>

    <div class = "info">
      <el-descriptions title="病患信息" :column="2">
        <el-descriptions-item label="用户名">{{userInfo.name}}</el-descriptions-item>
        <el-descriptions-item label="年龄">{{userInfo.age}}</el-descriptions-item>
        <el-descriptions-item label="性别">{{userInfo.gender}}</el-descriptions-item>
        <el-descriptions-item label="左裸眼视力">
          <el-tag size="small">{{userInfo.left_eyesight}}</el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="右裸眼视力">
          <el-tag size="small">{{userInfo.right_eyesight}}</el-tag>
        </el-descriptions-item>
      </el-descriptions>
    </div>
    <el-divider></el-divider>
    <div class = "record_info">
      <el-descriptions title="报告内容">
        <el-descriptions-item label="报告编号">{{record_id}}</el-descriptions-item>
      </el-descriptions>
    </div>
    <el-divider></el-divider>
    <QueryList v-bind:record_id="record_id"></QueryList>

<!--    <div class = "describe">-->
<!--      <el-descriptions title="症状" :column="1">-->
<!--        <el-descriptions-item label="左眼"><i class="el-icon-brush"></i></el-descriptions-item>-->
<!--        <el-descriptions-item label="右眼"><i class="el-icon-edit"></i></el-descriptions-item>-->
<!--      </el-descriptions>-->
<!--      <el-divider></el-divider>-->
<!--    </div>-->
    <el-divider></el-divider>
    <div class = "note">
      <el-descriptions :column="1">
      <el-descriptions-item label="备注">
          <el-tag size="small">以上诊断结果皆由算法自动生成</el-tag>
        </el-descriptions-item>
      </el-descriptions>
    </div>


  </div>
</template>

<script>
import QueryList from "@/components/QueryList";
export default {
  name: "RecordBody",
  components: {QueryList},
  props:{
    record_id:{
      type: String,
      required: true
    }
  },
  data(){
    this.getUserInfo()
    return{
      userInfo: this.userInfo
    }
  },
  methods:{
    getUserInfo(){
      let that = this
      that.axios({
        method: 'get',
        url: '/main/getUserInfo'
      })
      .then(res=>{
        that.userInfo = res.data['user']
      }).catch(function(error){
        console.log(error)
      })
    },
  }
}
</script>


<style scoped>

</style>