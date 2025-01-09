<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'
import { Icon } from "@iconify/vue";

const menu = ref('menu hidden')
const toggleMenu = () => {
  menu.value = menu.value === 'menu hidden' ? 'menu' : 'menu hidden'
}

</script>

<template>
  <header>
    <nav>
      <RouterLink to="/" id="home">
        <Icon icon="line-md:home-alt-twotone" />
      </RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
#home {
  position: fixed;
  top: 1rem;
  left: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 2rem;
  padding: 0.5rem;
  color: var(--color-text);
  border-radius: var(--btn-border-radius);
  background: var(--color-blur-bg);
  backdrop-filter: var(--blur-filter);
  z-index: 100;
}
</style>
