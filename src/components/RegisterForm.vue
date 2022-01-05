<template>
  <el-descriptions :column="2"  :colon="false" id="el-des">
    <el-descriptions-item :span="2">
      <el-input class="reg_input" v-model="form.username" placeholder="用户名"></el-input>
    </el-descriptions-item>
    <el-descriptions-item :span="2">
      <el-input class="reg_input" v-model="form.emailAddress" placeholder="邮箱"></el-input>
    </el-descriptions-item>
    <el-descriptions-item :span="1">
      <el-input class="verif_text" v-model="form.verifyCode" placeholder="验证码"></el-input>
    </el-descriptions-item>
    <el-descriptions-item>
      <el-button class="verif_but" type="primary" :disabled='isDisable' @click="sendVerifyCode">
        发送验证码
      </el-button>
    </el-descriptions-item>
    <el-descriptions-item :span="2">
      <el-input class="reg_input" v-model="form.password" placeholder="密码" show-password></el-input>
      <p class="warn" v-if="!validPW">密码应包括6-20位数字、字母或符号</p>
    </el-descriptions-item>
    <el-descriptions-item :span="2">
      <el-input class="reg_input" v-model="form.confirmPassword" placeholder="确认密码" show-password></el-input>
    </el-descriptions-item>
    <el-descriptions-item :span="2">
      <p class="warn" v-if="!isPWDSame">两次输入的密码应该相同</p>
      <p class="warn" v-if="isRegisterClick && errorMsg!== null">{{ errorMsg }}</p>
    </el-descriptions-item>
    <el-descriptions-item>
      <el-button id="reg_but" type="primary" @click="registerClick">注册</el-button>
      <p class="login" @click="gotoLogin">已经拥有账号？现在去登录</p>
    </el-descriptions-item>
  </el-descriptions>


</template>

<script>
import {mapState} from "vuex";
import {register} from '@/api/user'
import {verify_code} from '@/api/user'
export default {
  name: "RegisterForm",
  computed: {
    ...mapState("purchase", {
      form: state => state.form,
      accountValid: state => state.accountValid,
      errorMsg: state => state.errorMsg
    }),
    isPWDSame() {
      return this.form.password === this.form.confirmPassword
    },
    validPW(){
      var len = this.form.password.length
      if(len > 20){
        return false
      }else if(len < 6){
        return false
      }
      return true
    }
  },
  data() {
    return {
      isDisable: false,
      isRegisterClick: false,
      verifycode:0
    }
  },
  methods: {
    sendVerifyCode() {
      verify_code(this)
    },
    gotoLogin() {
      this.$router.push('/login')
    },
    registerClick() {
      console.log("notice: "+this.verifycode+" 000 "+this.form.verifyCode)

      if(this.verifycode === this.form.verifyCode){
        this.isDisable = true

        register(this)

      }
      this.isRegisterClick = true

    }
  },
  watch: {
    accountValid() {
      if (this.accountValid) {
        this.$router.push('/purchase')
      }
    },
  }
}
</script>

<style scoped>
.code >>> .el-form-item__content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.code button {
  margin-left: 20px;
  width: 140px;
  text-align: center;
}

.login {
  margin-top: 10px;
  font-size: 14px;
  line-height: 22px;
  color: #1ab2ff;
  cursor: pointer;
  text-align: left;
  text-indent: 8px;
  width: 100%;
}

.warn {
  margin-top: 10px;
  font-size: 14px;
  line-height: 22px;
  color: #dc3005;
  cursor: pointer;
  text-align: left;
  text-indent: 8px;
  width: 100%;
}

.reg_input{
  width: 250px;
}

.verif_text{
  width: 100px;
  padding: 0;
}

.verif_but{
  width: 110px;
  border-radius: 0px;
  justify-content: center;
  background-color: #CAD5FD;
  border: 0px #ffffff;
  color: #fff;
  text-shadow: 1px 1px 10px #999;
}

#reg_but{
  width: 100%;
  border-radius: 100px;
  background-color: #CAD5FD;
  border: 0px;
  color: #fff;
  text-shadow: 1px 1px 10px #999;
}

</style>