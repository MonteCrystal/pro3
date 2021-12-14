<template>
  <el-menu
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#B3C0D1"
      style="width: 100%"
      text-color="#fff"
      active-text-color="#ffd04b">
<!--    <el-submenu index="2">-->
<!--      <template slot="title">注释</template>-->
<!--      <el-menu-item index="2-1">选项1</el-menu-item>-->
<!--      <el-menu-item index="2-2">选项2</el-menu-item>-->
<!--      <el-menu-item index="2-3">选项3</el-menu-item>-->
<!--      <el-submenu index="2-4">-->
<!--        <template slot="title">选项4</template>-->
<!--        <el-menu-item index="2-4-1">选项1</el-menu-item>-->
<!--        <el-menu-item index="2-4-2">选项2</el-menu-item>-->
<!--        <el-menu-item index="2-4-3">选项3</el-menu-item>-->
<!--      </el-submenu>-->
<!--    </el-submenu>-->
  </el-menu>
</template>

<script>
export default {
  name: "DisplayHeader",
  data() {
    return {
      activeIndex2: '1'
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }}
</script>

<style scoped>

</style>