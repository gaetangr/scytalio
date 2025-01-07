<template>
  <div class="bg-gray-900 min-h-screen">
    <div class="container mx-auto p-4 md:p-8 max-w-4xl">
      <div class="bg-gray-800 shadow-2xl rounded-lg overflow-hidden border border-gray-700">
        <!-- Header Section -->
        <div class="bg-gray-700/50 p-8 border-b border-gray-600">
          <h1 class="text-4xl font-bold text-violet-400 mb-4">Privacy Policy</h1>
          <p class="text-lg text-gray-300">
            Last updated: January 2025
          </p>
        </div>

        <!-- Main Content -->
        <div class="p-8 space-y-8">
          <!-- Introduction -->
          <section>
            <h2 class="text-2xl font-semibold text-violet-400 mb-4">Our Commitment to Privacy</h2>
            <p class="text-gray-300 leading-relaxed">
              At Scytalio, we believe privacy is a fundamental right. Our platform is built with security and privacy at its core, providing you with complete control over your data through self-hosting capabilities.
            </p>
          </section>

          <!-- Security Features -->
          <section>
            <h2 class="text-2xl font-semibold text-violet-400 mb-4">Security Features</h2>
            <div class="grid md:grid-cols-2 gap-6">
              <div class="bg-gray-700 p-6 rounded-lg border border-gray-600">
                <h3 class="text-xl font-medium mb-3 text-violet-300">End-to-End Encryption</h3>
                <p class="text-gray-300">
                  All messages and data are protected with industry-standard end-to-end encryption. Your communications remain private and can only be accessed by intended recipients.
                </p>
              </div>
              <div class="bg-gray-700 p-6 rounded-lg border border-gray-600">
                <h3 class="text-xl font-medium mb-3 text-violet-300">Self-Hosted Infrastructure</h3>
                <p class="text-gray-300">
                  Deploy Scytalio on your own servers for complete control over your data infrastructure and security protocols.
                </p>
              </div>
            </div>
          </section>

          <!-- Data Handling -->
          <section>
            <h2 class="text-2xl font-semibold text-violet-400 mb-4">Data Handling Practices</h2>
            <ul class="space-y-4">
              <li class="flex items-start">
                <span class="text-violet-400 mr-3">•</span>
                <p class="text-gray-300">
                  <strong class="text-violet-300">No Data Collection:</strong> By default, Scytalio does not collect, store, or process any user data.
                </p>
              </li>
              <li class="flex items-start">
                <span class="text-violet-400 mr-3">•</span>
                <p class="text-gray-300">
                  <strong class="text-violet-300">Optional Features:</strong> Any data collection is strictly opt-in and configured by the host administrator.
                </p>
              </li>
            </ul>
          </section>

          <!-- Host Responsibilities -->
          <section>
            <h2 class="text-2xl font-semibold text-violet-400 mb-4">Host Responsibilities</h2>
            <div class="bg-gray-700/50 p-6 rounded-lg border-l-4 border-violet-400">
              <p class="text-gray-300 mb-4">As a self-hosted platform, hosts are responsible for:</p>
              <ul class="space-y-2">
                <li class="flex items-start">
                  <span class="text-violet-400 mr-3">•</span>
                  <p class="text-gray-300">Server security and updates</p>
                </li>
                <li class="flex items-start">
                  <span class="text-violet-400 mr-3">•</span>
                  <p class="text-gray-300">Encryption key management</p>
                </li>
              </ul>
            </div>
          </section>

          <!-- Contact Section -->
          <section class="border-t border-gray-700 pt-8">
            <h2 class="text-2xl font-semibold text-violet-400 mb-4">Contact Us</h2>
            <div class="flex flex-col sm:flex-row gap-4">
              <a 
                href="mailto:support@scytalio.com"
                class="inline-flex items-center justify-center px-6 py-3 rounded-md text-base font-medium text-white bg-violet-600 hover:bg-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-violet-500 focus:ring-offset-gray-800"
              >
                Email Support
              </a>
              <a 
                href="https://docs.scytalio.com/privacy"
                class="inline-flex items-center justify-center px-6 py-3 border border-gray-600 rounded-md text-base font-medium text-gray-300 bg-gray-700 hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-violet-500 focus:ring-offset-gray-800"
              >
                Privacy Documentation
              </a>
            </div>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>
