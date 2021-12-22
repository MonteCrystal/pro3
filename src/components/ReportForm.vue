<template>
  <div>
    <el-table
        :data="recordList"
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
        <template slot-scope="scope">
          <el-button @click="openClick(scope.row.link)">打开</el-button>
        </template>
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
    this.getRecordList()
    return {
      value: false,
      recordList: []
      // {date: '2016-05-02',
      //  name: '王小虎',
      //  note: '样例报告',
      //  link: 'LinkToReport'}
    }
  },
  methods: {
    openClick(link) {
      this.$router.push('/main/report/' + link)
    },
    getRecordList(){
      // let token = localStorage.getItem('Authorization')
      // console.log("token==>")
      // console.log(token)
      let that = this
      this.axios.get('/main/getRecordList')
      .then(function(response){
        that.recordList = response.data['recordList']
      }).catch(function(error){
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>