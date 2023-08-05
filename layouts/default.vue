<template>
    <div>
        <header class="shadow-sm bg-white">
            <nav class="container mx-auto p-4 flex justify-between">
                <NuxtLink to="/" class="font-bold">Archons</NuxtLink>
                <ul class="flex gap-4">
                    <li><NuxtLink to="/Barbatos" class="btn">Barbatos</NuxtLink></li>
                    <li><NuxtLink to="/Beezebul" class="btn">Beezebul</NuxtLink></li>                    
                    <li><NuxtLink to="/Morax" class="btn">morax</NuxtLink></li>
                    <li><NuxtLink to="/Buer" class="btn">Buer</NuxtLink></li>
                </ul>
            </nav>
        </header>

        <!-- page content go here -->
        <div class="container mx-auto p-4">
            <slot />
        </div>
    </div>
</template>

<style scoped>
    .router-link-exact-active {
        color: #12b488;
    }
</style>