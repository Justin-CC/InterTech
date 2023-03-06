<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <div>
    <Header :isShowTopTip="isShowTopTip"></Header>
    <router-view :isShowTopTip="isShowTopTip"></router-view>
    <Footer></Footer>
    <b-button href="#hero" class="back-to-top-button"></b-button>
    <!-- test element -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Header from './components/Header'
import Footer from './components/Footer'
export default {
  name: '',
  components: {
    // HelloWorld
    Header,
    Footer
  },
  data() {
    return {
      isShowTopTip: true,
    }
  },
  mounted () {
    window.addEventListener('scroll', this.scrollToTop)
  },
  methods: {
    scrollToTop() { 
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
      this.isShowTopTip = scrollTop <= 80
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
.back-to-top-button {
  background: transparent;
  background: url('./assets/backToTop.png') no-repeat !important;
  background-size: cover !important;
  width: 50px;
  height: 50px;
  border: none !important;
  position: fixed !important;;
  z-index: 1000;
  bottom: 200px;
  right: 30px;
}
</style>
