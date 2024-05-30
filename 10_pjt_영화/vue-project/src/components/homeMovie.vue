<template>
    <div>
    <div class="container">
    <div class="row"><br><br>
      <div style="text-align: center;" class="col-4">
        <h1 class="gugi-regular ">전국</h1>
        <img src="/public/KOREA.png" alt="#" style="height: 600px;">
      </div>

      <div class="col-8">
        <h1 style="text-align: center;" class="gugi-regular ">현재 상영중인 영화 목록</h1>
          <div v-if="boxOffices">
            <div style="display:flex; flex-wrap: wrap;">
                <p v-for="boxOffice in boxOffices" :key="boxOffice.movieCd">
                <!-- <li>{{ boxOffice }}</li> -->
              <div style="color:black;justify-content: space-evenly; width: 240px;height: 300px; margin: 20px;padding: 10px;background-color: rgb(255, 188, 96);text-align: center;" class="card stylish-regular">
                <p style="font-size: x-large;">{{ boxOffice.movieNm }}</p>
                <p>현재 순위 : {{ boxOffice.rank }} 등</p>
                <p>개봉일 : {{ boxOffice.openDt }}</p>
                <p>누적 관객수 : {{ boxOffice.audiAcc }} 명</p>
                <p>전날 관객수 : {{ boxOffice.audiCnt }} 명</p>
                <button type="button" class="btn btn-outline-light" @click="findDetail(boxOffice.movieNm)"><pre style="margin-bottom: 0px;">more_info</pre></button>
              </div>
                <br><br>
                </p>
            </div>
          </div>
          <div v-else>
            데이터 로드 중...
          </div>
      </div>
    </div>
    </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter} from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const boxOffices = ref(null)

onMounted(async () => {
  // 비동기 호출로 데이터를 로드
  await store.latestMovie()
  boxOffices.value = store.boxOffice.boxOfficeResult.dailyBoxOfficeList
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
</style>