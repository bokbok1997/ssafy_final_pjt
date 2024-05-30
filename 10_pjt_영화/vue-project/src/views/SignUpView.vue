<template>
  <div style="margin-top:100px; display: flex; justify-content: center;">
    <div style="display: flex;flex-wrap: wrap;justify-content: center;
    flex-direction: column; padding: 40px; border: solid gray ; width: 40%; background-color: rgb(250, 247, 243);">
      <h1 style="text-align: center;"><pre style="font-weight: bolder;">회원가입</pre></h1>
      <form @submit.prevent="signUp" style="text-align: center;">
        <div style="margin: 20px;flex-direction: column;">
          <label for="title"><pre style="margin-bottom: 0px;">User name</pre></label>
          <br>
          <input type="text" v-model.trim="username" id="username">
        </div>
        <div style="margin: 20px;">
          <label for="password1"><pre style="margin-bottom: 0px;">password</pre></label>
          <br>
          <input type="password" v-model.trim="password1" id="password1">
        </div>
        <div style="margin: 20px;">
          <label for="password2"><pre style="margin-bottom: 0px;">password confirmation</pre></label>
          <br>
          <input type="password" v-model.trim="password2" id="password2">
        </div>
        <button type="submit" class="btn btn-outline-dark" ><pre style="font-size: larger; margin-bottom: 0px;">Submit</pre></button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const store = useCounterStore()

const signUp = function () {
  const payload = {
    username : username.value,
    password1 : password1.value,
    password2 : password2.value
  }
  // console.log(username.value, password1.value, password2.value)
  store.signUp(payload)

}

</script>

<style>

</style>
