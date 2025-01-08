<script setup>
import { ref } from 'vue'

const game = ref(null)
fetch('http://localhost:8000/get_all_games')
  .then(response => response.json())
  .then(data => game.value = data)
</script>

<template>
  <main>
    <div class="game-list">
      <template v-if="game">
        <div class="game" v-for="game in game.data.games" :key="game.id">
          <img :src="game.display.icon.url" alt="">
          <h2>{{ game.display.name }}</h2>
        </div>
      </template>
    </div>
  </main>
</template>
