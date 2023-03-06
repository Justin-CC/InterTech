<template>
  <TopBar :isShowTopTip="isShowTopTip"/>
  <!-- <HeaderNav/> -->
  <Hero />
  <WhyUs />
  <Menu />
  <Specials />
  <Events />
  <Gallery />
</template>
<script>
import TopBar from './components/TopBar'
// import HeaderNav from './components/HeaderNav'
import Hero from './components/Hero'
import WhyUs from './components/WhyUs'
import Menu from './components/Menu'
import Specials from './components/Specials'
import Events from './components/Events'
import Gallery from './components/Gallery'

export default {
  components: {
    TopBar,
    // HeaderNav,
    Hero,
    WhyUs,
    Menu,
    Specials,
    Events,
    Gallery,
  },
  // mounted(){
  //   this.$store.dispatch('getUserInfo');
  // }
  props: {
    isShowTopTip: {
      type: Boolean,
      default: true,
    }
  },
}
</script>

<style scoped></style>
