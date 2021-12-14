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
                    margin: 0px;display:
                    inline-grid;
                    white-space: pre-line;
                    word-wrap: break-word;
                    overflow: hidden;
                    "
              border=true
              v-for="algo in algorithms" 
              :label="algo" 
              :key="algo">
              {{algo}} 
          </el-checkbox>
      </el-checkbox-group>

      <div style="margin: 30px 0;"></div>
<!--      <el-upload-->
<!--        class="upload"-->
<!--        action="https://jsonplaceholder.typicode.com/posts/"-->
<!--        :on-preview="handlePreview"-->
<!--        :on-remove="handleRemove"-->
<!--        :before-remove="beforeRemove"-->
<!--        multiple-->
<!--        :limit="1"-->
<!--        :on-exceed="handleExceed"-->
<!--        :on-success="handleSuccess"-->
<!--        :file-list="dataList">-->
<!--        <el-button  type="primary" @click="uploadSectionFile">点击上传</el-button>-->
<!--        <div slot="tip" class="el-upload__tip">只能上传jpg/png/txt文件，且不超过500kb</div>-->
<!--      </el-upload>-->
<!--                 <el-dialog :title="addName" :visible.sync="dialogAddFile" width="500px" style="padding:0;" @close="resetAdd">-->
<!--               附件名称：<el-input v-model="addFileName" autocomplete="off" size="small" style="width: 300px;" ></el-input>-->
<!--                <div class="add-file-right" style="height:70px;margin-left:100px;margin-top:15px;">-->
<!--                    <div class="add-file-right-img" style="margin-left:70px;">上传文件：</div>-->
<!--                    <input type="file" ref="clearFile" @change="getFile($event)" multiple="multiplt" class="add-file-right-input" style="margin-left:70px;" accept=".docx,.doc,.pdf">-->
<!--                    <span class="add-file-right-more">支持扩展名：.doc .docx .pdf </span>-->
<!--                </div>-->
<!--                <div class="add-file-list">-->
<!--                    <ul>-->
<!--                        <li v-for="(item, index) in addArr" :key="index"><a >{{item.name}}</a></li>-->
<!--                    </ul>-->
<!--                </div>-->
<!--                <div slot="footer" class="dialog-footer">-->
<!--                    <el-button type="primary" @click="submitAddFile" size="small">开始上传</el-button>-->
<!--                    <el-button @click="resetAdd" size="small">全部删除</el-button>-->
<!--               </div>-->
<!--            </el-dialog>-->
          <el-upload ref="upfile"
                     class = "upload"
                style="display: inline"
                :auto-upload="false"
                :file-list="dataList"
                     :on-preview="handlePreview"
        :on-remove="handleRemove"
        :before-remove="beforeRemove"
        multiple
        :limit="1"
        :on-exceed="handleExceed"
                action="https://jsonplaceholder.typicode.com/posts/">
                <el-button  type="success">选择文件</el-button>
            </el-upload>
      <div style="margin: 20px 0;"></div>
      <el-button  type="primary" @click="upload">点击上传</el-button>
      <div slot="tip" class="el-upload__tip">只能上传jpg/png/txt文件，且不超过500kb</div>


      <div style="margin: 30px 0;"></div>
      <el-button type="primary" @click="runAlgo">生成报告</el-button>
    </div>
</template>

<script>
import {uploadFile} from '@/api/file'

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
        dataList: [],
        uploadParams: {}
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
      handleRemove(file, dataList) {
        console.log(file, dataList);
      },
      handlePreview(file) {
        console.log(file);
      },
      handleExceed(files, dataList) {
        this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + dataList.length} 个文件`);
      },
      beforeRemove(file) {
        return this.$confirm(`确定移除 ${ file.name }？`);
      },
      handleChange(file, dataList) {
        this.dataList = dataList;
        console.log(dataList)
      },
      upload(){
        // var fd = new FormData();
        this.uploadParams['name']="name";
        // fd.append("name",this.name);
            this.dataList.forEach(item=>{
                //文件信息中raw才是真的文件
              // this.uploadParams['files'] = item.raw;
              this.uploadParams['files'] = item;
                // fd.append("files",item.raw);
                //console.log(item.raw)
            })
            uploadFile(this)


      },
      runAlgo(){
        this.$router.push('/main/algo')
      }
    }
  };
</script>

<style>

.cont {
  height: 80vh;
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