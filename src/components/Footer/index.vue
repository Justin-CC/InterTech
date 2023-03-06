<template>
  <div class="footer">
    <div class="footer-container">
      <div class="copyright">
        <ul class="helpLink">
          <li><a href="#aboutus" class="footer-link scrollto">About us</a><span class="space"></span></li>
          <li><a href="#contactus" class="footer-link scrollto">Contact us</a><span class="space"></span></li>
          <li><a href="#faqs" class="footer-link scrollto">FAQs</a><span class="space"></span></li>
          <li><a href="#helpcenter" class="footer-link scrollto">Help Center</a><span class="space"></span></li>
        </ul>
        <!-- <p>Openning Hour: 11:00am —— 23:00pm</p> -->
        <!-- <p>Et aut eum quis fuga eos sunt ipsa nihil. Labore corporis magni eligendi fuga maxime saepe commodi placeat.</p> -->
        <p>© Copyright Delicious. All Rights Reserved</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: '',
}
</script>

<style scoped lang="less">
.footer {
  background-color: #eaeaea;

  .footer-container {
    width: 1200px;
    margin: 0 auto;
    padding: 0 15px;

    .copyright {
      padding: 20px;

      .helpLink {
        text-align: center;
        // width: 100px;
        ;

        li {
          display: inline;
          // color: white;
          // width: 100px;

          .space {
            border-left: 1px solid #666;
            width: 1px;
            height: 13px;
            background: #666;
            margin: 8px 10px;
          }
        }
      }

      p {
        margin: 40px 0;
        // height: 40px;
        text-align: center;
        color: #666;
      }
    }
  }
}

a{
  color: #666;
}
</style>

