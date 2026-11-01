<template>
    <div>
        <header>
            <h2>My Nuxt App</h2>

            <nav>
                <NuxtLink to="/">Home</NuxtLink>
                <NuxtLink to="/about">About</NuxtLink>
                <NuxtLink to="/contact">Contact</NuxtLink>
                <NuxtLink to="/items">Items</NuxtLink>
            </nav>
        </header>
        <slot/>
    
    </div>
</template>