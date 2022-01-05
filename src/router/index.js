import VueRouter from 'vue-router'
import LoginPage from "@/views/LoginPage";
import RegisterPage from "@/views/RegisterPage";
import RecordPage from "../views/RecordPage";
import MainPage from "@/views/MainPage";
import AlgorithmPage from "@/views/AlgorithmPage";
import UploadPage from "@/views/UploadPage";
import PersonalPage from "@/views/PersonalPage";
import DataPage from "@/views/DataPage";

const routes = [
    {path: '/login', component: LoginPage},
    {path: '/register', component: RegisterPage},
    {path: '/', redirect: '/login'},
    {path: '/main',component: MainPage},
    {path: '/main/record',component:RecordPage},
    {path: '/main/upload', component: UploadPage},
    {path:'/main/algo',component:AlgorithmPage},
    {path:'/main/personal', component: PersonalPage},
    {path: '/main/datalist', component: DataPage}
]

const router = new VueRouter({
    mode: 'history',
    routes: routes
})

router.beforeEach( (to, from, next) => {
    if (to.path === '/login' || to.path === '/register') {
        next();
    } else {
        let token = localStorage.getItem('Authorization');
        if (token === null || token === '') {
          next('/login');
        } else {
          next();
        }
    }
})

export default router;
