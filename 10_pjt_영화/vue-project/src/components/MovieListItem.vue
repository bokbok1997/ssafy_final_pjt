<template>
  <div class="movie-list-one">
    <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="" @click="goDetail(movie.id, movie.movie_id)">
  </div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()

defineProps({
  movie: Object,
})

const goDetail = function(id, movie_id) {
  router.push({name: 'DetailView', params: { id: id, movie_id:movie_id }})
}


</script>

<style scoped>

.movie-list-one {
  border: 1px solid black;
  border-radius: 10px;
  background-color: rgb(255, 188, 96);
  margin: 5px;
  padding: 5px;
  padding-top: 10px;
}

</style>
