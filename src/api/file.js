export function uploadFile(obj) {
    obj.axios({method:'post', url:'/upload', data: obj.uploadParams})
          .then(
              res=>{
                  if (res.data.code === 200) {
                      obj.$message('上传成功')
                  }else{
                      obj.$message('失败')
                  }

          });
}