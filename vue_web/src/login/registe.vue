<template>
  <div class="col-xs-6 col-sm-4 tab">
    <div><span><h1 class="size">用户注册页面</h1></span>
      <div class="input-group input-div">
        <span class="input-group-addon" id="basic-addon1">帐号</span>
        <input v-on:blur="this.username" v-model="authlist.username" id="username" title="输入字母数字下划线，最少输入6位"
               type="text"
               class="form-control"
               placeholder="Username"
               aria-describedby="basic-addon1">
      </div>
      <span v-if="isauthlist.isusername" class="tishi">*用户名输入错误</span>
      <span v-else class="istishi">*用户名输入错误</span>
      <div class="input-group input-div">
        <span class="input-group-addon" id="basic-addon2">密码</span>
        <input @blur="this.password" v-model="authlist.password" id="password" title="请输入字母数字下划线，最少输入六位且不可与用户名相同"
               type="password"
               class="form-control"
               placeholder="password" aria-describedby="basic-addon1">
      </div>
      <span v-if="isauthlist.ispassword" class="tishi">*密码输入错误</span>
      <span v-else class="istishi">*密码输入错误</span>
      <div class="input-group input-div">
        <span class="input-group-addon" id="basic-addon3">电子邮箱</span>
        <input @blur="this.email" v-model="authlist.email" id="email" type="text" title="输入您的邮箱，目前仅支持163邮箱以及qq邮箱"
               class="form-control"
               placeholder="email"
               aria-describedby="basic-addon1">
        <span class="input-group-addon" id="basic-addon4 email">
          <div class="dropdown"><button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1"
                                        data-toggle="dropdown"
                                        aria-haspopup="true" aria-expanded="true">
                                      <span class="caret"></span>
                                    @163.com</button>
                                    <ul class="dropdown-menu login-reght" aria-labelledby="dropdownMenu1">
                                      <li><a href="#">@qq.com</a></li>
                                    </ul></div>
                                           </span>
      </div>
      <span v-if="isauthlist.isemail" class="tishi">*输入的邮箱不符合规则</span>
      <span v-else class="istishi">*输入的邮箱不符合规则</span>
      <div class="input-group input-div">
        <span class="input-group-addon" id="basic-addon5">手机号</span>
        <input @blur="this.phone" v-model="authlist.phone" id="phone" type="text" class="form-control"
               placeholder="phone"
               aria-describedby="basic-addon1">
      </div>

      <span v-if="isauthlist.isphone" class="tishi">*输入的手机号不符合规则</span>
      <span v-else class="istishi">*输入的手机号不符合规则</span>
      <div class="input-group input-div">
        <span class="input-group-addon" id="basic-addon6">用户名</span>
        <input @blur="this.name" v-model="authlist.name" id="name" title="请输入一个用户名，如不输入则默认为帐号" type="text"
               class="form-control"
               placeholder="name"
               aria-describedby="basic-addon1">

      </div>
      <span v-if="isauthlist.isname" class="tishi">*输入的用户名不符合规则</span>
      <span v-else class="istishi">*输入的用户名不符合规则</span>
    </div>
    <button @click="loginAuth" class="btn btn-default" type="submit">注册</button>
  </div>
</template>

<script>
  export default {
    name: "registe",
    data() {
      return {
        isauthlist: {
          "isusername": true,
          "ispassword": true,
          "isphone": true,
          "isemail": true,
          "isname": true
        },
        authlist: {
          "username": '',
          "password": "",
          "phone": '',
          "email": "",
          "name": "",
          "user": ""
        }
      }
    },
    methods: {
      username: function () {
        var username = this.authlist.username;
        var re_username = /^(\d|\s|_){6,}$/;
        if (!username.match(re_username) || username == null) {
          $(this.isauthlist.isusername = false);
          return 0;
        } else {
          $(this.isauthlist.isusername = true);
        }
      },
      password: function () {
        var username = this.authlist.username;
        var password = this.authlist.password;
        var re_password = /^\w+$/;
        if (!password.match(re_password)) {
          $(this.isauthlist.ispassword = false)
          alert(password)
          return 0;
        } else {
          $(this.isauthlist.ispassword = true)
        }

        if (password == username) {
          $(this.isauthlist.ispassword = false)
          alert("帐号密码不可以相同")
          return 0;
        }
      },
      phone: function () {
        var phone = this.authlist.phone;
        var re_phone = /^1[34578]\d{9}$/;
        // alert("是否有数据："+phone)
        if (!phone.match(re_phone) || phone == null) {
          $(this.isauthlist.isphone = false)
          return 0;
        } else {
          // alert()
          $(this.isauthlist.isphone = true)
        }
      },
      email: function () {
        var email = this.authlist.email + "@qq.com"
        // var email = this.authlist.email + $("#dropdownMenu1").text();
        //测试阶段使用qq邮箱，不同邮箱下拉列表暂时不用，等后面时间宽松在进行这个功能的添加
        var re_email = /^.{6,}@(163|qq)\.com$/;
        // alert(email)
        if (!email.match(re_email) || email == null) {
          $(this.isauthlist.isemail = false)
          alert(email)
          return 0;
        } else {
          $(this.isauthlist.isemail = true)
        }
      },
      name: function () {
        var name = this.authlist.name;
        var re_name = /^([\u4E00-\u9FA5]|\d|\s|_){3,20}$/;
        if (name.match(re_name) || name == null) {
          $(this.isauthlist.isname = false)
          return 0;
        }
      },
      loginAuth: function () {
        this.username();
        this.password();
        this.email();
        this.phone();
        this.name();
        this.$cookies.set("Access-Control-Allow-Origin", "*");
        this.$cookies.set("Access-Control-Allow-Methods", "POST");
        if (this.isauthlist.isusername == true ||
          this.isauthlist.ispassword == true ||
          this.isauthlist.isemail == true ||
          this.isauthlist.isphone == true ||
          this.isauthlist.isname == true) {
          var date = {
            "username": this.authlist.username,
            "userpwd": this.authlist.password,
            "eamil": this.authlist.email + '@qq.com',
            "phone": this.authlist.phone,
            "name": this.authlist.name,
          }
          var header = {"Access-Control-Allow-Origin": "*"}
          this.$axios({
            method: "post",
            url: "http://127.0.0.1:5000" + '/registe',
            // url:'/api/registe',
            dataType: 'jsonp',
            data: this.qs.stringify(date)
          }).then((data) => {

            alert(data)
          }).catch((error) => {
            alert(error)
          });
          $.ajax(
            "http://127.0.0.1:5000" + '/registe',
            {
              type: "post",
              changeOrigin: true,
              data: date,
              headers: header,
              success: function (data) {
                alert(data)
              }
            }
          )
        }
      }
    },
  }
</script>

<style scoped>
  .size {
    text-align: center
  }

  .login-reght {
    float: right;
  }

  .tab {
    border: 1px dashed darkgreen;
  }

  .tishi {
    display: block;
    visibility: hidden;
  }

  .istishi {
    visibility: visible;
  }

</style>
