<template>
  <div id="header" class="fixed-top d-flex align-items-center header-transparent" :class="isShowTopTip ? '' : 'topFixedBar'">
      <div class="container-fluid container-xl d-flex align-items-center justify-content-between">
        <div class="logo me-auto">
          <!-- 修改 -->
          <h1><router-link to="/"
              style="color: orange; font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">Delicious</router-link>
          </h1>
          <!-- <h1><a href="index.html"
              style="color: orange; font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">Delicious</a>
          </h1> -->
          <!-- Uncomment below if you prefer to use an image logo -->
          <!-- <a href="index.html"><img src="assets/img/logo.png" alt="" class="img-fluid"></a>-->
        </div>

        <nav id="navbar" class="navbar order-last order-lg-0">
          <ul>
            <li><a class="nav-link scrollto active" href="#hero" style="color: white;">Home</a></li>
            <li><a class="nav-link scrollto" href="#why-us">Why Us</a></li>
            <li><a class="nav-link scrollto" href="#menu">Menu</a></li>
            <li><a class="nav-link scrollto" href="#specials">Specials</a></li>
            <li><a class="nav-link scrollto" href="#events">Events</a></li>
            <li><a class="nav-link scrollto" href="#gallery">Gallery</a></li>
          </ul>
          <i class="bi bi-list mobile-nav-toggle"></i>
        </nav><!-- .navbar -->
      </div>
    </div>
</template>

<script>
export default {
  props: {
    isShowTopTip: {
      type: Boolean,
      default: true,
    }
  },
}
</script>

<style scoped>
#navbar {
  /* float: left; */
  /* text-align: center; */
  /* margin-left: 100px; */
  width: 900px;
  /* background-color: black; */
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

#navbar a {
  float: left;
  margin-left: 50px;
  color: orange;
}

#navbar a:hover {
  color: white;
}

.topFixedBar {
  top : 0 !important;
  background-color: #212529E0 !important;
}
</style>
