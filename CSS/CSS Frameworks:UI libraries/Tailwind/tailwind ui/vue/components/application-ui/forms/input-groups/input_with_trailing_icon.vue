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
    <label for="account-number" class="block text-sm font-medium text-gray-700">Account number</label>
    <div class="relative mt-1 rounded-md shadow-sm">
      <input type="text" name="account-number" id="account-number" class="block w-full rounded-md border-gray-300 pr-10 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="000-00-0000" />
      <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3">
        <QuestionMarkCircleIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { QuestionMarkCircleIcon } from '@heroicons/vue/20/solid'
</script>