import axios from "axios"
import store from "@/store";

let requests=axios.create({
    baseURL:"/api",
    // request time 5s
    timeout:5000,
});

requests.interceptors.request.use((config)=>{
    
    let token=store.state.user.token;
    if(token){
        config.headers.token=token;
    }
    return config;
})

requests.interceptors.response.use((res)=>{
    return res.data;
}, (error)=>{
    return Promise.reject(new Error('fail'));
});

export default requests;