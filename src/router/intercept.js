import axios from 'axios'


axios.defaults.baseURL = 'http://127.0.0.1:5000';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';


axios.interceptors.request.use(
	config => {
		let token = localStorage.getItem('Authorization');
		if(token){
			config.headers.common['token'] = token
		}
		return config
	},
	err => {
		console.log(err)
		return Promise.reject(err);
	}
)


// //异步请求后，判断token是否过期
// axios.interceptors.response.use(
//   response => {
//     return response;
//   },
//   error => {
//     if (error.response) {
//       switch (error.response.status) {
//         case 401:
//           localStorage.removeItem('token');
//           this.$router.push('/');
//       }
//     }
//   }
// )

export default axios