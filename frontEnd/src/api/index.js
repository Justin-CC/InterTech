// API interface unified management
import requests from "./request";

// menu
// export const reqMenuList=()=>requests({url:'',method:'get'});

// register
export const reqUserRegister=(data)=>requests({url:'',data,method:'post'});
// login
export const reqUserLogin=(data)=>requests({url:'',data,method:'post'});
// get user's information -- with token
export const reqUserInfo=()=>requests({url:'',method:'get'});
// logout
export const reqLogout=()=>requests({url:'',method:'get'});

// get dishes detail
export const reqGoodsInfo=(mealId)=>requests({url:'',method:'get'});

// commit
export const reqCommentSubmit=(data)=>requests({url:'',data,method:'post'})