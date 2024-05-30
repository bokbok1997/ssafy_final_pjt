<template>
    <div>
        <h1 style="text-align: center;"><pre>Review 📃</pre></h1>
        <!-- {{ movie.title }}
        {{ mid }} -->
        <div class="mb-1 ps-5 pe-5" style="display: flex; flex-direction: column;">
            <h4>리뷰 작성하기 ✒</h4>
            <hr>
            <form @submit.prevent="createReview(mid)">
                <div>
                    <label for="title">제목 : </label>
                    <!-- <label for="title" class="form-label">제목 : </label> -->
                    <input id="title" type="text" v-model="title" class="form-control" placeholder="제목을 입력하세요">
                    <br>
                    <label for="content">내용 : </label>
                    <textarea id="content" cols="30" rows="6" v-model="content" class="form-control" placeholder="내용을 입력하세요"></textarea>
                    <br>
                </div>
                <div style="display: flex; justify-content: flex-end;">
                    <button type="submit" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">작성하기</p></button>
                </div>
                <!-- <input type="submit" value="작성하기"> -->
            </form>
        </div>
        <hr>
        <div v-if="thisReivew.length === 0" class="mb-1 ps-5 pe-5">
            <br>
            <h3>😥 아직 리뷰가 없습니다.</h3>
            <br>
            <br>
            <br>
        </div>
        <div v-else>
            <ReviewList 
                v-for="review in thisReivew"
                :key="review.id"
                :review="review"
            />
            <!-- <div v-for="review in thisReivew">
                {{ review.id }}
                <h4>{{ review.title }}</h4>
                <p>{{ review.content }}</p>
                <hr>

            </div> -->
        </div>

    </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import ReviewList from '@/components/ReviewList.vue'

const props = defineProps({
    movie : Object,
    mid : Number
})

// const props2 = defineProps(['mid'])

// console.log(props)
// console.log(props.mid)

const title = ref('')
const content = ref('')
const store = useCounterStore()
const route = useRouter()
// const thisReivew = ref([])

onMounted(() => {
    store.getReviews()
})
// 해당 영화에 달린 리뷰들
const thisReivew = ref([])

thisReivew.value = store.reviews.filter((review) => {
        // console.log(review.movie)
        // console.log(props.mid)
        let movId = Number(props.mid)
    return review.movie == movId
})


watch(() => store.reviews, (newValue) => {
    thisReivew.value = newValue.filter((review) => {
    // console.log('watch=========');
    // console.log(review);
    let movId = Number(props.mid);
    return review.movie == movId;
});
}, { deep: true });

// console.log(thisReivew[0])

// watch(store.reviews, (newValue) => {
//     thisReivew.value = newValue.filter((review) =>{
//         console.log('watch=========')
//         console.log(review)
//         let movId = Number(props.mid)
//         return review.movie == movId
//     })
//     // console.log(thisReivew)
// })



// thisReivew.value = computed(() => {
//     const targetMovie = store.review.filter((reivew) => {
//         let movId = Number(props.mid)
//         return review.movie == movId
//     })
//     return targetMovie
// })

// watch(thisReivew, (newValue, oldValue) => {

// })

// console.log(store.reviews)

// console.log(thisReivew)
// console.log(thisReivew.value)



const createReview = function (movieId) {
    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/reviews/`,
      data : {
        title : title.value,
        content : content.value,
        movie : movieId
      },
      headers : {
        Authorization : `Token ${store.token}`
      },
      
    })
      .then(response => {
        // title.value.reset()
        // content.value.reset()
        title.value = ''
        content.value = ''
        console.log('보내기 성공!')
        store.getReviews()
        // watch(() => store.reviews, (newValue) => {
        //     thisReivew.value = newValue.filter((review) => {
        //     console.log('watch=========');
        //     console.log(review);
        //     let movId = Number(props.mid);
        //     return review.movie == movId;
        // });
        // }, { deep: true });
    // console.log(thisReivew)
      })
      .catch(error => {
        console.log(error)
      })

  }

</script>

<style scoped>

</style>