<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'

const menu = ref('menu hidden')
const toggleMenu = () => {
  menu.value = menu.value === 'menu hidden' ? 'menu' : 'menu hidden'
}

</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <button class="menu-btn" @click="toggleMenu">menu</button>
      <div :class="menu">
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/contact">Contact</RouterLink>
      </div>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
