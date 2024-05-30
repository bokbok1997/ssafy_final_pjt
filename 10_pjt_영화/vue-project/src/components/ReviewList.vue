<template>
    <div style="background-color: rgb(250, 247, 243);">
        <div class="review-box p-3">
            <div>
              <div style="display: flex;">
                <h4>📝 {{ review.title }}</h4>
                &nbsp; &nbsp; &nbsp;
                <span>😊 {{ reviewUser }}</span>
              </div>
              <div class="ps-4 pt-2">
                <p>{{ review.content }}</p>
              </div>
            </div>
            <p v-if="reviewUser === store.nowUser">
              <button @click="deleteReview(review.id)" type="button" class="btn btn-secondary" style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;">
                DEL
              </button>
                <!-- <button @click="deleteReview(review.id)">삭제</button> -->
            </p>
        </div>
        <Comment
            :review-id="reviewId"
        />
        <hr>
        <!-- {{ isAuthenicated.user }} -->
    </div>
</template>

<script setup>
import Comment from '@/components/Comment.vue'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios';

const store = useCounterStore()
// const reviewUser = ref(null)

const props = defineProps({
    review : Object
})

// console.log(props.review.id)
const reviewId = props.review.id
const reviewUser = ref('')
// console.log('-------------')
// console.log(reviewId, typeof(reviewId))
// console.log(typeof(reviewId))

const findUser = function (reviewPk) {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/reviews/${reviewPk}/find_user/`,
      headers : {
        Authorization : `Token ${store.token}`
      },
      
    })
      .then(response => {
        // console.log(response.data.username)
        reviewUser.value = response.data.username
        // title.value.reset()
        // content.value.reset()
        // store.getReviews()
      })
      .catch(error => {
        console.log(error)
      })

  }

findUser(reviewId)

const deleteReview = function (reviewPk) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/api/v1/reviews/${reviewPk}/`,
      headers : {
        Authorization : `Token ${store.token}`
      },
      
    })
      .then(response => {
        // title.value.reset()
        // content.value.reset()
        console.log('삭제성공!')
        store.getReviews()
      })
      .catch(error => {
        console.log(error)
      })

  }

</script>

<style scoped>

.review-box {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid black;

}

</style>