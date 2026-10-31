<template>
  <div class="card">
    <h2>Counter</h2>

    <h3>Count: {{ counter.count }}</h3>
    <h3>Double Count: {{ counter.doubleCount }}</h3>

    <button @click="counter.increment()">Increment</button>
    <button @click="counter.decrement()">Decrement</button>
    <button @click="counter.reset()">Reset</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '../stores/counterStore'

const counter = useCounterStore()
</script>

<style scoped>
.card {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
}
button {
  margin: 5px;
  padding: 8px 15px;
  cursor: pointer;
}
</style>