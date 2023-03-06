<template>
  <div class="login-container">
    <!-- log in -->
    <div class="login-wrap">
      <div class="login">
        <div class="loginform">
          <ul class="tab clearFix">
            <li><a href="##" class="current">Account Sign In</a></li>
          </ul>
          <div class="content">
            <form>
              <div class="input-text clearFix">
                <span>Username</span>
                <input type="text" placeholder="E-mail" v-model="email">
              </div>
              <div class="input-text clearFix">
                <span class="pwd">Password</span>
                <input type="password" placeholder="Please input your password" v-model="password">
              </div>
              <div class="setting clearFix">
                <label class="checkbox inline">
                  <input name="m1" type="checkbox" value="2" checked="">
                  Automatic Logon
                </label>
                <span class="forget">Forget your password?</span>
              </div>
              <button class="btn" @click.prevent="userLogin">Log&nbsp;&nbsp;In</button>
            </form>
            <div class="call clearFix">
              <router-link class="register" to="/register">Sign Up Now!</router-link>
              <!-- <router-link class="register" :to={path:'./register', query:$route.query}>Sign Up</router-link> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Login',
  data(){
    return{
      email:'',
      password:'',
    }
  },
  methods:{
    async userLogin() {
      try {
        const { email, password } = this;
        (email && password) && (await this.$store.dispatch('userLogin', { email, password }));
        this.$router.push("/");
      } catch (error) {
        alert(error.message);
      }
    },
  },
};
</script>

<style scoped lang="less">
.login-container {
  .login-wrap {
    height: 687px;
    background-color: orange;

    .login {
      width: 1200px;
      height: 687px;
      margin: 0 auto;
      background: wheat;
    }

    .loginform {
      width: 420px;
      height: 406px;
      box-sizing: border-box;
      background: #fff;
      float: right;
      top: 140px;
      right: 50px;
      position: relative;
      padding: 20px;

      .tab {
        li {
          width: 50%;
          float: left;
          text-align: center;
          top: 55px;

          a {
            width: 100%;
            display: block;
            height: 50px;
            line-height: 50px;
            font-size: 20px;
            font-weight: 700;
            color: #333;
            //   border: 1px solid #ddd;
            box-sizing: border-box;
            text-decoration: none;
          }

          .current {
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            color: orange;
            text-align: center;
            margin-top: 5px;
            margin-left: 60px;
          }
        }
      }

      .content {
        width: 380px;
        height: 336px;
        box-sizing: border-box;
        top: 600px;
        border: 1px solid orange;
        border-top-color: orange;
        padding: 18px;

        form {
          margin: 15px 0 18px 0;
          font-size: 12px;
          line-height: 18px;
          top: 150px;

          .input-text {
            margin-bottom: 30px;

            span {
              float: left;
              width: 70px;
              height: 32px;
              // line-height: 32;
              border: 1px solid #ccc;
              background: orange;
              box-sizing: border-box;
              border-radius: 2px 0 0 2px;
              margin-top: 30px;
              text-align: center;
              padding-top: 6px;
              font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            }

            .pwd {
              background-position: -72px -201px;
            }

            input {
              width: 270px;
              height: 32px;
              box-sizing: border-box;
              border: 1px solid #ccc;
              border-left: none;
              float: left;
              padding-top: 6px;
              padding-bottom: 6px;
              font-size: 14px;
              line-height: 22px;
              padding-right: 8px;
              padding-left: 8px;
              border-radius: 0 2px 2px 0;
              outline: none;
              margin-top: 30px;
              font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            }
          }

          .setting {
            label {
              float: left;
              margin-top: 15px;
              font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            }

            .forget {
              float: right;
              margin-top: 15px;
              font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            }
          }

          .btn {
            background-color: orange;
            padding: 6px;
            border-radius: 0;
            font-size: 16px;
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            word-spacing: 4px;
            border: 1px solid orange;
            color: #fff;
            width: 100%;
            height: 36px;
            margin-top: 45px;
            outline: none;
          }
        }

        .call {
          margin-top: -10px;

          ul {
            float: left;

            li {
              float: left;
              margin-right: 5px;
            }
          }

          .register {
            float: right;
            font-size: 12px;
            line-height: 38px;
            color: black;
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
          }

          .register:hover {
            color: orange;
            text-decoration: underline;
          }
        }
      }
    }
  }
}</style>
    

    
