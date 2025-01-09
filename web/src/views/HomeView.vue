<script setup lang="ts">
import { ref } from 'vue'
import { useRoute,RouterLink } from 'vue-router'
import type { get_all_games } from '@/interface/get_all_games';

const route = useRoute()
let api_host = 'localhost:8000'
if (route.params.api_host) {
  api_host = api_host = Array.isArray(route.params.api_host) ? route.params.api_host[0] : route.params.api_host
}

const game_list = ref<{ area: string, data: get_all_games }[]>([])
async function get_All_Game(area: string = '国服') {
  const res = await fetch(`http://${api_host}/get_all_games?area=${area}`)
  const data = await res.json() as get_all_games
  game_list.value.push({ area: area, data: data })
}
get_All_Game()
get_All_Game("国际服")
</script>

<template>
  <main>
    <h1>游戏列表</h1>
    <template v-for="games in game_list" :key="games.area">
      <h2>{{ games.area }}</h2>
      <div class="game-list">
        <RouterLink :to="'/game/' + game.id" v-for="game in games.data.data.games" :key="game.id"
          :title="'点击进入 ' + game.display.name">
          <div class="game">
            <div class="game-info-img">
              <img class="game-info-icon-img" :src="game.display.icon.url" :art="game.biz">
              <img class="game-info-logo-img" :src="game.display.thumbnail.url" :art="game.biz">
            </div>
            <!-- <h2>{{ game.display.name }}</h2> -->
          </div>
        </RouterLink>
      </div>
    </template>

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