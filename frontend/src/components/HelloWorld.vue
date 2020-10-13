<template>
  <div class="hello">
    <input name="una" v-model="username">
    <input name="pwd" v-model="password">
    <!-- 只有这两个接口进行请求 -->
    <button type="button" @click="handleClick">登录</button>
    <!-- <button type="button" @click="handlezhuxiao">注销</button> -->
    <button type="button" @click="handleWacth">查看所有用户</button>
  </div>
</template>

<script>
// let instanceTmp = axios.create({
//   baseURL:'http://127.0.0.1:8000',
//   timeout:2000
// })
import Cookies from 'js-cookie'

export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  data(){
    return{
      username:'',
      password:'',
      loading: true,
      num: null,
      islogin: false,
    }
  },
  methods:{
     handleWacth(){
      this.$axios.get("http://127.0.0.1:8000/apis/users/get_all_user/"
      ,{
        withCredentials:true 
      }

      ).then(res=>{
        console.log('res',res);
      }).catch(err=>{
        console.log('err:',err);
      })
      
    },
    handleClick(){
    this.$axios.post("http://127.0.0.1:8000/apis/users/login/", {
      username: this.username,
      password: this.password,
    }
      ,{
        withCredentials:true 
      }
    ).then(res=>{
       console.log('res',res)
     }).catch(err=>{
       console.log('err',err)
     })
    },
    handlezhuxiao(){
      
      this.$axios.get("/apis/user/logout")
        .then(response => {
          // 重载界面
          this.$router.go(0)
        }).catch(err=>{
          console.log('err:',err);
    })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
