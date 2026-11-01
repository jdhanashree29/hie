<script setup>
const items = ref([
    {id:'1',name:'Item 1 - Laptop'},
    {id:'2',name:'Item 2 - Mobile'},
    {id:'3',name:'Item 3 - Televison'}
])
</script>

<template>
    <div>
        <h1>Items List</h1>
    <ul>
        <li v-for="item in items" :key="item.id">
            <NuxtLink :to="`/items/${item.id}`">
                {{ item.name }}
            </NuxtLink>
        </li>
    </ul>
        
    </div>
</template>