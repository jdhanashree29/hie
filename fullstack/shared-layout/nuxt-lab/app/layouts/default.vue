<template>
  <div>
    <header>
      <h2>My Nuxt Site</h2>
      <nav>
        <NuxtLink to="/">Home</NuxtLink> |
        <NuxtLink to="/about">About</NuxtLink> |
        <NuxtLink to="/items">Items</NuxtLink>
      </nav>
    </header>
    <slot />
    <footer>My Nuxt Site</footer>
  </div>
</template>