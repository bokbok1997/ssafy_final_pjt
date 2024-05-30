<template>
  <br><br>
    <div style="display: flex; flex-direction: column; align-items: center;">
        <h1>당신에게 맞는 영화를 추천받으세요!</h1>
        <br><br>
        <form @submit.prevent="formInfo()" style="border: solid black 1px;width: 620px;padding: 20px; text-align: center;background-color: rgb(250, 247, 243);">
            <p>
                <h3>당신의 성별은 무엇입니까?</h3>
                <input type="radio" name="gender" value="여성" v-model="gender"> 여성 &nbsp;&nbsp;
                <input type="radio" name="gender" value="남성" v-model="gender"> 남성 &nbsp;&nbsp;
            </p>
            <p>
                <h3>당신의 나이대는 무엇입니까?</h3>
                <input type="radio" name="age" value="10대" v-model="age"> 10대 &nbsp;&nbsp;
                <input type="radio" name="age" value="20대" v-model="age"> 20대 &nbsp;&nbsp;
                <input type="radio" name="age" value="30대" v-model="age"> 30대 &nbsp;&nbsp;
                <br>
                <input type="radio" name="age" value="40대" v-model="age"> 40대 &nbsp;&nbsp;
                <input type="radio" name="age" value="50대" v-model="age"> 50대 &nbsp;&nbsp;
                <input type="radio" name="age" value="60대 이상" v-model="age"> 60대 이상  
            </p>
            <p>
                <h3>좋아하는 분위기는 무엇입니까?</h3>
                 <input type="radio" name="mood" value="즐거운 분위기" v-model="mood"> 즐거운 분위기 &nbsp;&nbsp;
                 <input type="radio" name="mood" value="몽환적인 분위기" v-model="mood"> 몽환적인 분위기 &nbsp;&nbsp;<br><br>
                 <input type="radio" name="mood" value="어두운 분위기" v-model="mood"> 어두운 분위기 &nbsp;&nbsp;
                 <input type="radio" name="mood" value="가족같은 분위기" v-model="mood"> 가족같은 분위기 &nbsp;&nbsp;<br><br>
                 <input type="radio" name="mood" value="활기찬 분위기" v-model="mood"> 활기찬 분위기 &nbsp;&nbsp;
                 <input type="radio" name="mood" value="여유로운 분위기" v-model="mood"> 여유로운 분위기 &nbsp;&nbsp;
            </p>
            <button type="submit" class="btn btn-outline-dark" @click="search">제출하기</button>
        </form>
        <br><br><br>
        <div v-if="cnt>1">
        <h2><pre>당신을 위한 AI 추천 영화 🎬</pre></h2>
        <div style="display: flex;">
        <p v-for="thismovie in new_movieBox">
            <!-- {{ thismovie.title }} -->
            <img :src="`https://image.tmdb.org/t/p/w500/${thismovie.poster_path}`" alt="" @click="goDetail(thismovie.id, thismovie.movie_id)" style="width:200px; margin:20px;" class="card">
        </p>
        </div>
      </div>
    </div>
</template>

<script setup>
    const check = ref(0)
    const movieBox = ref('')
    const new_movieBox = ref([0,0,0,0,0])
    const randomNumber = ref(0)
    const rand_array = ref([0,0,0,0,0])
    const generateRandomNumber = (max_num) => {
    randomNumber.value = Math.floor(Math.random() * max_num) + 0
    rand_array.value[0]=randomNumber.value
    randomNumber.value = Math.floor(Math.random() * max_num) + 0
    rand_array.value[1]=randomNumber.value
    randomNumber.value = Math.floor(Math.random() * max_num) + 0
    rand_array.value[2]=randomNumber.value
    randomNumber.value = Math.floor(Math.random() * max_num) + 0
    rand_array.value[3]=randomNumber.value
    randomNumber.value = Math.floor(Math.random() * max_num) + 0
    rand_array.value[4]=randomNumber.value
    }

import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
const cnt = ref(0)
const store = useCounterStore()

const two_genres = ref([0,0])
const gender = ref('')
const age = ref('')
const mood = ref('')

const prompt = ref('')

const formInfo = function() {
    console.log(gender.value, age.value, mood.value)
    prompt.value = `아래 영화 키워드 중 [액션, 모험, 애니메이션, 코미디, 범죄, 다큐멘터리, 드라마, 가족, 판타지, 역사, 공포, 음악, 미스터리, 로맨스, SF, TV 영화, 스릴러, 전쟁, 서부] ${mood.value}를 선호하는 ${age.value} ${gender.value}이 좋아할만한 키워드 2개만 선택해 줘`
}


import OpenAI from 'openai'
const response = ref(null)

const getGPTResponse = async () => {
  try {
    const openai = new OpenAI({
      apiKey: `${import.meta.env.VITE_OPENAI_API_KEY}`,
      dangerouslyAllowBrowser: true,
    })
    const response1 = await openai.chat.completions.create({
      messages: [
        {
          role: 'user',
          content: prompt.value,
        },
      ],
      model: 'gpt-3.5-turbo',
    })
    console.log(prompt)
    console.log('chatGPT 결과: ', response1.choices[0].message.content)
    response.value = response1.choices[0].message.content.trim()
    console.log(response.value)

    let i = 0
    for (const genre of genre_names.value){
        console.log(genre)
        if (i===2){
            console.log(two_genres.value)
            break
        }
        if (response.value.includes(genre)){
            two_genres.value[i++]=genres.value[genre]
        }
    }



    
    movieBox.value = store.movies.filter((movie)=>{
        return ((movie.genre_ids==two_genres.value[1]) ||  (movie.genre_ids==two_genres.value[0]))
    })
    if (movieBox.value.length <= 5){
        check.value = 1
        // new_movieBox = movieBox
    }else{
        check.value = 1
        generateRandomNumber(movieBox.value.length)
        for(let iii=0; iii<5;iii++){
            console.log(movieBox.value[rand_array.value[iii]])
            new_movieBox.value[iii]=movieBox.value[rand_array.value[iii]]
        }
        console.log(new_movieBox.value)
    }

    console.log(movieBox.value.length)
    console.log(movieBox.value)

    
  } catch (error) {
    console.log('chatGPT: 에러가 발생했습니다.')
    console.log(error)
  }
}

const search = () => {
      response.value = null
      getGPTResponse()
      cnt.value++
    }
import { useRouter } from 'vue-router'

const router = useRouter()

defineProps({
  movie: Object,
})

const goDetail = function(id, movie_id) {
  router.push({name: 'DetailView', params: { id: id, movie_id:movie_id }})
}


const genre_names = ref([
    '액션',
  '모험',
  '애니메이션',
  '코미디',
  '범죄',
  '다큐멘터리',
  '드라마',
  '가족',
  '판타지',
  '역사',
  '공포',
  '음악',
  '미스터리',
  '로맨스',
  'SF',
  'TV 영화',
  '스릴러' ,
  '전쟁',
  '서부'
])
const genres = ref({
  '액션' : 28,
  '모험' : 12,
  '애니메이션' : 16,
  '코미디' : 35,
  '범죄' : 80,
  '다큐멘터리' : 99,
  '드라마' : 18,
  '가족' : 10751,
  '판타지' : 14,
  '역사' : 36,
  '공포' : 27,
  '음악' : 10402,
  '미스터리' : 9648,
  '로맨스' : 10749,
  'SF' : 878,
  'TV 영화' : 10770,
  '스릴러' : 53,
  '전쟁' : 10752,
  '서부' : 37
})
</script>

<style scoped>

</style>