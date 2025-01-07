<template>
    <div class="bg-gray-900 min-h-screen">
      <div class="container mx-auto p-4 md:p-8 max-w-4xl">
        <div class="bg-gray-800 shadow-2xl rounded-lg overflow-hidden border border-gray-700">
          <!-- Header Section -->
          <div class="bg-gray-700/50 p-8 border-b border-gray-600">
            <h1 class="text-4xl font-bold text-violet-400 mb-4">Terms of Service</h1>
            <p class="text-lg text-gray-300">
              Last updated: January 2025
            </p>
          </div>
  
          <!-- Main Content -->
          <div class="p-8 space-y-8">
            <!-- Introduction -->
            <section>
              <h2 class="text-2xl font-semibold text-violet-400 mb-4">Welcome to Scytalio</h2>
              <p class="text-gray-300 leading-relaxed">
                These Terms of Service govern your access to and use of Scytalio's software and services. By using Scytalio, you agree to be bound by these terms.
              </p>
            </section>
  
            <!-- Service Usage -->
            <section>
              <h2 class="text-2xl font-semibold text-violet-400 mb-4">Use of Service</h2>
              <div class="bg-gray-700 p-6 rounded-lg border border-gray-600">
                <h3 class="text-xl font-medium mb-3 text-violet-300">Self-Hosting Requirements</h3>
                <ul class="space-y-3">
                  <li class="flex items-start">
                    <span class="text-violet-400 mr-3">•</span>
                    <p class="text-gray-300">
                      You are responsible for providing and maintaining your own hosting infrastructure
                    </p>
                  </li>
                  <li class="flex items-start">
                    <span class="text-violet-400 mr-3">•</span>
                    <p class="text-gray-300">
                      You must ensure compliance with all applicable laws
                    </p>
                  </li>
                </ul>
              </div>
            </section>
  
            <!-- License Terms -->
            <section>
              <h2 class="text-2xl font-semibold text-violet-400 mb-4">Open Source License</h2>
              <div class="bg-gray-700/50 p-6 rounded-lg border-l-4 border-violet-400">
                <p class="text-gray-300 mb-4">
                  Scytalio is released under the MIT License, which permits you to:
                </p>
                <ul class="space-y-3">
                  <li class="flex items-start">
                    <span class="text-violet-400 mr-3">•</span>
                    <p class="text-gray-300">Use the software for commercial purposes</p>
                  </li>
                  <li class="flex items-start">
                    <span class="text-violet-400 mr-3">•</span>
                    <p class="text-gray-300">Modify and distribute the source code</p>
                  </li>
                </ul>
              </div>
            </section>
  
            <!-- Liability -->
            <section>
              <h2 class="text-2xl font-semibold text-violet-400 mb-4">Disclaimer and Limitations</h2>
              <div class="bg-gray-700/50 p-6 rounded-lg border-l-4 border-red-400">
                <h3 class="text-xl font-medium mb-3 text-red-400">Disclaimer of Warranties</h3>
                <p class="text-gray-300">
                  The software is provided "as is", without warranty of any kind, express or implied.
                </p>
              </div>
            </section>
  
            <!-- Contact Section -->
            <section class="border-t border-gray-700 pt-8">
              <h2 class="text-2xl font-semibold text-violet-400 mb-4">Contact Information</h2>
              <div class="flex flex-col sm:flex-row gap-4">
                <a 
                  href="mailto:support@scytalio.com"
                  class="inline-flex items-center justify-center px-6 py-3 rounded-md text-base font-medium text-white bg-violet-600 hover:bg-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-violet-500 focus:ring-offset-gray-800"
                >
                  Contact Support
                </a>
                <a 
                  href="https://docs.scytalio.com/terms"
                  class="inline-flex items-center justify-center px-6 py-3 border border-gray-600 rounded-md text-base font-medium text-gray-300 bg-gray-700 hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-violet-500 focus:ring-offset-gray-800"
                >
                  View Documentation
                </a>
              </div>
            </section>
          </div>
        </div>
      </div>
    </div>
  </template>