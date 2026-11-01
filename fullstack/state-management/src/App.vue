<script setup>
import { ref } from 'vue'
import { useCounterStore } from './stores/counter'
import { useTodoStore } from './stores/todo'

const counter = useCounterStore()
const todo = useTodoStore()

const task = ref('')
</script>

<template>
    <h1>Pinia State Management</h1>

    <h2>Counter</h2>

    <h3>Count: {{ counter.count }}</h3>
    <p>Double: {{ counter.doubleCount }}</p>

    <button @click="counter.increment()">Increment</button>
    <button @click="counter.decrement()">Decrement</button>

    <hr>

    <h2>Todo List</h2>

    <input v-model="task" placeholder="Enter task">

    <button @click="todo.addTodo(task); task = ''">
        Add Todo
    </button>

    <p>Total Todos: {{ todo.totalTodos }}</p>

    <ul>
        <li v-for="item in todo.todos" :key="item.id">
            <input
                type="checkbox"
                :checked="item.completed"
                @change="todo.toggleTodo(item.id)"
            >
            <span>{{ item.text }}</span>

            <button @click="todo.removeTodo(item.id)">
                Delete
            </button>
        </li>
    </ul>
</template>