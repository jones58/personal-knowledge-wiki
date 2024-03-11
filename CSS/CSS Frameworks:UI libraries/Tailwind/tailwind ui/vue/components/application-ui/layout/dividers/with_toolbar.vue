<template>
  <div class="relative">
    <div class="absolute inset-0 flex items-center" aria-hidden="true">
      <div class="w-full border-t border-gray-300" />
    </div>
    <div class="relative flex justify-center">
      <span class="isolate inline-flex -space-x-px rounded-md shadow-sm">
        <button type="button" class="relative inline-flex items-center rounded-l-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-400 hover:bg-gray-50 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500">
          <span class="sr-only">Edit</span>
          <PencilIcon class="h-5 w-5" aria-hidden="true" />
        </button>
        <button type="button" class="relative inline-flex items-center border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-400 hover:bg-gray-50 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500">
          <span class="sr-only">Attachment</span>
          <PaperClipIcon class="h-5 w-5" aria-hidden="true" />
        </button>
        <button type="button" class="relative inline-flex items-center border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-400 hover:bg-gray-50 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500">
          <span class="sr-only">Annotate</span>
          <ChatBubbleBottomCenterTextIcon class="h-5 w-5" aria-hidden="true" />
        </button>
        <button type="button" class="relative inline-flex items-center rounded-r-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-400 hover:bg-gray-50 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500">
          <span class="sr-only">Delete</span>
          <TrashIcon class="h-5 w-5" aria-hidden="true" />
        </button>
      </span>
    </div>
  </div>
</template>

<script setup>
import { ChatBubbleBottomCenterTextIcon, PaperClipIcon, PencilIcon, TrashIcon } from '@heroicons/vue/20/solid'
</script>