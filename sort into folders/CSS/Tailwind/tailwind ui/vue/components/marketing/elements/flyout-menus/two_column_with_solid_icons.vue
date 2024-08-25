<template>
  <Popover class="relative" v-slot="{ open }">
    <PopoverButton :class="[open ? 'text-gray-900' : 'text-gray-500', 'group inline-flex items-center rounded-md bg-white text-base font-medium hover:text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2']">
      <span>Solutions</span>
      <ChevronDownIcon :class="[open ? 'text-gray-600' : 'text-gray-400', 'ml-2 h-5 w-5 transition duration-150 ease-in-out group-hover:text-gray-500']" aria-hidden="true" />
    </PopoverButton>

    <transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-1" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-1">
      <PopoverPanel class="absolute left-1/2 z-10 mt-3 w-screen max-w-md -translate-x-1/2 transform px-2 sm:px-0 lg:max-w-3xl">
        <div class="overflow-hidden rounded-lg shadow-lg ring-1 ring-black ring-opacity-5">
          <div class="relative grid gap-6 bg-white px-5 py-6 sm:gap-8 sm:p-8 lg:grid-cols-2">
            <a v-for="item in solutions" :key="item.name" :href="item.href" class="-m-3 flex items-start rounded-lg p-3 transition duration-150 ease-in-out hover:bg-gray-50">
              <div class="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-md bg-indigo-500 text-white sm:h-12 sm:w-12">
                <component :is="item.icon" class="h-6 w-6" aria-hidden="true" />
              </div>
              <div class="ml-4">
                <p class="text-base font-medium text-gray-900">{{ item.name }}</p>
                <p class="mt-1 text-sm text-gray-500">{{ item.description }}</p>
              </div>
            </a>
          </div>
          <div class="bg-gray-50 p-5 sm:p-8">
            <a href="#" class="-m-3 flow-root rounded-md p-3 transition duration-150 ease-in-out hover:bg-gray-100">
              <span class="flex items-center">
                <span class="text-base font-medium text-gray-900">Enterprise</span>
                <span class="ml-3 inline-flex items-center rounded-full bg-indigo-100 px-3 py-0.5 text-xs font-medium leading-5 text-indigo-800">New</span>
              </span>
              <span class="mt-1 block text-sm text-gray-500">Empower your entire team with even more advanced tools.</span>
            </a>
          </div>
        </div>
      </PopoverPanel>
    </transition>
  </Popover>
</template>

<script setup>
import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
import { ChevronDownIcon } from '@heroicons/vue/20/solid'
import {
  ArrowPathIcon,
  ChartBarIcon,
  CursorArrowRaysIcon,
  DocumentChartBarIcon,
  ShieldCheckIcon,
  Squares2X2Icon,
} from '@heroicons/vue/24/outline'

const solutions = [
  {
    name: 'Analytics',
    description: 'Get a better understanding of where your traffic is coming from.',
    href: '#',
    icon: ChartBarIcon,
  },
  {
    name: 'Engagement',
    description: 'Speak directly to your customers in a more meaningful way.',
    href: '#',
    icon: CursorArrowRaysIcon,
  },
  { name: 'Security', description: "Your customers' data will be safe and secure.", href: '#', icon: ShieldCheckIcon },
  {
    name: 'Integrations',
    description: "Connect with third-party tools that you're already using.",
    href: '#',
    icon: Squares2X2Icon,
  },
  {
    name: 'Automations',
    description: 'Build strategic funnels that will drive your customers to convert',
    href: '#',
    icon: ArrowPathIcon,
  },
  {
    name: 'Reports',
    description: 'Get detailed reports that will help you make more informed decisions',
    href: '#',
    icon: DocumentChartBarIcon,
  },
]
</script>