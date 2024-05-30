<template>
  <div class="container">
    <div  class="row"><br><br>
      <div style="text-align: center;" class="col-4">
        <!-- {{ region_boxOffice }} -->
        <h1 class="gugi-regular ">{{region_name[0][regionId]}}</h1>
        <img :src="`/public/${regionId}.png`" alt="#" style="height: 600px;">
      </div>
        <div class="col-8">
          <h1 style="text-align: center;" class="gugi-regular ">현재 상영중인 영화 목록</h1>
            <div v-if="region_boxOffice">
            <div style="display:flex; flex-wrap: wrap;">
                <p v-for="boxOffice in region_boxOffice" :key="boxOffice.movieCd">
                <!-- <li>{{ boxOffice }}</li> -->
                <div style="color:black;justify-content: space-evenly; width: 240px;height: 300px; margin: 20px;padding: 10px; background-color: rgb(255, 188, 96); text-align: center;" class="card stylish-regular">
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
</template>

<script setup>
import { ref, onMounted, onUpdated ,watch} from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter,useRoute,onBeforeRouteUpdate} from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const route = useRoute()
const regionId = ref(route.params.regionNum)
const boxOffices = ref(null)
console.log(regionId.value)
//////////////////////////////////////////////////////////

let today = new Date()
let year = today.getFullYear()
let month = today.getMonth() + 1
let day = today.getDate() - 1
let date = ''

if (month < 10) {
  date = year.toString() + '0' + month.toString() + day.toString()
} else {
  date = year.toString() + month.toString() + day.toString()
}

const movieAPI = import.meta.env.VITE_MOVIE_API
import axios from 'axios'
const region_boxOffice = ref([])

const Region_latestMovie = function (rnum) {
    axios({
      method:'get',
      url:'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json',
      params : {
        key : movieAPI,
        targetDt : date,
        itemPerPage : '5',
        wideAreaCd: rnum
      }
    })
      .then((response) => {
        console.log(response.data)
        region_boxOffice.value = response.data.boxOfficeResult.dailyBoxOfficeList
      })
      .catch((error) => {
        console.log(error)
      })
  }

  onMounted(() => {
    Region_latestMovie(regionId.value)
})

watch(() => route.params.regionNum,
(newRegionNum) => {
    regionId.value = newRegionNum
    Region_latestMovie(newRegionNum)
  }
)

const findDetail = (title) => {
  const movieTitle = title.split(' ').join('')
  const targetMovie = store.movies.find((movie) => {
    return movieTitle === movie.title.split(' ').join('')
  })
  if (targetMovie) {
    router.push({ name: 'DetailView', params: { id: targetMovie.id, movie_id : targetMovie.movie_id } })
  }
}

const region_name=ref([
    {
      "0105001": "서울시",
      "0105002": "경기도",
      "0105003": "강원도",
      "0105004": "충청북도",
      "0105005": "충청남도",
      "0105006": "경상북도",
      "0105007": "경상남도",
      "0105008": "전라북도",
      "0105009": "전라남도",
      "0105010": "제주도",
      "0105011": "부산시",
      "0105012": "대구시",
      "0105013": "대전시",
      "0105014": "울산시",
      "0105015": "인천시",
      "0105016": "광주시",
      "0105017": "세종시",
    }
])
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