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

import {mapState} from "vuex";
import {login} from '@/api/user'
export default {
  name: "LoginForm",
  props: ['form'],
  data() {
    return {
      isLoginClick: false,
      name:false,
      password:false
    }
  },
  methods: {
    onchange(){
      this.name=true
      },
    onchange2(){
       this.password=true
     },
    loginClick() {
      // this.$store.dispatch("purchase/loginCheck")
      this.isLoginClick = true
      login(this)


      // this.axios({method:'post', url:'/login',data: {//用post方法传 输入框输入的用户名和密码
      //     username: this.form.username,
      //     password: this.form.password,
      //     id:this.form.id
      //   }}).then(res=>{console.log('res=>',res);
      //   if(res.data['code'] === 200){
      //     this.$router.push('/main')}
      //   }
      //   )
      // .catch((err) =>
      // {console.log(err);});
      // if (this.name && this.password){
      //   this.$router.push('/main')
      // }
    },
    registerClick() {
      this.$router.push('/register')
    }
  },
  computed: {
    ...mapState("purchase", {
      isWrongPassword: state => !state.accountValid
    }),
    isUsernameEmpty() {
      return this.form.username === null
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