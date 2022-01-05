<template>
  <el-descriptions :column="1"  :colon="false" id="el-des" >
    <el-descriptions-item>
      <el-input class="login_input" v-model="form.emailAddress" @change="onchange" placeholder="邮箱"></el-input>
      <p class="warn" v-if="isLoginClick && !(hasemail)">邮箱地址为空</p>
      <p v-else class="elseword"></p>
    </el-descriptions-item>
    <el-descriptions-item>
      <el-input class="login_input" v-model="form.password" @change="onchangepw" show-password placeholder="密码"></el-input>
      <p class="warn" v-if="isLoginClick && isWrongPassword">用户名或密码错误</p>
      <p v-else class="elseword"></p>
    </el-descriptions-item>
    <el-descriptions-item :span="2">
      <el-button type="primary" @click="loginClick" id="login_button">登录</el-button>
      <el-button @click="registerClick" id="register_button">注册</el-button>
    </el-descriptions-item>
  </el-descriptions>
</template>

<script>

import {mapMutations} from "vuex";
export default {
  name: "LoginForm",
  data() {
    return {
      isLoginClick: false,
      hasemail: false,
      hasPassword: false,
      isWrongPassword: false,
      form:{
        password: '',
        emailAddress: ''
      },
    }
  },
  methods: {
    ...mapMutations(['changeLogin']),
    onchange(){
      this.hasemail = !(this.form.emailAddress === '')
    },
    onchangepw(){
       this.hasPassword = !(this.form.password === '')
    },
    loginClick() {
      this.isLoginClick = true
      this.login()
    },
    registerClick() {
      this.$router.push('/register')
    },
    login(){
      console.log(this.isLoginClick)
      console.log(this.hasemail)
      console.log(this.isWrongPassword)
      let that = this
      this.axios({
        method:'post',
        url:'/login',
        data:{
          emailAddress:that.form.emailAddress,
          password:that.form.password,
      }}).then(function(response){
          if(response.data['code'] === 200){
            that.$store.commit('purchase/changeLogin',{Authorization: response.data['token']})
            that.$router.push('/main')
          }else{
            that.isWrongPassword = true
          }
      })
      .catch(function(error){
          console.log(error)
      })
    }
  // },
  // computed: {
  //   ...mapState("purchase", {
  //     isWrongPassword: state => !state.accountValid
  //   })
  // },
  // watch: {
  //   isWrongPassword() {
  //     if (!this.isWrongPassword) {
  //       this.$router.push('/main')
  //     }
  //   }
  }

}
</script>

<style>

.el-descriptions-item__container {
    display: flex;
    align-items: center;
    justify-content: center;
}

.elseword{
  color: #fff0;
  padding: 0;
}

.el-descriptions__body {
    background-color: #fff0;
}

.warn{
  color: red;
}

#login_button{
  border-radius: 100px;
  background-color: #CAD5FD;
  border: 0px;
  color: white;
}

#register_button{
  border-radius: 100px;
  background-color: #ffffff;
  border: 0px #ffffff;
  color: black;
}

.login_input{
  width: 200px;
}

</style>