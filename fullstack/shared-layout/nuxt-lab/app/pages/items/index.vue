<script setup>
const items = [
  { id: '1', name: 'Laptop' },
  { id: '2', name: 'Smartphone' },
  { id: '3', name: 'Headphones' }
]
</script>

<template>
  <div>
    <h1>Items List</h1>

    <ul>
      <li v-for="item in items" :key="item.id">
        <NuxtLink :to="'/items/' + item.id">
          {{ item.name }}
        </NuxtLink>
      </li>
    </ul>
  </div>
</template>