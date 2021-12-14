<template>
  <div>
    <el-table
        :data="tableData"
        style="width: 100%">
      <el-table-column
          prop="date"
          label="日期"
          width="180">
      </el-table-column>
      <el-table-column
          prop="name"
          label="姓名"
          width="180">
      </el-table-column>
      <el-table-column
          prop="note"
          label="备注">
      </el-table-column>
      <el-table-column>
        <el-button @click="openClick">打开</el-button>
      </el-table-column>

    </el-table>
    <el-pagination
        :hide-on-single-page="value"
        :total="5"
        layout="prev, pager, next">
    </el-pagination>
  </div>
</template>

<script>
export default {
  name: "ReportForm",
  data() {
    return {
      value: false,
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        note: '诊断报告1'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        note: '诊断报告2'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        note: '诊断报告3'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        note: '诊断报告4'
      }]
    }
  },
  methods: {
    openClick() {
      this.$router.push('/main/report')

    }
  }
}
</script>

<style scoped>

</style>