<template>
  <div style="text-align: left;line-height: 60px;height;" >
    <!-- <el-tag>标签一</el-tag>
    <el-tag type="success">标签二</el-tag>
    <el-tag type="info">标签三</el-tag>
    <el-tag type="warning">标签四</el-tag>
    <el-tag type="danger">标签五</el-tag> -->

  </div>
</template>

<script>
export default {
  name: "DisplayFooter",
  data() {
    return {
      value: null,
      iconClasses: ['icon-rate-face-1', 'icon-rate-face-2', 'icon-rate-face-3'] // 等同于 { 2: 'icon-rate-face-1', 4: { value: 'icon-rate-face-2', excluded: true }, 5: 'icon-rate-face-3' }
    }
  }
}
</script>

<style scoped>

</style>