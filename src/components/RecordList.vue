<template>
  <div id="record_table">
    <el-table
      :data="recordList"
      stripe
      style="width: 100%">
<!--      <el-table-column>-->
<!--        <template slot-scope="scope">-->
<!--          <img src="cover.jpg" height="200" width="250" @click="openClick(scope.row.id)"/>-->
<!--          <p>{{scope.row.date}}</p>-->
<!--          <p>{{scope.row.name}}</p>-->
<!--          <p>{{scope.row.note}}</p>-->
<!--        </template>-->
<!--      </el-table-column>-->
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
          <el-button @click="openClick(scope.row.id)">打开</el-button>
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
  name: "RecordList",
  data() {
    this.getRecordList()
    return {
      value: false,
      recordList: []
    }
  },
  methods: {
    openClick(rec_id) {
      this.$router.push({ path: '/main/record', query: { record_id: rec_id }});
    },
    getRecordList(){
      let that = this
      that.axios({
        method:'get',
        url:'/main/getRecordList'
      })
      .then(res=>{
        that.recordList = res.data['recordList']
      }).catch(function(error){
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
/*TODO*/
/*.el-table__body-wrapper{*/
/*  width: 6px;*/
/*  height: 6px;*/
/*}*/

/*::-webkit-scrollbar-thumb {*/
/*  background-color: #000;*/
/*  border-radius: 3px;*/
/*}*/

.el-button{
  border-radius: 100px;
  background-color: #B6E3E3;
  border: 0px;
  color: white;
}


</style>

<!--{date: '2016-05-02',-->
<!-- name: '王小虎',-->
<!-- note: '样例报告',-->
<!-- id: 12345}-->