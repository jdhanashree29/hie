import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

// TODO 2: Complete the todo store
export const useTodoStore = defineStore('todo', () => {

  // State
  const todos = ref([])

  // Getter
  const completedCount = computed(() =>
    todos.value.filter(todo => todo.completed).length
  )

  // Action: Add TODO
  const addTodo = (text) => {
    todos.value.push({
      id: Date.now(),
      text,
      completed: false
    })
  }

  // Action: Remove TODO
  const removeTodo = (id) => {
    todos.value = todos.value.filter(todo => todo.id !== id)
  }

  // Action: Toggle TODO
  const toggleTodo = (id) => {
    const todo = todos.value.find(todo => todo.id === id)

    if (todo) {
      todo.completed = !todo.completed
    }
  }

  return {
    todos,
    completedCount,
    addTodo,
    removeTodo,
    toggleTodo
  }
})