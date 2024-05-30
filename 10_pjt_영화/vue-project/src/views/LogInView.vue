<template>
  <div style="margin-top:100px; display: flex; justify-content: center;">
    <div style="display: flex;flex-wrap: wrap;justify-content: center;
    flex-direction: column; padding: 40px; border: solid gray ; width: 40%; background-color: rgb(250, 247, 243);">
      <h1 style="text-align: center;"><pre style="font-weight: bolder;">로그인</pre></h1>
      <form @submit.prevent="logIn" style="text-align: center;">
        <div style="margin: 20px;flex-direction: column;">
          <pre>User name</pre>
          <input type="text" v-model.trim="username" id="username" >
        </div>
        <div style="margin: 20px;">
          <pre>Password</pre>
          <input type="password" v-model.trim="password" id="password" >
        </div>
        <button type="submit" class="btn btn-outline-dark" ><pre style="font-size: larger; margin-bottom: 0px;">LOGIN</pre></button>
      </form>
    </div>
  </div>
</template>


<script setup>

  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'

  const username = ref(null)
  const password = ref(null)
  const store = useCounterStore()

  const logIn = function () {
    const payload = {
      username : username.value,
      password : password.value
    }
    
    store.logIn(payload)

  }

</script>

<style>

</style>
