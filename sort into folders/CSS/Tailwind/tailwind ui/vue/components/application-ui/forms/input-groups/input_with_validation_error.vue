<!--
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
-->
<template>
  <div>
    <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
    <div class="relative mt-1 rounded-md shadow-sm">
      <input type="email" name="email" id="email" class="block w-full rounded-md border-red-300 pr-10 text-red-900 placeholder-red-300 focus:border-red-500 focus:outline-none focus:ring-red-500 sm:text-sm" placeholder="you@example.com" value="adamwathan" aria-invalid="true" aria-describedby="email-error" />
      <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3">
        <ExclamationCircleIcon class="h-5 w-5 text-red-500" aria-hidden="true" />
      </div>
    </div>
    <p class="mt-2 text-sm text-red-600" id="email-error">Your password must be less than 4 characters.</p>
  </div>
</template>

<script setup>
import { ExclamationCircleIcon } from '@heroicons/vue/20/solid'
</script>