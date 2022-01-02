<template>
    <div class="cont">
    <el-checkbox
        :indeterminate="isIndeterminate"
        v-model="checkAll"
        @change="handleCheckAllChange"
        style="display:block;width:30px;">
      全选
    </el-checkbox>
    <div style="margin: 15px 0;"></div>
    <el-checkbox-group
        v-model="checkedAlgorithms"
        @change="handleCheckedAlgosChange">
      <el-checkbox
          style="display:block;
                    width:100%;
                    height:20%;
                    margin: 0;
                    white-space: pre-line;
                    word-wrap: break-word;
                    overflow: hidden;
                    "
          :border=true
          v-for="algo in algorithms"
          :label="algo.id"
          :key="algo.id">
        <el-descriptions :title="algo.name"
                         :column="3">
          <el-descriptions-item label="功能概述" span="3">{{algo.description}}</el-descriptions-item>
          <el-descriptions-item label="输入模态">{{algo.input_format}}</el-descriptions-item>
          <el-descriptions-item label="输出模态">{{algo.output_format}}</el-descriptions-item>
          <el-descriptions-item label="作者">
            <el-tag size="small">{{algo.uploader}}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="上传时间">{{algo.upload_timestamp}}</el-descriptions-item>
          <el-descriptions-item label="使用次数">{{algo.used_time}}</el-descriptions-item>
          <el-descriptions-item label="疾病百科">
            <el-link type="primary" href="http://www.baidu.com">疾病百科</el-link>
          </el-descriptions-item>
        </el-descriptions>
      </el-checkbox>
    </el-checkbox-group>
  </div>
</template>

<script>
export default {
  data() {
    this.getAlgorithmList()
    return {
      checkAll: false,
      checkedAlgorithms: [],
      algorithms: [],
      isIndeterminate: false
    };
  },
  methods: {
    handleCheckAllChange(val) {
      this.checkedAlgorithms = []
      if(val){
        for(var i = 0; i < this.algorithms.length;i++){
          this.checkedAlgorithms.push(this.algorithms[i].id)
        }
      }
      //this.checkedAlgorithms = val ? this.algorithms : [];
      this.isIndeterminate = false;
    },
    handleCheckedAlgosChange(val) {
      let checkedCount = val.length;
      this.checkAll = checkedCount === this.algorithms.length;
      this.isIndeterminate = checkedCount > 0 && checkedCount < this.algorithms.length;
      this.$forceUpdate();
    },
    getAlgorithmList(){
      let that = this
      that.axios({
        method:'get',
        url:'/main/getAlgorithmList'
      })
      .then(res=>{
        that.algorithms = res.data['algorithmList']
      }).catch(function(error){
        console.log(error)
      })
    }
  }
};
</script>

<style>

</style>

<!--{//TODO 从后端获取算法列表，参考record list那一页-->
<!--'id': 1,-->
<!--'name': '基于xx的算法',-->
<!--'description':'算法描述算法描述算法描述',-->
<!--'input_format': 'PNG',-->
<!--'output_format': 'JPG',-->
<!--'uploader': '上传者用户名',-->
<!--'upload_timestamp': 'yy-MM-dd',-->
<!--'used_time': '%d次',-->
<!--'wiki': 'https://www.baidu.com'}-->