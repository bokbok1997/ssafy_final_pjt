<template>
  <div>

    <!-- {{ movie }} -->
    <div class="movie-box">
      <div class="movie-inside">
        <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="">
        <div class="movie-overview">
          <img :src="logoURL" alt="" ><hr><br><br>
          <p class="gugi-regular" style="font-size: xx-large;">평점 : {{ movie.vote_average }}점</p>
          <!-- <h2>제목 : {{ movie.title }}</h2> -->
          <div class="p-3" style="background-color: white; border-radius: 10px;">
            <!-- <h2><pre>overview</pre></h2> -->
            <p class='stylish-regular' style="font-size: xx-large;">{{ movie.overview }}</p>
          </div>
        </div>
      </div>
      <br><hr>
    </div>
    <!-- {{ logoURL }} -->
    <!-- <h3>{{ movie.title }}</h3> -->
    <p>{{ index }}</p>
    <!-- <p>{{ typeof(movie) }}</p> -->
    <!-- <p>{{ movie.id }}</p> -->
    <p>{{ movie.pk }}</p>
   
    <div v-if="movieTrail !== ''" style="text-align: center;">
      <iframe width="600" height="375" :src="movieTrail" :title="movie.title" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
    <div v-else style="text-align: center;">
      <!-- <p>배경을 넣을 예정</p> -->
      <img :src="`https://image.tmdb.org/t/p/w500${movie.backdrop_path}`" alt="">
    </div>
    

    <div v-if="fiveMovie" style="background-color: rgb(250, 247, 243);">
      <hr><br>
      <h2 class="gugi-regular " style="text-align: center;">비슷한 영화 추천</h2><br>
      <card class="similar-movie-box">
        <div v-for="simMovie in fiveMovie" @click="goDetail(simMovie.id, simMovie.movie_id)">
          <img :src="`https://image.tmdb.org/t/p/w300/${simMovie.poster_path}`" alt="">
  
        </div>

      </card>
      <br><hr>
    </div>


    <Review :movie="movie" :mid="moviePk" />

  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, RouterLink, RouterView, useRouter } from 'vue-router'
import Review from '@/components/Review.vue'
import { setMapStoreSuffix } from 'pinia'

const store = useCounterStore()
const route = useRoute()
// console.log(route.params)
const movieId = ref(route.params.movie_id)
const moviePk = route.params.id
// console.log(movieId)
// console.log(movieId)
// const movie = ref([])
const movie = ref(null)
const movieTrail = ref('')
// const lang = ref('')
const logoURL = ref('')
const similarMovie = ref('')
const fiveMovie = ref([0,0,0,0,0])
const targetMovie = ref(null)
// const backURL = ref(`https://image.tmdb.org/t/p/w500${movie.value.backdrop_path}`)
// console.log(backURL.value)
// console.log(movie.value)

// movieTrail.value = `https://www.youtube.com/embed/${response.results[0].key}`

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


watch(() => route.params.movie_id,
(newMovieId) => {
    movieId.value = newMovieId
    // 해당 영화의 디테일의 정보를 받을 비동기 요청
    const MovieDetail = {
      method: 'GET',
      url: `https://api.themoviedb.org/3/movie/${movieId.value}`,
      params: {language: 'ko-KOR'},
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${store.tmdbLongAPI}`
      }
    };

    axios
      .request(MovieDetail)
      .then(function (response) {
        // console.log(response.data);
        // console.log(response.data.genres[0].id);
        // console.log(response)
        movie.value = response.data
        // lang = response.data.original_language
        // console.log(movie.value.genres[0].id)
        // findGenre(response.data.genres[0].id)


      })
      .catch(function (error) {
        console.error(error);
        
      });


    // 영화 트레일러 받기
    const findMovieTrail = {
    method: 'GET',
    url: `https://api.themoviedb.org/3/movie/${movieId.value}/videos?`,
    params: {language: 'ko-KOR'},
    headers: {
      accept: 'application/json',
      Authorization: `Bearer ${store.tmdbLongAPI}`
    }
    };

    axios
    .request(findMovieTrail)
    .then(function (response) {
      // console.log(response.data);
      // console.log(response.data.results[0].key)
      if (response.data.results[0]) {
        movieTrail.value = `https://www.youtube.com/embed/${response.data.results[0].key}`
        // console.log(movieTrail.value)
      }
    })
    .catch(function (error) {
      console.error(error);
      
    });

    // 영화 로고 받기
    const findLogo = {
      method: 'GET',
      url: `https://api.themoviedb.org/3/movie/${movieId.value}/images`,
      params: {language: 'en'},
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${store.tmdbLongAPI}`
      }
    };

    axios
      .request(findLogo)
      .then(function (response) {
        // console.log(response.data);
        logoURL.value = `https://image.tmdb.org/t/p/w200${response.data.logos[0].file_path}`
      })
      .catch(function (error) {
        console.error(error);
      });

  

    targetMovie.value = store.movies.find((movie) => {
      return movie.id == moviePk
    })
    similarMovie.value = store.movies.filter((mv) => {
      return mv.genre_ids == targetMovie.value.genre_ids
    })

    if (similarMovie.value.length < 6) {
      fiveMovie.value = similarMovie.value
      
      const index = fiveMovie.value.findIndex((mv) => {
        return mv.id == moviePk
      })
      fiveMovie.value.splice(index,1)
    } else {
      generateRandomNumber(similarMovie.value.length)
      for (let i=0; i<5; i++) {
        fiveMovie.value[i] = similarMovie.value[rand_array.value[i]]
      }

      const index = fiveMovie.value.findIndex((mv) => {
        return mv.id == moviePk
      })
      fiveMovie.value.splice(index,1)
    }
  }
)

