<template>
  <div class="flex min-h-0 flex-1 flex-col bg-indigo-700">
    <div class="flex flex-1 flex-col overflow-y-auto pt-5 pb-4">
      <div class="flex flex-shrink-0 items-center px-4">
        <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=300" alt="Your Company" />
      </div>
      <nav class="mt-5 flex-1 space-y-1 px-2" aria-label="Sidebar">
        <a v-for="item in navigation" :key="item.name" :href="item.href" :class="[item.current ? 'bg-indigo-800 text-white' : 'text-indigo-100 hover:bg-indigo-600 hover:bg-opacity-75', 'group flex items-center px-2 py-2 text-sm font-medium rounded-md']">
          <component :is="item.icon" class="mr-3 h-6 w-6 flex-shrink-0 text-indigo-300" aria-hidden="true" />
          <span class="flex-1">{{ item.name }}</span>
          <span v-if="item.count" :class="[item.current ? 'bg-indigo-600' : 'bg-indigo-800', 'ml-3 inline-block py-0.5 px-3 text-xs font-medium rounded-full']">{{ item.count }}</span>
        </a>
      </nav>
    </div>
    <div class="flex flex-shrink-0 border-t border-indigo-800 p-4">
      <a href="#" class="group block w-full flex-shrink-0">
        <div class="flex items-center">
          <div>
            <img class="inline-block h-9 w-9 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
          </div>
          <div class="ml-3">
            <p class="text-sm font-medium text-white">Tom Cook</p>
            <p class="text-xs font-medium text-indigo-200 group-hover:text-white">View profile</p>
          </div>
        </div>
      </a>
    </div>
  </div>
</template>

<script setup>
import { CalendarIcon, ChartBarIcon, FolderIcon, HomeIcon, InboxIcon, UsersIcon } from '@heroicons/vue/24/outline'

const navigation = [
  { name: 'Dashboard', icon: HomeIcon, href: '#', current: true },
  { name: 'Team', icon: UsersIcon, href: '#', count: 3, current: false },
  { name: 'Projects', icon: FolderIcon, href: '#', count: 4, current: false },
  { name: 'Calendar', icon: CalendarIcon, href: '#', current: false },
  { name: 'Documents', icon: InboxIcon, href: '#', count: 12, current: false },
  { name: 'Reports', icon: ChartBarIcon, href: '#', current: false },
]
</script>