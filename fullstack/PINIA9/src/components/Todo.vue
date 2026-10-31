<template>
  <div class="card">
    <h2>TODO List</h2>

    <input
      v-model="newTodo"
      placeholder="Enter a task"
    />

    <button @click="addTask">Add TODO</button>

    <ul>
      <li v-for="todo in todoStore.todos" :key="todo.id">
        <span
          @click="todoStore.toggleTodo(todo.id)"
          :class="{ completed: todo.completed }"
        >
          {{ todo.text }}
        </span>

        <button @click="todoStore.removeTodo(todo.id)">
          Delete
        </button>
      </li>
    </ul>

    <h3>Completed: {{ todoStore.completedCount }}</h3>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useTodoStore } from '../stores/todoStore'

const todoStore = useTodoStore()
const newTodo = ref('')

function addTask() {
  if (newTodo.value.trim()) {
    todoStore.addTodo(newTodo.value)
    newTodo.value = ''
  }
}
</script>

<style scoped>
.card {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
}

input {
  padding: 8px;
  margin-right: 5px;
}

button {
  padding: 8px 12px;
  margin: 5px;
  cursor: pointer;
}

li {
  margin: 12px 0;
}

.completed {
  text-decoration: line-through;
  color: gray;
  cursor: pointer;
}
</style>
