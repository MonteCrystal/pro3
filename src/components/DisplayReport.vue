<template xmlns:el-col="http://www.w3.org/1999/html">
  <div class = "report">
    <el-header>多疾病多模态辅助诊断报告</el-header>

    <p></p>
    <p></p>

    <div class = "imfo">
      <el-descriptions title="病患信息" column="2">
        <el-descriptions-item label="用户名">王小虎</el-descriptions-item>
        <el-descriptions-item label="手机号">18100000000</el-descriptions-item>
        <el-descriptions-item label="居住地">深圳市</el-descriptions-item>
        <el-descriptions-item label="地址">学苑大道 1088号</el-descriptions-item>

        <el-descriptions-item label="左裸眼视力">
          <el-tag size="small">0.5</el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="右裸眼视力">
          <el-tag size="small">0.5</el-tag>
        </el-descriptions-item>


      </el-descriptions>
      <el-divider></el-divider>
    </div>


    <div class="set">
      <el-row :gutter="10">

        <el-col :span="10">
          <img src="../assets/img.png" height="355" width="355"/>
        </el-col>

        <el-col :span="11">

          <img src="../assets/img_1.png" height="380" width="355"/></el-col>

        <el-col :span ="3">
          <el-row >
            <el-link href="https://h5.baike.qq.com/mobile/home.html?VNK=6ba27963">疾病科普链接</el-link>
          </el-row>
        </el-col>

      </el-row>
      <el-divider></el-divider>
    </div>

    <div class="set">
      <el-row :gutter="10">
        <el-col :span="12">

          <img src="../assets/21_training.png" height="584" width="565"/></el-col>

        <el-col :span="10">
          <img src="../assets/21_manual1.gif" height="584" width="565"/></el-col>

        <el-col :span ="2">
<!--          <el-link>链接</el-link>-->
        </el-col>
      </el-row>
      <el-divider></el-divider>
    </div>

    <div class = "describe">
      <el-descriptions title="症状" column="1">
        <el-descriptions-item label="左眼"><i class="el-icon-brush"></i></el-descriptions-item>
        <el-descriptions-item label="右眼"><i class="el-icon-edit"></i></el-descriptions-item>
      </el-descriptions>
      <el-divider></el-divider>
    </div>

    <div class = "describe">
      <el-descriptions title="诊断结果" column="1">
        <el-descriptions-item label="左眼"><i class="el-icon-brush"></i></el-descriptions-item>
        <el-descriptions-item label="右眼"><i class="el-icon-edit"></i></el-descriptions-item>
      </el-descriptions>
      <el-divider></el-divider>
    </div>

    <div class = "describe">
      <el-descriptions title="就医意见" column="1">
        <el-descriptions-item label="左眼"><i class="el-icon-brush"></i></el-descriptions-item>
        <el-descriptions-item label="右眼"><i class="el-icon-edit"></i></el-descriptions-item>
      </el-descriptions>
    </div>


    <div class = "note">

      <el-descriptions column="1">
      <el-descriptions-item label="备注">
          <el-tag size="small">以上诊断结果皆由算法自动生成</el-tag>
        </el-descriptions-item>
      </el-descriptions>
    </div>


  </div>
</template>

<script>
export default {
  name: "DisplayReport"
}


<style scoped>

</style>