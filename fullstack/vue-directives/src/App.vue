<script setup>
    import {ref} from 'vue'
    const role = ref('Guest')
    const username = ref('') 
    const showMessage = ref(true)
    const users = ref(['Pranay','Tanaya','Ethan','Archit'])

    function login(){
        alert('Welcome '+username.value)
    }
</script>

<template>
    <h1>Role based UI Rendering</h1>

    <h3>Enter username</h3>
    <input v-model="username" placeholder="Enter username">

    <h3>Select Role</h3>
    <select v-model="role">
        <option>Guest</option>
        <option>Student</option>
        <option>Admin</option>
    </select>

    <h3>Role Access:</h3>
    <p v-if="role == 'Admin'"> 
        Welcome Admin you have full Access
    </p> 
    <p v-else-if="role == 'Student'"> 
        Welcome Student, You can view your courses
    </p>
    <p v-else>
        Welcome Guest, You have limited Access
    </p>

    <h3>Important notice</h3>
    <p v-show="showMessage">
        This is an important Message
    </p>
    <button @click="showMessage = !showMessage">
        Toggle notice
    </button>

    <h3>UserList:</h3>
    <ul>
        <li v-for="(user,index) in users" :key="index">
            {{user}}
        </li>
    </ul>

    <h3>Login</h3>
    <button v-on:click="login">
        Login
    </button>
</template>