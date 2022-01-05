<template>
  <el-descriptions title="病患信息" :column="2" id="personal_description">
    <template slot="extra">
      <el-button id="edit_but" type="primary" @click="enableEdit">{{edit_save}}</el-button>
    </template>
    <el-descriptions-item label="用户名">
      <span v-show="!edit">{{userInfo.name}}</span>
      <el-input v-show="edit" v-model="userInfo.name"></el-input>
    </el-descriptions-item>
    <el-descriptions-item label="邮箱">
      <span v-show="!edit">{{userInfo.email}}</span>
      <el-input v-show="edit" v-model="userInfo.email"></el-input>
    </el-descriptions-item>
    <el-descriptions-item label="年龄">
      <span v-show="!edit">{{userInfo.age}}</span>
      <el-input v-show="edit" v-model="userInfo.age"></el-input>
    </el-descriptions-item>
    <el-descriptions-item label="性别">
      <span v-show="!edit">{{userInfo.gender}}</span>
      <el-select v-show="edit" v-model="userInfo.gender" :placeholder="userInfo.gender">
        <el-option
          v-for="item in gender_options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </el-descriptions-item>
    <el-descriptions-item label="手机号">
      <span v-show="!edit">{{userInfo.phone}}</span>
      <el-input v-show="edit" v-model="userInfo.phone"></el-input>
    </el-descriptions-item>
    <el-descriptions-item label="地址">
      <span v-show="!edit">{{userInfo.address}}</span>
      <el-input v-show="edit" v-model="userInfo.address"></el-input>
    </el-descriptions-item>
    <el-descriptions-item label="左裸眼视力">
      <el-tag class="eye_tag" v-show="!edit" size="small">{{userInfo.left_eyesight}}</el-tag>
      <el-select v-show="edit" v-model="userInfo.left_eyesight" :placeholder="userInfo.left_eyesight">
        <el-option
          v-for="item in eyesight_options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </el-descriptions-item>
    <el-descriptions-item label="右裸眼视力">
      <el-tag class="eye_tag" v-show="!edit" size="small">{{userInfo.right_eyesight}}</el-tag>
      <el-select v-show="edit" v-model="userInfo.right_eyesight" :placeholder="userInfo.right_eyesight">
        <el-option
          v-for="item in eyesight_options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </el-descriptions-item>
  </el-descriptions>
</template>

<script>
export default {
  name: "PersonalForm",
  data(){
    this.getUserInfo()
    return{
      userInfo: this.userInfo,
      edit: false,
      edit_save: '编辑',
      gender_options:[{
        value:'Female',
        label:'Female',
      },{
        value:'Male',
        label:'Male',
      },{
          value:'Transgender',
          label:'Transgender',
      },{
          value:'Non-binary/non-conforming',
          label:'Non-binary/non-conforming',
      },{
          value:'Prefer not to respond',
          label:'Prefer not to respond',
      }],
      eyesight_options:[{
        value:'0.0',label:'0.0',
      },{
        value:'0.1',label:'0.1',
      },{
        value:'0.12',label:'0.12',
      },{
        value:'0.15',label:'0.15',
      },{
        value:'0.2',label:'0.2',
      },{
        value:'0.25',label:'0.25',
      },{
        value:'0.4',label:'0.4',
      },{
        value:'0.5',label:'0.5',
      },{
        value:'0.6',label:'0.6',
      },{
        value:'0.7',label:'0.7',
      },{
        value:'0.8',label:'0.8',
      },{
        value:'0.9',label:'0.9',
      },{
        value:'1.0',label:'1.0',
      },{
        value:'1.2',label:'1.2',
      },{
        value:'1.5',label:'1.5',
      }]
    }
  },
  methods:{
    getUserInfo(){
      let that = this
      that.axios({
        method: 'get',
        url: '/main/getUserInfo'
      })
      .then(res=>{
        that.userInfo = res.data['user']
      }).catch(function(error){
        console.log(error)
      })
    },
    enableEdit(){
      this.edit = !this.edit
      if(this.edit){
        this.edit_save = '保存'
      }else{
        this.edit_save = '编辑'
        this.axios({
          method: 'post',
          url: '/main/setUserInfo',
          data:{
            userInfo: this.userInfo
        }}).then(res=>{
          console.log(res)
        }).catch(e=>{
          console.log(e)
        })
      }
    }
  }
}
</script>

<style scoped>

.el-descriptions-item__container{
  justify-content: left;
}

#edit_but{
  border-radius: 100px;
  background-color: #CAD5FD;
  border: 0px;
  color: white;
}

.eye_tag{
  background-color: white;
}

</style>