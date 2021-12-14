
export function register(obj) {
        obj.axios({method:'post', url:'/register',data: {//用post方法传 输入框输入的用户名和密码
          username: obj.form.username,
          password: obj.form.password,
          emailAddress:obj.form.emailAddress

        }})
          .then(
              res=>{
                  console.log('res=>',res);
          obj.$router.push('/main')
          });
}

export function login(obj){
          obj.axios({method:'post', url:'/login',data: {//用post方法传 输入框输入的用户名和密码
          username: obj.form.username,
          emailAddress: obj.form.emailAddress,
          password: obj.form.password,
        }}).then(res=>{console.log('res=>',res);
        if(res.data['code'] === 200){
          obj.$router.push('/main')}
        }
        )
      .catch((err) =>
      {console.log(err);});
}

export function verify_code(obj){
          obj.axios({method:'post', url:'/email_captcha',data: {//用post方法传 输入框输入的用户名和密码
          emailAddress: obj.form.emailAddress
        }}).then(res=>{console.log('res=>',res);
        if(res.data['code'] === 200){
          // obj.isDisable = true

            obj.verifycode = res.data['data']
        }}
        )
      .catch((err) =>
      {console.log(err);});
}
