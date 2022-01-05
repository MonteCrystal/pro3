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
          <p id="login_text">登录</p>
        </el-row>
        <el-row id="loginForm">
            <LoginForm :form="form"></LoginForm>
        </el-row>
      </el-row>
    </el-col>

  </div>
</template>

<script>
import LoginForm from "@/components/LoginForm";
import {mapState} from "vuex";

export default {
  name: "LoginPage",
  components: {
    LoginForm
  },
  data() {
    return {}
  },
  methods: {},
  computed: {
    ...mapState("purchase", {
      form: state => state.form
    })
  }
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
  height: calc(29%);
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
}

#pad_row{
  width: 100%;
  height: calc(80% - 10px);
  overflow: hidden;
  margin-top: 20px
}

#login_text{
  font-size: 30px;
  color: white;
  text-shadow: 1px 1px 10px #999
}

#loginForm{
  width: 90%;
  height: 90%;
  padding-left: 10%;
  padding-bottom: 10%;
  background-color: #fff0;
}

</style>