<template>
  <div class="container">
    <h1>📊 Pinia State Management</h1>

    <div class="grid">
      <CounterComponent />
      <TodoComponent />
    </div>
  </div>
</template>

<script setup>
import CounterComponent from './components/Counter.vue'
import TodoComponent from './components/Todo.vue'
</script>

<style scoped>
.container {
  padding: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 20px;
}

@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>