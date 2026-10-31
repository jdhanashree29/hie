<script setup>
import { ref } from 'vue'
import users from './data/users.json'
const username = ref('')
const password = ref('')
const loggedIn = ref(false)
const currentUser = ref(null)
const showError = ref(false)
const tasks = ['Learn Vue', 'Practice directives']
function login() {
  currentUser.value = users.find(
    u => u.username === username.value && u.password === password.value
  )
  loggedIn.value = !!currentUser.value
  showError.value = !loggedIn.value
}
</script>
<template>
  <div v-if="!loggedIn">
    <h2>Login</h2>
    <input v-model="username" placeholder="Username">
    <input v-model="password" type="password" placeholder="Password">
    <button @click="login">Login</button>
    <p v-show="showError">Invalid login!</p>
  </div>
  <div v-else>
    <h2>Welcome {{ currentUser.username }}</h2>
    <p v-show="currentUser.role === 'Admin'">Admin Dashboard</p>
    <p v-show="currentUser.role === 'User'">User Dashboard</p>
    <h3>Tasks</h3>
    <ul>
      <li v-for="(task, index) in tasks" :key="index">{{ task }}</li>
    </ul>
  </div>
</template>