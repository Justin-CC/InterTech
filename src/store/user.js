import { reqUserRegister,reqUserLogin,reqUserInfo,reqLogout,reqCommentSubmit } from "@/api"
import { setToken, getToken, removeToken } from "@/utils/token";
const state={
    token:getToken(),
    userInfo:{}
};

const mutations={
    USERLOGIN(state,token){
        state.token=token;
    },
    GETUSERINFO(state,userInfo){
        state.userInfo=userInfo;
    },
    CLEAR(state){
        state.token='';
        state.userInfo='';
        removeToken();
    }
};
const actions={
    // register
    async userRegister({commit},user){
        let result=await reqUserRegister(user);
        if(result.code==200){
            // return 'ok';
        }
        // else{
        //     return Promise.reject(new Error('fail'));
        // }
    },
    // login
    async userLogin({commit},data){
        let result=await reqUserLogin(data);
        if(result.code==200){
            // 用户登陆成功，获取到token
            commit("USERLOGIN",result.data.token);
            // 持久化存储token
            // localStorage.setItem("TOKEN",result.data.token);
            setToken(result.data.token);
            return 'ok';
        }
        else{
            return Promise.reject(new Error('fail'));
        }
    },
    // get user's information -- with token
    async getUserInfo({commit}){
        let result=await reqUserInfo();
        if(result.code==200){
            // submit user's info
            commit("GETUSERINFO",result.data);
            return 'ok';
        }
        else{
            return Promise.reject(new Error('fail'));
        }
    },
    // log out
    async userLogout({commit}){
        let result=await reqLogout();
        if(result.code=200){
            commit("CLEAR");
            return 'ok';
        }
        else{
            return Promise.reject(new Error('fail'));
        }
    },
    // comment
    async commentSubmit({commit},usercom){
        let result=await reqCommentSubmit(usercom);
        if(result.code==200){
            commit('COMMENTSUBMIT');
            return 'ok';
        }
        else{
            return Promise.reject(new Error('fail'));
        }
    }
};

const getters={};

export default{
    state,
    mutations,
    actions,
    getters,
};