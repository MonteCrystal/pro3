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
        v-model="checkedImages"
        @change="handleCheckedImagesChange">
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
          v-for="aimg in imgs"
          :label="aimg.id"
          :key="aimg.id">
        <img :src="aimg.filename"/>
      </el-checkbox>
    </el-checkbox-group>
  </div>
</template>

<script>
import Bus from '@/api/bus'
export default {
  data() {
    return {
      checkAll: false,
      checkedImages: [],
      imgs: [],
      isIndeterminate: false
    };
  },
  methods: {
    handleCheckAllChange(val) {
      this.checkedImages = []
      if(val){
        for(var i = 0; i < this.imgs.length;i++){
          this.checkedImages.push(this.imgs[i].id)
        }
      }
      // this.checkedImages = val ? this.imgs : [];
      this.isIndeterminate = false;
      this.$forceUpdate();
    },
    handleCheckedImagesChange(val) {
      let checkedCount = val.length;
      this.checkAll = checkedCount === this.imgs.length;
      this.isIndeterminate = checkedCount > 0 && checkedCount < this.imgs.length;
      this.$forceUpdate();
    },
  },
  mounted (){
    const that = this;
    Bus.$on('filearr', message=>{
      that.imgs=that.imgs.concat(message)
    })
  }
};
</script>

<style>

</style>