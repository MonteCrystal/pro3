import VueRouter from 'vue-router'
import Login from "@/views/Login";
import Register from "@/views/Register";
import Display from "../views/Display";
import DataList from "../views/DataList";
import ReportList from "@/views/ReportList";
import History from "@/views/History";
import Personal from "@/views/Personal";
import Algorithm from "@/views/Algorithm";

const routes = [
    {path: '/login', component: Login},
    {path: '/register', component: Register},
    {path: '/', redirect: '/login'},
    {path: '/main/report',component:Display},
    {path: '/main/datalist',component:DataList},
    {path: '/main',component: ReportList},
    {path:'/main/history',component: History},
    {path:'/main/personal',component: Personal},
    {path:'/main/algo',component:Algorithm}

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
