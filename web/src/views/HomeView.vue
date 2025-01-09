<script setup lang="ts">
import { ref } from 'vue'
import { get_all_games } from '@/interface/get_all_games';

const game = ref < null | get_all_games > (null)
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
