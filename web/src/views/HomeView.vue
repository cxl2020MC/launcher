<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import type { get_all_games } from '@/interface/get_all_games';

const game = ref<null | get_all_games>(null)
fetch('http://localhost:8000/get_all_games')
  .then(response => response.json())
  .then(data => game.value = data)
</script>

<template>
  <main>
    <div class="game-list">
      <template v-if="game">
        <RouterLink :to="'/game/'+game.id" v-for="game in game.data.games" :key="game.id"
          :title="'点击进入 ' + game.display.name">
          <div class="game">
            <div class="game-info-img">
              <img class="game-info-icon-img" :src="game.display.icon.url" :art="game.biz">
              <img class="game-info-logo-img" :src="game.display.thumbnail.url" :art="game.biz">
            </div>
            <!-- <h2>{{ game.display.name }}</h2> -->
          </div>
        </RouterLink>
      </template>
    </div>
  </main>
</template>

<style scoped>
.game-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1em;
  margin: 1em;
}

.game {
  width: 20em;
  border: var(--card-border);
  border-radius: 1em;
  overflow: hidden;
  background: var(--color-card-bg);
}

.game .game-info-img {
  display: flex;
  width: 100%;
  overflow: hidden;
  position: relative;
}

.game .game-info-logo-img {
  width: 100%;
  transition: scale 0.3s ease-in-out;
  overflow: hidden;
}

.game:hover .game-info-logo-img {
  scale: 1.1;
}

.game .game-info-icon-img {
  position: absolute;
  top: 1em;
  left: 1em;
  width: 3em;
  border-radius: 0.5em;
  z-index: 1;
}

.game h2 {
  margin: 0;
}
</style>