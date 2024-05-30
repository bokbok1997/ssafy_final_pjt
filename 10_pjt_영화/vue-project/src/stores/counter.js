import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  
  // 모든 리뷰를 담은 ref
  const reviews = ref([])
  //모든 댓글을 담은 ref
  const comments = ref([])
  // 모든 영화 목록을 담은 ref
  const movies = ref([])
  // 현재 상영작 영화 목록을 담은 ref
  const boxOffice = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  // 현재 로그인한 유저의 이름(유저네임)
  const nowUser = ref(null)

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const router = useRouter()
  const movieAPI = import.meta.env.VITE_MOVIE_API
  const tmdbLongAPI = import.meta.env.VITE_TMDB_LONG_API

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



  // 최근 개봉 영화(박스오피스) 관련으로 받은 정보
  const latestMovie = function () {
    axios({
      method:'get',
      url:'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json',
      params : {
        key : movieAPI,
        targetDt : date,
        itemPerPage : '5'
      }
    })
      .then((response) => {
        console.log(response.data)
        boxOffice.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }

  // 영화에 달린 리뷰를 가져오는 함수
  const getReviews = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/reviews/`,
      headers : {
        Authorization : `Token ${token.value}`
      }
    })
      .then(response => {
        reviews.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  // 리뷰에 달린 댓글을 가져오는 함수
  const getComments = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/comments/`,
      headers : {
        Authorization : `Token ${token.value}`
      }
    })
      .then(response => {
        comments.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`,
      headers : {
        Authorization : `Token ${token.value}`
      }
    })
      .then(response => {
        // console.log(response)
        // console.log(movieAPI)
        movies.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const signUp = function (payload) {
    // 1) 사용자 입력 데이터를 받아
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2
    // 구조 분해 할당을 사용하기
    const { username, password1, password2 } = payload
    // 2) axios로 django에 요청을 보냄
    axios({
      method:'post',
      url :  `${API_URL}/accounts/signup/`,
      data : {
        // username : username,
        // password1 : password1,
        // password2 : password2,
        username,
        password1,
        password2
      }
    })
      .then((response) => {
        console.log('회원가입 성공!')
        const password = password1
        logIn({username, password})
      })
      .catch((error) => {
        console.log(error)
        window.alert('회원가입에 실패하였습니다. 다시 입력해주세요.')
      })

  }

  const logIn = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password } = payload
    nowUser.value = username
    // 2. axios로 django에 요청을 보냄
    axios({
      method:'post',
      url: `${API_URL}/accounts/login/`,
      data : {
        username, password
      }
    })
      .then((response) => {
        // console.log('로그인 성공!')
        // console.log(response)
        // console.log(response.data.key)
        // 3. 로그인 성공 후 응답 받은 토큰을 저장
        console.log(response.data)
        token.value = response.data.key
        router.push({name:'MovieHomeView'})
      })
      .catch((error) => {
        console.log(error)
        window.alert('아이디 혹은 비밀번호를 제대로 입력해주세요!')
      })

  }

  // +) 로그아웃은 django 로그아웃 url로 요청을 보내기 + 우리 token 값을 null 값으로 바꾸기를 하면 된다!!!
  
  const logOut = function () {
    axios({
      method:'post',
      url: `${API_URL}/accounts/logout/`,
      params:{
        'Media type' : 'application/json',
        'Content' : ''
      }
    })
      .then((response) => {
        console.log(response)
        token.value = null
        router.push({name:'LogInView'})
      })
      .catch((error) => {
        console.log(error)
      })
  }

  


  return {
    reviews, API_URL, getReviews, signUp, logIn,
    token, isLogin, logOut, getMovies, movies,
    latestMovie, boxOffice, tmdbLongAPI,
    comments, getComments, nowUser
  }
}, { persist: true })

