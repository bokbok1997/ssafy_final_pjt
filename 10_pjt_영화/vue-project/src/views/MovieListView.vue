<template>
  <div>
    <h1 class="gugi-regular" style="text-align: center;margin-top: 10px;">영화목록</h1>
    <MovieList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import MovieList from '@/components/MovieList.vue'

const store = useCounterStore()

onMounted(() => {
  // store.getArticles()
  store.getMovies()
})

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
