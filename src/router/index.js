import VueRouter from 'vue-router'
import LoginPage from "@/views/LoginPage";
import RegisterPage from "@/views/RegisterPage";
import RecordPage from "../views/RecordPage";
import DataListPage from "../views/DataListPage";
import MainPage from "@/views/MainPage";
import HistoryPage from "@/views/HistoryPage";
import PersonalPage from "@/views/PersonalPage";
import AlgorithmPage from "@/views/AlgorithmPage";

const routes = [
    {path: '/login', component: LoginPage},
    {path: '/register', component: RegisterPage},
    {path: '/', redirect: '/login'},
    {path: '/main/record',component:RecordPage},
    {path: '/main/datalist',component:DataListPage},
    {path: '/main',component: MainPage},
    {path:'/main/history',component: HistoryPage},
    {path:'/main/personal',component: PersonalPage},
    {path:'/main/algo',component:AlgorithmPage}
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
