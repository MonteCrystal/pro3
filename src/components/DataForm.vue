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
        @change="handleCheckedAlgorithmsChange">
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
          :label="algo"
          :key="algo">
        {{ algo }}
      </el-checkbox>
    </el-checkbox-group>
    <div style="margin: 30px 0;"></div>


<!--    <input type="file" ref="file2" name="check_img_url" accept="image/*" multiple="true" @change="tirggerFile($event)"/>-->
<!--    <div>-->
<!--      <img style="width:200px;height:150px;margin-left:105px" id="img1" src alt/>-->
<!--    </div>-->


    <el-button type="primary" @click="upload">上传</el-button>


    <div style="margin: 30px 0;"></div>
    <el-button type="primary" @click="runAlgo">生成报告</el-button>
  </div>
</template>

<script>
// import {uploadFile} from '@/api/file'

const algoOptions = [
  'image_01',
  'image_02',
  'image_03',
  'image_04'
];
export default {
  data() {
    return {
      checkAll: false,
      checkedAlgorithms: [],
      algorithms: algoOptions,
      isIndeterminate: false,
      dataList: []
    };
  },
  methods: {
    handleCheckAllChange(val) {
        this.checkedAlgorithms = val ? algoOptions : [];
        this.isIndeterminate = false;
    },
    handleCheckedAlgorithmsChange(val) {
      let checkedCount = val.length;
      this.checkAll = checkedCount === this.algorithms.length;
      this.isIndeterminate = checkedCount > 0 && checkedCount < this.cities.length;
    },
      runAlgo(){
        this.$router.push('/main/algo')
      },
    update(e) {
      // let file = e.target.files[0];
      let param = new FormData();//创建form对象
      param.append('file', e.target.files[0]);//通过append向form对象添加数据
      param.append('file', e.target.files[1]);//通过append向form对象添加数据
      // console.log(param.get('file')); //FormData私有类对象，访问不到，可以通过get判断值是否传进去
      this.axios({method: 'post', url: '/update', data: param})
          .then(
              response => {
                console.log(response.data);
                this.$message('上传成功');
              })
          .catch(function (error) {
            console.log(error);
          })

    },
    upload() {
      this.axios({method: 'post', url: '/upload'})
      .then(
        response => {
          console.log(response.data);
          if (response.data['code'] === 200) {
            this.$message('上传成功')
          }

        })
      .catch(function (error) {
        console.log(error);}
    )}
  }
};
</script>

<style>

.cont {

}

.el-checkbox.is-bordered {
  padding: 9px 20px 9px 10px;
  border-radius: 4px;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  line-height: normal;
  height: 40px;
  background: white;
}

</style>

