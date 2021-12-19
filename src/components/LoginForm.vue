<template>
  <el-form ref="form" :model="form" label-width="80px">
    <el-form-item label="Name">
      <el-input v-model="form.username" @change="onchange"></el-input>
      <p class="login" v-if="isLoginClick && this.isUsernameEmpty">Empty Username!</p>
    </el-form-item>
    <el-form-item label="email">
      <el-input v-model="form.emailAddress" @change="onchange"></el-input>
      <p class="login" v-if="isLoginClick && this.isIDEmpty">Empty emailAddress!</p>
    </el-form-item>
    <el-form-item label="Password">
      <el-input v-model="form.password" @change="onchange2"></el-input>
      <p class="login" v-if="isLoginClick && isWrongPassword">Wrong Password or Valid Username</p>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="loginClick">Login</el-button>
      <el-button @click="registerClick">Register</el-button>
    </el-form-item>
  </el-form>
</template>

<script>

import {mapMutations, mapState} from "vuex";
export default {
  name: "LoginForm",
  data() {
    return {
      isLoginClick: false,
      name:false,
      hasPassword:false,
      form:{
        username: '',
        password: '',
        emailAddress: ''
      },
    }
  },
  methods: {
    ...mapMutations(['changeLogin']),
    onchange(){
      this.name=true
      },
    onchange2(){
       this.hasPassword=true
     },
    loginClick() {
      // this.$store.dispatch("purchase/loginCheck")
      this.isLoginClick = true
      this.login(this)
    },
    registerClick() {
      this.$router.push('/register')
    },
    login(obj){
      let _this = this
      obj.axios.post('/login',{
          username:obj.form.username,
          emailAddress:obj.form.emailAddress,
          password:obj.form.password,
      })
      .then(function(response){
          if(response.data['code'] === 200){
            _this.$store.commit('purchase/changeLogin',{Authorization: response.data['token']})
            obj.$router.push('/main')
          }else{
              return false
          }
      })
      .catch(function(error){
          console.log(error)
      })
    }
  },
  computed: {
    ...mapState("purchase", {
      isWrongPassword: state => !state.accountValid
    }),
    isUsernameEmpty() {
      return this.form.username === null
    },
    isIDEmpty() {
      return this.form.emailAddress === null
    }
  },
  watch: {
    isWrongPassword() {
      if (!this.isWrongPassword) {
        this.$router.push('/main')
      }
    }
  }

}
</script>

<style scoped>
.login {
  margin-top: 20px;
  font-size: 14px;
  line-height: 22px;
  color: #dc3005;
  cursor: pointer;
  text-align: left;
  text-indent: 8px;
  width: 100%;
}
</style>