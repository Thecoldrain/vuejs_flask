<template>
  <button v-bind:content="message" @click="ajaxs">{{ message }}</button>


</template>

<script>
  import Vue from "vue"
  import VueResource from "vue-resource"

  Vue.use(VueResource);
  Vue.http.options.emulateJSON = true;
  export default {
    name: "csrf_post",
    data() {
      return {
        message: "成功",
      }
    },
    methods: {
      ajaxs: function () {
        var xhrCors = 'withCredentials' in new XMLHttpRequest();

        var exp = new Date();
        var date = {
          "username": 123456,
          "userpwd": 12345678,
          "eamil": 12345678 + '@qq.com',
          "phone": 15637342593,
          "name": "name",
        };
        this.$http.post("http://127.0.0.1:5000" + '/registe', date, {
          "headers": {
            'Content-Type': 'application/x-www-form-urlencoded',
            "Access-Control-Allow-Origin": "*"
          }
        })
        // exp.setTime(exp.getTime()+8*3600*1000)
        //   $.cookie("Access-Control-Allow-Origin","*")
        //   this.$axios({
        //     method: "post",
        //     url:"http://127.0.0.1:5000"+'/registe',
        //     // url: '/api/registe',
        //     dataType: 'jsonp',
        //     data: this.qs.stringify(date)
        //   }).then((data) => {
        //     this.message = data
        //   }).catch((error) => {
        //     this.message = error
        //   })
        // }

      }
    }
  }
</script>

<style scoped>

</style>
