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
  <div class="border-b border-gray-200 pb-5 sm:flex sm:items-center sm:justify-between">
    <h3 class="text-lg font-medium leading-6 text-gray-900">Job Postings</h3>
    <div class="mt-3 sm:mt-0 sm:ml-4">
      <label for="mobile-search-candidate" class="sr-only">Search</label>
      <label for="desktop-search-candidate" class="sr-only">Search</label>
      <div class="flex rounded-md shadow-sm">
        <div class="relative flex-grow focus-within:z-10">
          <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
            <MagnifyingGlassIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
          </div>
          <input type="text" name="mobile-search-candidate" id="mobile-search-candidate" class="block w-full rounded-none rounded-l-md border-gray-300 pl-10 focus:border-indigo-500 focus:ring-indigo-500 sm:hidden" placeholder="Search" />
          <input type="text" name="desktop-search-candidate" id="desktop-search-candidate" class="hidden w-full rounded-none rounded-l-md border-gray-300 pl-10 focus:border-indigo-500 focus:ring-indigo-500 sm:block sm:text-sm" placeholder="Search candidates" />
        </div>
        <button type="button" class="relative -ml-px inline-flex items-center rounded-r-md border border-gray-300 bg-gray-50 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500">
          <BarsArrowUpIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
          <span class="ml-2">Sort</span>
          <ChevronDownIcon class="ml-2.5 -mr-1.5 h-5 w-5 text-gray-400" aria-hidden="true" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { BarsArrowUpIcon, ChevronDownIcon, MagnifyingGlassIcon } from '@heroicons/vue/20/solid'
</script>