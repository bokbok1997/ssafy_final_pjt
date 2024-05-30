import { createRouter, createWebHistory } from 'vue-router'
import MovieListView from '@/views/MovieListView.vue'
import DetailView from '@/views/DetailView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import MovieHomeView from '@/views/MovieHomeView.vue'
import MovieRegion from '@/components/MovieRegion.vue'
import homeMovie from '@/components/homeMovie.vue'
import FormView from '@/views/FormView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/MovieList',
      name: 'MovieListView',
      component: MovieListView
    },
    {
      path: '/movies/:id/:movie_id',
      name: 'DetailView',
      component: DetailView,
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/',
      component: MovieHomeView,
      children : [
        {path: '', name: 'MovieHomeView', component:homeMovie },
        {path: 'region/:regionNum', name:'MovieRegion', component:MovieRegion}
      ]
    },
    {
      path : '/form',
      name : 'FormView',
      component : FormView
    },
  ]
})  

import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'

// to 는 이동하려는 곳 / from은 현재 있는 위치
router.beforeEach((to, from) => {
  const store = useCounterStore()
  // 인증되지 않은 사용자는 영화 리스트 및 디테일에 접근 할 수 없음
  if ((to.name === 'MovieListView' || to.name === 'DetailView' || to.name === 'FormView') && store.isLogin === false) {
    window.alert('로그인이 필요해요!')
    return { name:'LogInView' }
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin === true)) {
    window.alert('이미 로그인했습니다.')
    return { name:'MovieHomeView'}
  }
})

export default router