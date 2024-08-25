<template>
  <!--
    This example requires updating your template:

    ```
    <html class="h-full bg-gray-50">
    <body class="h-full overflow-hidden">
    ```
  -->
  <div class="flex h-full">
    <TransitionRoot as="template" :show="mobileMenuOpen">
      <Dialog as="div" class="relative z-40 lg:hidden" @close="mobileMenuOpen = false">
        <TransitionChild as="template" enter="transition-opacity ease-linear duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="transition-opacity ease-linear duration-300" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-600 bg-opacity-75" />
        </TransitionChild>

        <div class="fixed inset-0 z-40 flex">
          <TransitionChild as="template" enter="transition ease-in-out duration-300 transform" enter-from="-translate-x-full" enter-to="translate-x-0" leave="transition ease-in-out duration-300 transform" leave-from="translate-x-0" leave-to="-translate-x-full">
            <DialogPanel class="relative flex w-full max-w-xs flex-1 flex-col bg-white focus:outline-none">
              <TransitionChild as="template" enter="ease-in-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in-out duration-300" leave-from="opacity-100" leave-to="opacity-0">
                <div class="absolute top-0 right-0 -mr-12 pt-4">
                  <button type="button" class="ml-1 flex h-10 w-10 items-center justify-center rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" @click="mobileMenuOpen = false">
                    <span class="sr-only">Close sidebar</span>
                    <XMarkIcon class="h-6 w-6 text-white" aria-hidden="true" />
                  </button>
                </div>
              </TransitionChild>
              <div class="pt-5 pb-4">
                <div class="flex flex-shrink-0 items-center px-4">
                  <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company" />
                </div>
                <nav aria-label="Sidebar" class="mt-5">
                  <div class="space-y-1 px-2">
                    <a v-for="item in navigation" :key="item.name" :href="item.href" class="group flex items-center rounded-md p-2 text-base font-medium text-gray-600 hover:bg-gray-50 hover:text-gray-900">
                      <component :is="item.icon" class="mr-4 h-6 w-6 text-gray-400 group-hover:text-gray-500" aria-hidden="true" />
                      {{ item.name }}
                    </a>
                  </div>
                </nav>
              </div>
              <div class="flex flex-shrink-0 border-t border-gray-200 p-4">
                <a href="#" class="group block flex-shrink-0">
                  <div class="flex items-center">
                    <div>
                      <img class="inline-block h-10 w-10 rounded-full" :src="user.imageUrl" alt="" />
                    </div>
                    <div class="ml-3">
                      <p class="text-base font-medium text-gray-700 group-hover:text-gray-900">{{ user.name }}</p>
                      <p class="text-sm font-medium text-gray-500 group-hover:text-gray-700">Account Settings</p>
                    </div>
                  </div>
                </a>
              </div>
            </DialogPanel>
          </TransitionChild>
          <div class="w-14 flex-shrink-0" aria-hidden="true">
            <!-- Force sidebar to shrink to fit close icon -->
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <!-- Static sidebar for desktop -->
    <div class="hidden lg:flex lg:flex-shrink-0">
      <div class="flex w-20 flex-col">
        <div class="flex min-h-0 flex-1 flex-col overflow-y-auto bg-indigo-600">
          <div class="flex-1">
            <div class="flex items-center justify-center bg-indigo-700 py-4">
              <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=white" alt="Your Company" />
            </div>
            <nav aria-label="Sidebar" class="flex flex-col items-center space-y-3 py-6">
              <a v-for="item in navigation" :key="item.name" :href="item.href" class="flex items-center rounded-lg p-4 text-indigo-200 hover:bg-indigo-700">
                <component :is="item.icon" class="h-6 w-6" aria-hidden="true" />
                <span class="sr-only">{{ item.name }}</span>
              </a>
            </nav>
          </div>
          <div class="flex flex-shrink-0 pb-5">
            <a href="#" class="w-full flex-shrink-0">
              <img class="mx-auto block h-10 w-10 rounded-full" :src="user.imageUrl" alt="" />
              <div class="sr-only">
                <p>{{ user.name }}</p>
                <p>Account settings</p>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>

    <div class="flex min-w-0 flex-1 flex-col overflow-hidden">
      <!-- Mobile top navigation -->
      <div class="lg:hidden">
        <div class="flex items-center justify-between bg-indigo-600 py-2 px-4 sm:px-6 lg:px-8">
          <div>
            <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=white" alt="Your Company" />
          </div>
          <div>
            <button type="button" class="-mr-3 inline-flex h-12 w-12 items-center justify-center rounded-md bg-indigo-600 text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" @click="mobileMenuOpen = true">
              <span class="sr-only">Open sidebar</span>
              <Bars3Icon class="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
        </div>
      </div>

      <main class="flex flex-1 overflow-hidden">
        <!-- Primary column -->
        <section aria-labelledby="primary-heading" class="flex h-full min-w-0 flex-1 flex-col overflow-y-auto lg:order-last">
          <h1 id="primary-heading" class="sr-only">Account</h1>
          <!-- Your content -->
        </section>

        <!-- Secondary column (hidden on smaller screens) -->
        <aside class="hidden lg:order-first lg:block lg:flex-shrink-0">
          <div class="relative flex h-full w-96 flex-col overflow-y-auto border-r border-gray-200 bg-white">
            <!-- Your content -->
          </div>
        </aside>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue'
import {
  Bars3Icon,
  BookmarkSquareIcon,
  FireIcon,
  HomeIcon,
  InboxIcon,
  UserIcon,
  XMarkIcon,
} from '@heroicons/vue/24/outline'

const user = {
  name: 'Emily Selman',
  email: 'emily.selman@example.com',
  imageUrl:
    'https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
}
const navigation = [
  { name: 'Home', href: '#', icon: HomeIcon },
  { name: 'Trending', href: '#', icon: FireIcon },
  { name: 'Bookmarks', href: '#', icon: BookmarkSquareIcon },
  { name: 'Messages', href: '#', icon: InboxIcon },
  { name: 'Profile', href: '#', icon: UserIcon },
]

const mobileMenuOpen = ref(false)
</script>