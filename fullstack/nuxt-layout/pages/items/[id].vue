<script setup>
const route = useRoute()
const itemId = route.params.id

const items = [
  { id: '1', name: 'Laptop', description: 'High performance developer laptop.' },
  { id: '2', name: 'Mobile', description: '5G mobile phone with high-res camera.' },
  { id: '3', name: 'Headphones', description: 'Wireless noise cancelling headphones.' },
  { id: '4', name: 'Smartwatch', description: 'Fitness tracker and smartwatch.' },
  { id: '5', name: 'Keyboard', description: 'Mechanical RGB gaming keyboard.' }
]

const item = computed(() => items.find(i => i.id === itemId))
</script>

<template>
  <div>
    <div v-if="item">
      <h2>{{ item.name }} (ID: {{ item.id }})</h2>
      <p>{{ item.description }}</p>
    </div>

    <div v-else>
      <h2>Item Not Found</h2>
      <p>No item found with ID: {{ itemId }}</p>
    </div>
  </div>
</template>