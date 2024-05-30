<template>
    <div class="mt-2">
      <div class="comment-box ps-3 pe-3" style="background-color: white; border: 1px solid rgb(255, 188, 96); border-radius: 10px;">
        <div>
          ⌊ {{ comment.content }} - {{ commentUser }} 💬
        </div>
        &nbsp; &nbsp;
        <button v-if="commentUser === store.nowUser" @click="deleteComment(comment.id)" type="button" class="btn btn-outline-dark" style=" --bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem; max-height: 30px;">
          DEL
        </button>
      </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const props = defineProps({
    comment : Object
})

const commentId = props.comment.id
const commentUser = ref('')

const findUser = function (commentPk) {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/comments/${commentPk}/find_user/`,
      headers : {
        Authorization : `Token ${store.token}`
      },
      
    })
      .then(response => {
        // console.log(response.data.username)
        commentUser.value = response.data.username
        // title.value.reset()
        // content.value.reset()
        // store.getReviews()
      })
      .catch(error => {
        console.log(error)
      })

  }

findUser(commentId)


const deleteComment = function (commentPk) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/api/v1/comments/${commentPk}/`,
      headers : {
        Authorization : `Token ${store.token}`
      },
      
    })
      .then(response => {
        // title.value.reset()
        // content.value.reset()
        console.log('삭제성공!')
        store.getComments()
      })
      .catch(error => {
        console.log(error)
      })

  }

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Gugi&family=Stylish&display=swap');
.stylish-regular {
  font-family: "Stylish", serif;
  font-weight: 400;
  font-style: normal;
}
.gugi-regular {
  font-family: "Gugi", sans-serif;
  font-weight: 400;
  font-style: normal;
}

.comment-box {
  display: flex;
  /* justify-content: space-between; */
  margin-left: 40px;
  margin-right: 40px;
  padding-left: 10px;
  padding-top: 10px;
  padding-bottom: 10px;
}

</style>