import Vue from 'vue'
import {createRouter, createWebHashHistory} from 'vue-router'

import Home from '@/pages/Home'
import Search from '@/pages/Search'
import Login from '@/pages/Login'
import Register from '@/pages/Register'
import Aboutus from '@/pages/Aboutus'
import Contactus from '@/pages/Contactus'
import Faqs from '@/pages/Faqs'
import Helpcenter from '@/pages/Helpcenter'
import Booking from '@/pages/Booking'
import MenuDetail from '@/pages/MenuDetail'

// let originPush = createRouter.prototype.push;
// let originReplace = createRouter.prototype.replace;

// createRouter.prototype.push=function(location,resolve,reject){
//     if(resolve && reject){
//         originPush.call(this,location,resolve,reject);
//     }
//     else{
//         originPush.call(this,location,()=>{},()=>{});
//     }
// }

// createRouter.prototype.replace=function(location,resolve,reject){
//     if(resolve && reject){
//         originReplace.call(this,location,resolve,reject);
//     }
//     else{
//         originReplace.call(this,location,()=>{},()=>{});
//     }
// }

const router = createRouter({
    history: createWebHashHistory(),
    routes:[
        {
            path:"/",
            component:Home,
            props:true
        },

        {
            path:"/search/:keyword?",
            component:Search,
            name:"search",
            props:($route)=>{
                return {keyword:$route.params.keyword,k:$route.query.k};
            }
        },

        {
            path:"/login",
            component:Login
        },

        {
            path:"/register",
            component:Register
        },

        {
            path:"/aboutus",
            component:Aboutus
        },

        {
            path:"/contactus",
            component:Contactus
        },

        {
            path:"/faqs",
            component:Faqs
        },

        {
            path:"/helpcenter",
            component:Helpcenter
        },

        {
            path:"/booking",
            component:Booking
        },
         
        // redirect to home page
        {
            path:"/:pathMatch(.*)",
            redirect:"/"
        },

        {
            path:"/MenuDetail",
            component:MenuDetail,
            // props:($route)=>{
            //     return {mealId:$route.query.mealId};
            // }
        }

    ]
})

export default router