<template>
  <button type="button" class="inline-flex items-center rounded-full border border-transparent bg-indigo-600 p-1 text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
    <PlusIconMini class="h-5 w-5" aria-hidden="true" />
  </button>
  <button type="button" class="inline-flex items-center rounded-full border border-transparent bg-indigo-600 p-1.5 text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
    <PlusIconMini class="h-5 w-5" aria-hidden="true" />
  </button>
  <button type="button" class="inline-flex items-center rounded-full border border-transparent bg-indigo-600 p-2 text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
    <PlusIconMini class="h-5 w-5" aria-hidden="true" />
  </button>
  <button type="button" class="inline-flex items-center rounded-full border border-transparent bg-indigo-600 p-2 text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
    <PlusIconOutline class="h-6 w-6" aria-hidden="true" />
  </button>
  <button type="button" class="inline-flex items-center rounded-full border border-transparent bg-indigo-600 p-3 text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
    <PlusIconOutline class="h-6 w-6" aria-hidden="true" />
  </button>
</template>

<script setup>
import { PlusIcon as PlusIconMini } from '@heroicons/vue/20/solid'
import { PlusIcon as PlusIconOutline } from '@heroicons/vue/24/outline'
</script>