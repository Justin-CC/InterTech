<template>
    <div class="register-container">
        <!-- register -->
        <div class="register">
            <h3>Register as a new user
                
                <span class="go">I have an account, to&nbsp;<router-link class="login" to="/login">Log in</router-link>
                </span>
            </h3>
            <div class="content">
                <label>Username:</label>
                <input type="text" placeholder="Please input your Username" v-model="username" />
                <span class="error-msg">Please enter the correct information</span>
            </div>
            <div class="content">
                <label>Phone:</label>
                <input type="text" placeholder="Please input your Phone Number" v-model="phone" />
                <span class="error-msg">Please enter the correct information</span>
            </div>
            <div class="content">
                <label>E-mail:</label>
                <input type="text" placeholder="Please input your E-mail" v-model="email" />
                <span class="error-msg">Please enter the correct information</span>
            </div>
            <!-- <div class="content">
        <label>验证码:</label>
        <input type="text" placeholder="请输入验证码">
        <img ref="code" src="http://182.92.128.115/api/user/passport/code" alt="code">
        <span class="error-msg">Please enter the correct information</span>
      </div> -->
            <div class="content">
                <label>Password:</label>
                <input type="password" placeholder="Please input your password" v-model="password" />
                <span class="error-msg">Please enter the correct information</span>
            </div>
            <div class="content">
                <label>Confirm password:</label>
                <input type="password" placeholder="Please confirm your password" v-model="password1" />
                <span class="error-msg">Please enter the correct information</span>
            </div>
            <div class="controls">
                <input name="m1" type="checkbox" :checked="agree" />
                <span>&nbsp;&nbsp;Agree to the agreement and register our《User Agreement》</span>
                <span class="error-msg">Please enter the correct information</span>
            </div>
            <div class="btn">
                <button @click="userRegister">Complete Registration</button>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Register',
    //   components:{
    //   Register,
    // },
    data() {
        return {
            // Username
            username:"",
            // Phone Number
            phone:"",
            // E-mail
            email: "",
            // Password
            password: '',
            // Confirm password
            password1: '',
            // Agree
            agree: true
        };
    },
    methods: {
        async userRegister() {
            try {
                const { username, phone, email, password, password1 } = this;
                (username && phone && email && password == password1) && (await this.$store.dispatch('userRegister', { email, password }));
                this.$router.push('/login');
            } catch (error) {
                alert(error.message);
            }
        }
    }
}
</script>

<style scoped lang="less">
.register-container {
    margin-top: 150px;

    .register {
        width: 1200px;
        height: 545px;
        border: 1px solid rgb(223, 223, 223);
        margin: 0 auto;


        h3 {
            background: orange;
            margin: 0;
            padding: 6px 15px;
            color: white;
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            border-bottom: 1px solid #dfdfdf;
            font-size: 20.04px;
            line-height: 30.06px;
            text-align: left;

            span {
                font-size: 14px;
                float: right;

                a {
                    color: black;
                }
            }
        }

        div:nth-of-type(1) {
            margin-top: 80px;
        }

        .content {
            // padding-left: 390px;
            margin-bottom: 18px;
            position: relative;
            margin: 20px 0 10px -70px;

            label {
                font-size: 14px;
                width: 120px;
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                // text-align: right;
                display: inline-block;
                text-align: justify;
                // margin: 0 0 0 -30px;
            }

            input {
                width: 270px;
                height: 38px;
                // padding-left: 8px;
                box-sizing: border-box;
                outline: none;
                border: 1px solid #999;
                text-align: left;
                left: 495px;
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            }

            // img {
            //     vertical-align: sub;
            // }

            .error-msg {
                position: absolute;
                top: 100%;
                left: 560px;
                font-size: 10px;
                color: red;
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            }
        }

        .controls {
            text-align: center;
            position: relative;
            // margin: 0 0 0 115px;
            margin: 15px 0 0 125px;

            input {
                vertical-align: middle;
                // margin: 20px 0 0 130px;
            }

            span {
                font-size: 10px;
            }

            .error-msg {
                position: absolute;
                top: 100%;
                left: 495px;
                color: red;
                font-size: 10px;
                // margin: 0 0 0 15px;
                margin-left: -130px;
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;

            }
        }

        .btn {
            text-align: center;
            line-height: 36px;
            margin: 17px 0 0 55px;

            button {
                outline: none;
                width: 270px;
                // height: 36px;
                line-height: 36px;
                background: orange;
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                color: #fff !important;
                display: inline-block;
                // display: inline-flex;
                font-size: 16px;
                border: 1px solid darkgray;

            }
        }
    }
}
</style>