onMounted(() => {
  targetMovie.value = store.movies.find((movie) => {
    return movie.id == moviePk
  })
  similarMovie.value = store.movies.filter((mv) => {
    return mv.genre_ids == targetMovie.value.genre_ids
  })

  if (similarMovie.value.length < 6) {
    fiveMovie.value = similarMovie.value
    
    const index = fiveMovie.value.findIndex((mv) => {
      return mv.id == moviePk
    })
    fiveMovie.value.splice(index,1)
  } else {
    generateRandomNumber(similarMovie.value.length)
    for (let i=0; i<5; i++) {
      fiveMovie.value[i] = similarMovie.value[rand_array.value[i]]
    }

    const index = fiveMovie.value.findIndex((mv) => {
      return mv.id == moviePk
    })
    fiveMovie.value.splice(index,1)
  }

  
  // console.log(targetMovie.value)
})

// console.log(targetMovie)

// 비슷한 영화 디테일로 넘어가는 함수
const router = useRouter()
const goDetail = function(id, movie_id) {
  router.push({name: 'DetailView', params: { id: id, movie_id:movie_id }})
}


// 해당 영화의 디테일의 정보를 받을 비동기 요청
const MovieDetail = {
  method: 'GET',
  url: `https://api.themoviedb.org/3/movie/${movieId.value}`,
  params: {language: 'ko-KOR'},
  headers: {
    accept: 'application/json',
    Authorization: `Bearer ${store.tmdbLongAPI}`
  }
};

axios
  .request(MovieDetail)
  .then(function (response) {
    // console.log(response.data);
    // console.log(response.data.genres[0].id);
    // console.log(response)
    movie.value = response.data
    // lang = response.data.original_language
    // console.log(movie.value.genres[0].id)
    // findGenre(response.data.genres[0].id)


  })
  .catch(function (error) {
    console.error(error);
    
  });


// 영화 트레일러 받기
const findMovieTrail = {
method: 'GET',
url: `https://api.themoviedb.org/3/movie/${movieId.value}/videos?`,
params: {language: 'ko-KOR'},
headers: {
  accept: 'application/json',
  Authorization: `Bearer ${store.tmdbLongAPI}`
}
};

axios
.request(findMovieTrail)
.then(function (response) {
  // console.log(response.data);
  // console.log(response.data.results[0].key)
  if (response.data.results[0]) {
    movieTrail.value = `https://www.youtube.com/embed/${response.data.results[0].key}`
    // console.log(movieTrail.value)
  }
})
.catch(function (error) {
  console.error(error);
  
});

// 영화 로고 받기
const findLogo = {
  method: 'GET',
  url: `https://api.themoviedb.org/3/movie/${movieId.value}/images`,
  params: {language: 'en'},
  headers: {
    accept: 'application/json',
    Authorization: `Bearer ${store.tmdbLongAPI}`
  }
};

axios
  .request(findLogo)
  .then(function (response) {
    // console.log(response.data);
    logoURL.value = `https://image.tmdb.org/t/p/w200${response.data.logos[0].file_path}`
  })
  .catch(function (error) {
    console.error(error);
  });


// console.log(movie)
// console.log('벨류 적용 : ---- ', movie.value)



// similarMovie = store.movies.filter((mv) => {
//   return mv.genre_ids = movie.value.genre_ids
// })


// const findMovieTrail = {
// method: 'GET',
// headers: {
//   accept: 'application/json',
//   Authorization: `Bearer ${store.tmdbLongAPI}`
// }
// };

// fetch(`https://api.themoviedb.org/3/movie/${movieId}/videos?language=ko-KOR`, findMovieTrail)
//   .then(response => response.json())
//   .then(response => movieTrail.value = `https://www.youtube.com/embed/${response.results[0].key}`)
//   .catch(err => console.error(err));


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


.movie-box {
  background-color: rgb(250, 247, 243);
  padding: 10px;
  padding-bottom: 0px;
  z-index: 5;
}

.movie-box {
  background-image: url();
}

.movie-inside {
  display: flex;
}

.movie-overview {
  background-color:  rgb(255, 188, 96);
  /* background-color:  rgb(224, 243, 118,0.4); */
  /* opacity: 70%; */
  margin: 10px;
  padding: 20px;
  padding-top: 10px;
  margin-top: 0px;
  align-content: center;
}

.similar-movie-box {
  display: flex;
  justify-content: space-evenly;
}

</style>
