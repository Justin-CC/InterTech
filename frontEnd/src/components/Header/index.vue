<template>
  <section v-if="isShowTopTip" id="topbar" class="d-flex align-items-center fixed-top topbar-transparent">
      <div class="container-fluid container-xl d-flex align-items-center justify-content-center justify-content-lg-start">
        <!-- <i class="bi bi-phone d-flex align-items-center"><span style="color: orange;">+1 5589 55488 55</span></i> -->
        <!-- <i class="bi bi-clock ms-4 d-none d-lg-flex align-items-center"><span style="color: orange;">Mon-Sat: 11:00 AM - 23:00 PM</span></i> -->
        <!-- <i><span>test</span></i> -->


        
        <!-- 未登录 -->
        <!-- 需要获取用户信息 API -->
        <!-- <p v-if="!userName"> -->
        <p>
            <!-- <span></span> -->
            <router-link to="/login">Sign In</router-link>
            <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <router-link to="/register" class="register">Sign Up</router-link>
        </p>
        <!-- 登录 -->
        <!-- <p v-else>
            <a >{{ userName }}</a>
            <a class="register" @click="logout">Sign Out</a>
        </p> -->
        
        <!-- <button class="sign-in-btn scrollto" onclick="">Sign In</button>
        <button class="sign-in-btn scrollto" onclick="">Sign Up</button> -->
        <!-- <a href="#sign-up" class="sign-up-btn scrollto">Sign Up</a> -->
        <form action="###" class="searchForm"><span>
            <input type="text" id="autocomplete" class="input-error input-xxlarge" v-model="keyword" />
            <button class="sui-btn btn-xlarge btn-danger" type="button" @click="goSearch">Search</button>
          </span>
        </form>
      </div>
    </section>
</template>
  
<script>
export default {
  name: "",
  props: {
    isShowTopTip: {
      type: Boolean,
      default: true,
    }
  },
  data() {
    return {
      keyword: ''
    }
  },
  methods: {
    goSearch() {
      // this.$router.push('/search/'+this.keyword)
      // this.$router.push("/search/" + this.keyword +"?k=" +this.keyword.toUpperCase());
      this.$router.push({name:"search",params:{keyword:this.keyword||undefined},query:{k:this.keyword.toUpperCase()}});
      // console.log(result)
      // if(this.$route.query){
      //   let location={name:"search",paramms:{keyword:this.keyword||undefined}};
      //   location.query=this.$route.query;
      //   this.$router.push(location)
      // }
    },
    async logout(){
      try {
        // log out successfully, back to home page
        await this.$store.dispatch('userLogout');
        this.$router.push('/');
      } catch (error) {
        
      }
    }
  },
};
</script>
  
<style scoped>
.searchForm {
  margin-left: 600px;
  /* padding-right: 10px; */
}

.searchForm button {
  /* float: right; */
  height: 30px;
  width: 70px;
  background-color: orange;
  border: none;
  /* border-color: orange; */
  /* border: 1px solid orange; */
  text-align: center;
  color: white;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

p {
  height: 32px;
  width: 200px;
  /* background-color: orange; */
  /* border-radius: 20px; */
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  border: none;
  color: #fff;
  /* font-size: 20px; */
  text-align: center;
  margin-top: 25px;
  margin-right: 10px;
  /* float: right; */
  /* float: left; */
  cursor: pointer;
}

a.router-link-active{
  color: black;
}

</style>
  