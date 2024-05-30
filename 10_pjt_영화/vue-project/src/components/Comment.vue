<template>
    <div>
        <CommentList
          v-for="comment in thisComment"
          :key = comment.id
          :comment="comment"
        />
        <div class="mt-5 mb-1 ps-5 pe-5" style="display: flex; flex-direction: column;">
          <h4>댓글 작성하기 🖊</h4>
          <form @submit.prevent="createComment(reviewId)">
            <div style="display: flex;">
              <input id="content" cols="30" rows="6" v-model="content" class="form-control me-3" placeholder="내용을 입력하세요">
              <button type="submit" class="btn btn-outline-dark" style=" --bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem; min-width: 70px;">
                댓글달기
              </button>
              <!-- <input type="submit" value="작성하기"> -->
            </div>
          </form>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import CommentList from '@/components/CommentList.vue'

const props = defineProps({
    reviewId : Number
})

const title = ref('')
const content = ref('')
const store = useCounterStore()
const route = useRouter()

onMounted(() => {
    store.getComments()
})

// 해당 리뷰에 달린 댓글들
const thisComment = ref([])


thisComment.value = store.comments.filter((comment) => {
        // console.log(review.movie)
        // console.log(props.mid)
        let reviewId = Number(props.reviewId)
    return comment.review == reviewId
})


watch(() => store.comments, (newValue) => {
    thisComment.value = newValue.filter((comment) => {
    // console.log('watch=========');
    // console.log(review);
    let reviewId = Number(props.reviewId);
    return comment.review == reviewId;
});
}, { deep: true });


const createComment = function (reviewId) {
    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/comments/`,
      data : {
        content : content.value,
        review : reviewId
      },
      headers : {
        Authorization : `Token ${store.token}`
      },
      
    })
      .then(response => {
        // title.value.reset()
        // content.value.reset()
        content.value = ''
        console.log('보내기 성공!')
        store.getComments()
      })
      .catch(error => {
        console.log(error)
      })

  }


</script>

<style scoped>

</style>