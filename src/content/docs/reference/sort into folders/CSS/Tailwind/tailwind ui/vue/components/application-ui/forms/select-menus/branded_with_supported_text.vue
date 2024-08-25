<template>
  <Listbox as="div" v-model="selected">
    <ListboxLabel class="sr-only"> Change published status </ListboxLabel>
    <div class="relative">
      <div class="inline-flex divide-x divide-indigo-600 rounded-md shadow-sm">
        <div class="inline-flex divide-x divide-indigo-600 rounded-md shadow-sm">
          <div class="inline-flex items-center rounded-l-md border border-transparent bg-indigo-500 py-2 pl-3 pr-4 text-white shadow-sm">
            <CheckIcon class="h-5 w-5" aria-hidden="true" />
            <p class="ml-2.5 text-sm font-medium">{{ selected.title }}</p>
          </div>
          <ListboxButton class="inline-flex items-center rounded-l-none rounded-r-md bg-indigo-500 p-2 text-sm font-medium text-white hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-50">
            <span class="sr-only">Change published status</span>
            <ChevronDownIcon class="h-5 w-5 text-white" aria-hidden="true" />
          </ListboxButton>
        </div>
      </div>

      <transition leave-active-class="transition ease-in duration-100" leave-from-class="opacity-100" leave-to-class="opacity-0">
        <ListboxOptions class="absolute right-0 z-10 mt-2 w-72 origin-top-right divide-y divide-gray-200 overflow-hidden rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
          <ListboxOption as="template" v-for="option in publishingOptions" :key="option.title" :value="option" v-slot="{ active, selected }">
            <li :class="[active ? 'text-white bg-indigo-500' : 'text-gray-900', 'cursor-default select-none p-4 text-sm']">
              <div class="flex flex-col">
                <div class="flex justify-between">
                  <p :class="selected ? 'font-semibold' : 'font-normal'">{{ option.title }}</p>
                  <span v-if="selected" :class="active ? 'text-white' : 'text-indigo-500'">
                    <CheckIcon class="h-5 w-5" aria-hidden="true" />
                  </span>
                </div>
                <p :class="[active ? 'text-indigo-200' : 'text-gray-500', 'mt-2']">{{ option.description }}</p>
              </div>
            </li>
          </ListboxOption>
        </ListboxOptions>
      </transition>
    </div>
  </Listbox>
</template>

<script setup>
import { ref } from 'vue'
import { Listbox, ListboxButton, ListboxLabel, ListboxOption, ListboxOptions } from '@headlessui/vue'
import { CheckIcon, ChevronDownIcon } from '@heroicons/vue/20/solid'

const publishingOptions = [
  { title: 'Published', description: 'This job posting can be viewed by anyone who has the link.', current: true },
  { title: 'Draft', description: 'This job posting will no longer be publicly accessible.', current: false },
]

const selected = ref(publishingOptions[0])
</script>