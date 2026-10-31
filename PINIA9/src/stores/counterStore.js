import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

// TODO 1: Complete the counter store
export const useCounterStore = defineStore('counter', () => {

  // State
  const count = ref(0)

  // Getter
  const doubleCount = computed(() => count.value * 2)

  // Action
  const increment = () => {
    count.value++
  }

  // Action
  const decrement = () => {
    count.value--
  }

  // Action
  const reset = () => {
    count.value = 0
  }

  return {
    count,
    doubleCount,
    increment,
    decrement,
    reset
  }
})