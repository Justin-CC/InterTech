<template>
   
</template>

<script>
export default {
    name: 'Login',
    data(){
        return{
            email:"1047556574@qq.com",
            password:"123456"
        }
    },
    methods:{
        async login(){
            const{email,password,callback}=this;
            const errorMsg=await this.$store.dispatch('login',{email,password})
            if(!errorMsg){
                const redirect=this.$route.query.redirect
                this.$route.replace(redirect||'/')
            }
            else{
                alert(errorMsg)
            }
        },
    }
}
</script>
<style scoped>

</style>
