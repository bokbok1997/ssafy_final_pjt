<template>
  <div>
    <div>
      <div style="background-color: rgb(250, 247, 243);"><hr>
        <div style="display: flex; justify-content: center; flex-direction: row;">
          <h1 class="gugi-regular "> 📽 오늘의 추천 영화 </h1>
          <img src="`/public/update_icon.png`" alt="#" @click="generateRandomNumber" class="circular-button">
          <!-- <button @click="generateRandomNumber" class="circular-button">다른 추천</button> -->
        </div>
        <div v-if="rand_array != [0,0,0,0,0]" class="random-movie-box">
          <p v-for="thismovie in movieBox">
              <img :src="`https://image.tmdb.org/t/p/w500/${thismovie.poster_path}`" alt="" @click="goDetail(thismovie.id, thismovie.movie_id)" style="width:200px;display: flex; ">
          </p>
        </div><hr>
      </div>
      <br><br>
      <div style="text-align: center"><img src="/public/foam_png.png" alt="#" @click="goForm()" ></div>
    </div>

<br><br><br>
  <div style="text-align: center;">
    <h2 class="gugi-regular ">지역 별 현재 상영중인 영화 정보</h2>

    <div style="background-color: rgb(255, 188, 96);">
      <hr>
    <RouterLink :to="{name:'MovieHomeView'}" style="text-decoration: none;"><button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">전국</p></button> </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105001'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">서울</p></button></RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105002'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">경기도</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105003'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">강원도</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105004'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">충청북도</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105005'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">충청남도</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105006'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">경상북도</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105007'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">경상남도</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105008'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">전라북도</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105009'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">전라남도</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105010'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">제주도</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105011'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">부산시</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105012'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">대구시</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105013'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">대전시</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105014'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">울산시</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105015'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">인천시</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105016'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">광주시</p></button>  </RouterLink> &nbsp;
    <RouterLink :to="{name:'MovieRegion', params:{regionNum:'0105017'}}" style="text-decoration: none;"> <button type="button" class="btn btn-outline-dark"><p class="stylish-regular" style="margin-bottom:0px ;">세종시</p></button>  </RouterLink>
      <hr>
  </div>
    <br><br><br>
  </div>
    <RouterView/>
  </div>
</template>

<script setup>
const movieBox = ref('')
const randomNumber = ref(0)
const rand_array = ref([204,210,34,243,100])

import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, RouterLink, RouterView } from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const boxOffices = ref(null)


const generateRandomNumber = () => {
  randomNumber.value = Math.floor(Math.random() * 257) + 1
  rand_array.value[0]=randomNumber.value
  randomNumber.value = Math.floor(Math.random() * 257) + 1
  rand_array.value[1]=randomNumber.value
  randomNumber.value = Math.floor(Math.random() * 257) + 1
  rand_array.value[2]=randomNumber.value
  randomNumber.value = Math.floor(Math.random() * 257) + 1
  rand_array.value[3]=randomNumber.value
  randomNumber.value = Math.floor(Math.random() * 257) + 1
  rand_array.value[4]=randomNumber.value

  movieBox.value = store.movies.filter((movie)=>{
        return ((movie.id==rand_array.value[0]) ||  (movie.id==rand_array.value[1])||(movie.id==rand_array.value[2])||(movie.id==rand_array.value[3])||(movie.id==rand_array.value[4]))})
  }
  console.log(movieBox)


onMounted(async () => {
  // 비동기 호출로 데이터를 로드
  await store.latestMovie()
  // await store.getMovies()
  boxOffices.value = store.boxOffice.boxOfficeResult.dailyBoxOfficeList
  movieBox.value = store.movies.filter((movie)=>{
        return ((movie.id==rand_array.value[0]) ||  (movie.id==rand_array.value[1])||(movie.id==rand_array.value[2])||(movie.id==rand_array.value[3])||(movie.id==rand_array.value[4]))})
})

const findDetail = (title) => {
  const movieTitle = title.split(' ').join('')
  const targetMovie = store.movies.find((movie) => {
    return movieTitle === movie.title.split(' ').join('')
  })
  if (targetMovie) {
    router.push({ name: 'DetailView', params: { id: targetMovie.id, movie_id : targetMovie.movie_id } })
  }
}

defineProps({
  movie: Object,
})

const goDetail = function(id, movie_id) {
  router.push({name: 'DetailView', params: { id: id, movie_id:movie_id }})
}

const goForm = function() {
  router.push({name:'FormView'})
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

.random-movie-box {
  display: flex;
  justify-content: space-evenly;
}

.circular-button {
    width: 30px;
    height: 30px;
    /* border-radius: 80%; */
    border: none;
    margin-top: 7px;
    margin-left: 15px;
    color: white;
    font-size: 15px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.3s;
    
}
</style>
  