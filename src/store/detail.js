import { reqGoodsInfo } from "@/api";
const state={
    // type is object
    goodInfo:{}
};
const mutations={
    GETGOODINFO(state,goodInfo){
        state.goodInfo=goodInfo;
    }
};
const actions={
    // get good's infomation's action
    async getGoodInfo({commit},mealId){
        let result=await reqGoodsInfo(mealId);
        if(result.code==200){
            commit('GETGOODINFO',result.data);
        }
    }
};
const getters={};

export default {
    state,
    mutations,
    actions,
    getters
}