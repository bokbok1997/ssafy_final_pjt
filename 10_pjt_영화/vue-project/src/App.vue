<template>
  <div>
    <header>
      <nav class="navbar navbar-expand-lg navbar-light custom-navbar">
        <div class="container-fluid">
          <div class="d-flex align-items-center" style="margin-bottom: 30px;">
            <div class="menu-section">
              <RouterLink class="nav-link custom-link me-4" :to="{ name: 'MovieHomeView' }" active-class="active"><pre style="margin-bottom: 0%;font-size: xx-large;">HOME</pre></RouterLink>
              <span class="navbar-text custom-text"> | </span>
              <RouterLink class="nav-link custom-link mx-4" :to="{ name: 'MovieListView' }" active-class="active"><pre style="margin-bottom: 0%;font-size: xx-large;">MOVIE LIST</pre></RouterLink>
            </div>
          </div>
          <div class="d-flex align-items-center ms-auto" style="margin-bottom: 30px;">
            <div class="menu-section">
              <RouterLink v-if="!store.isLogin" class="nav-link custom-link mx-4" :to="{ name: 'SignUpView' }" active-class="active"><pre style="margin-bottom: 0%;font-size: xx-large;">SIGN UP</pre></RouterLink>
              <span v-if="!store.isLogin" class="navbar-text custom-text"> | </span>
              <RouterLink v-if="!store.isLogin" class="nav-link custom-link mx-4" :to="{ name: 'LogInView' }" active-class="active"><pre style="margin-bottom: 0%;font-size: xx-large;">LOGIN</pre></RouterLink>
              <a v-else class="nav-link custom-link mx-4" href="" @click.prevent="store.logOut()"><pre style="margin-bottom: 0%;font-size: xx-large;">LOGOUT</pre></a>
            </div>
          </div>
        </div>
      </nav>
    </header>
    <RouterView />
    <footer>
      <div class="custom-footer">
        <pre>Copyright ⓒ 2024 Seunghui & Hyunbok </pre>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
</script>

<style scoped>
.custom-navbar {
  background-color:rgb(255, 188, 96);
  height: 100px;
}

.custom-footer {
  background-color: rgb(255, 188, 96);
  height: 50px;
  text-align: center;
  margin-top: 50px;
  padding-top: 15px;
}

.menu-section {
  display: flex;
  align-items: center;
  margin-left: 30px;
  margin-top: 30px;
}

.navbar-text.custom-text {
  margin: 0 10px;
}

.nav-link.custom-link {
  color: black;
  text-decoration: none;
}

.nav-link.custom-link.active {
  font-weight: bold;
}

.d-flex.align-items-center.ms-auto {
  margin-left: auto;
  margin-right: 30px;
}
</style>