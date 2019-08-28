<template>
  <div id="app" class="container-fluid">
    <top></top>
    <router-view></router-view>
    <button type="button" @click="test">test</button>
  </div>
</template>
<script>
  export default {
    name: 'App',
    methods: {
      test:function () {
        $.ajax(
            "http://127.0.0.1:5000"+'/test',
            {
              type:"POST",
              changeOrigin:true,
              success:function (data) {
                alert(data.sccess)
              }
            }
          )
      }
    },
    components: {},
    created() {},
  }
</script>

<style>
  App {

  }

</style>
