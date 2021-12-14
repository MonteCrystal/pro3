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

export default new VueRouter({
    mode: 'history',
    routes: routes
})
