<script setup>
const route = useRoute()

const itemId = route.params.id

const items = [
  {
    id: '1',
    name: 'Laptop',
    description: 'Developer laptop'
  },
  {
    id: '2',
    name: 'Smartphone',
    description: '5G mobile phone'
  },
  {
    id: '3',
    name: 'Headphones',
    description: 'Wireless headphones'
  }
]

const item = items.find(i => i.id === itemId)
</script>

<template>
  <div v-if="item">
    <h2>{{ item.name }} (ID: {{ item.id }})</h2>
    <p>{{ item.description }}</p>
  </div>

  <div v-else>
    <h2>Item Not Found</h2>
  </div>
</template>