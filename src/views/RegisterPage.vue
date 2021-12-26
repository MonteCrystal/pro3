<template>
  <div id="main-pane">
    <el-row class="boundary" style="width: 100%; height: calc(30% - 4px); overflow: hidden">
      <div class="titletext">
        <p>Register</p>
      </div>
    </el-row>

    <el-col :span="12" :offset="6">
      <el-row class="boundary" style="width: 100%; height: calc(80% - 10px); overflow: hidden; margin-top: 20px">
        <el-row>
          <p style="font-size: 30px;">Register</p>
        </el-row>
        <div id="loginForm">
          <el-col :span="18" :offset="2">
            <RegisterForm></RegisterForm>
          </el-col>
        </div>
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

<style>

.container {
  width: 100%;
  height: 100%;
}

.titletext {
  font-size: 20px;

  border-bottom-right-radius: 4px;
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
  border-top-right-radius: 4px;
  list-style-type: none;

  background: #dddede;
  height: 50px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  color: #444444;
  text-align: center;
}

#RegisterForm {
  text-align: center;
  font-size: 20px;
  margin-top: 0px;
}

#main-pane {
  /*margin: 6px;*/
  /*width: calc(100% - 12px);*/
  /*height: calc(100% - 12px - 42px);*/
  margin: 6px;
  width: calc(100% - 12px);
  height: calc(100% - 12px);
  /* use grid layout rather than el-row */
  /* because el-row and el-scrollbar can't be used together */

}

</style>