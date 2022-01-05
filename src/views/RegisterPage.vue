<template>
  <div id="main-pane">
    <el-row id="head_row" class="boundary">
      <div class="titletext">
        <p id="head_text">多疾病多模态辅助诊断云平台</p>
      </div>
    </el-row>

    <el-col :span="12" :offset="6" id="pad">
      <el-row class="boundary" id="pad_row">
        <el-row>
          <p id="register_text">注册</p>
        </el-row>
        <el-row id="registerForm">
            <RegisterForm></RegisterForm>
        </el-row>
      </el-row>
    </el-col>

  </div>
</template>

<script>
import RegisterForm from "@/components/RegisterForm";

export default {
  name: "RegisterPage",
  components: {
    RegisterForm
  },
  data() {
    return {}
  },

  methods: {},
  computed: {}
}
</script>

<style scoped>

#main-pane {
  margin: 6px;
  width: calc(100% - 12px);
  height: calc(100% - 12px);
}

#head_row{
  width: 100%;
  height: calc(17%);
  overflow: hidden;
}

#head_text{
  vertical-align: center;
  text-align: center;
  transform: translateY(-15px);
  font-size: 25px;
  letter-spacing: 3px;
}

.titletext {
  font-size: 20px;

  border-radius: 100px;
  list-style-type: none;

  background: #B6CBE3;
  height: 50px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  color: #ffffff;
  text-align: center;
}

#pad{
  background-color: #D3EFF9;
  border-radius: 50px;
  width: 70%;
  margin-left: 15%;
}

#pad_row{
  width: 100%;
  height: calc(80% - 10px);
  overflow: hidden;
  margin-top: 20px
}

#register_text{
  font-size: 30px;
  color: white;
  text-shadow: 1px 1px 10px #999
}

#registerForm{
  width: 90%;
  height: 90%;
  padding-left: 10%;
  padding-bottom: 10%;
  background-color: transparent;
}

</style>