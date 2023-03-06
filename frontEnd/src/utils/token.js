// store token
export const setToken=(token)=>{
    localStorage.setItem('TOKEN',token);
};

// get token
export const getToken=()=>{
    return localStorage.getItem('TOKEN');
};

// clear token
export const removeToken=()=>{
    localStorage.removeItem("TOKEN");
}