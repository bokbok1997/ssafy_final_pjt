<template>
  <div style="background-color: rgb(250, 247, 243);">
    <div>
    <!-- <h3>Article List</h3> -->
    <hr><br>
    <div class="ms-5">
      <form @submit.prevent="MovieSearch(searchName)">
        <div style="display: flex; line-height: 40px;">
          <label for="search" class="gugi-regular"> 🔎 영화 검색 : &nbsp;</label>
          <input id="search" type="text" v-model="searchName" class="form-control" placeholder="검색어를 입력하세요" style="max-width: 300px;">
          &nbsp;
          <!-- <input type="submit" value="검색" class="gugi-regular"> -->
          <button type="submit" class="btn btn-outline-dark"><p class="gugi-regular" style="margin-bottom:0px ;">검색</p></button>
        </div>
      </form>
      <br>
      <div>
        <form>
          <select @change="selectGenre($event)" class="form-select" style="max-width: 200px;">
            <option value="0" >장르를 선택하세요.</option>
            <option :value="key" v-for=" (item, key) in genres">{{ key }}</option>
          </select>
        </form>
        <br><br>
      </div>
    </div>
  </div>
    <!-- <form action="">
      <input type="text" value="검색할 제목을 입력하시요">
    </form>
    <form>
      <select name="" id="select">
        <option value="">장르를 선택하세요.</option>
      </select>
    </form> -->
    <div class="movie-list-box"><hr><br>
      <MovieListItem 
        v-for="movie in movieList"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import MovieListItem from '@/components/MovieListItem.vue'
import { onMounted, ref } from 'vue'
import axios from 'axios'

const searchName = ref('')
const store = useCounterStore()
const movieList = ref([])
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
const num = ref(0)

const selectGenre = function(event) {
  // console.log(event.target.value)
  const gen = event.target.value
  // console.log(typeof(event.target.value))
  if (gen !== 0) {
    num.value = genres.value[gen]
  } else {
    num.value = 0
  }
  console.log(num.value)
  // console.log(typeof(num))

  if (!num.value || num.value == 0) {
    movieList.value = store.movies
  } else {
    movieList.value = store.movies
    movieList.value = movieList.value.filter((movie) => {
      return num.value == movie.genre_ids
    })
  }
  console.log('잘 필터 됨!!')
  console.log(num.value)
}

movieList.value = store.movies

const MovieSearch = function (name) {
  // console.log(name)
  // console.log(name)
  // console.log(typeof(name))
  if (!name) {
    movieList.value = store.movies
  } else {
    movieList.value = store.movies
    const tempName = name.split(' ').join('')
    // console.log(tempName)
    // console.log(movieList.length)
    movieList.value = movieList.value.filter((movie) => {
      // console.log(movie.title.split(' ').join(''))
      const movieTitle = movie.title.split(' ').join('')
      return movieTitle.includes(tempName)
      // return tempName in movie.title.split(' ').join('')
    })
    console.log('뽑은 무비 리스트')
    console.log(movieList.value)
    console.log(movieList.value.length)
    if (movieList.value.length === 0) {
      window.alert('검색 결과가 없습니다.')
      movieList.value = store.movies
    }

  }
  searchName.value = ''
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

.movie-list-box {
  display: flex;
  flex-wrap: wrap;
  padding: 10px;
  justify-content: center;
  background-color: rgb(250, 247, 243);

}

</style>