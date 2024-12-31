<template>
    <div class="flex flex-col min-h-screen" data-theme="night">
      <div class="navbar bg-base-100">
        <div class="flex-1">
          <a class="btn btn-ghost normal-case text-xl flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
  <g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="32" cy="32" r="30" />
    <line x1="16" y1="20" x2="48" y2="20" />
    <line x1="16" y1="32" x2="48" y2="32" />
    <line x1="16" y1="44" x2="48" y2="44" />
    <path d="M24,12 Q32,4 40,12" />
    <path d="M24,52 Q32,60 40,52" />
  </g>
</svg>
<RouterLink to="/" class="font-medium">Scytalio</RouterLink>
            
          </a>
        </div>
        <div class="flex-none">
          <ul class="menu menu-horizontal px-1 items-center">
            <li><RouterLink to="/" class="font-medium">Home</RouterLink></li>
            <li><RouterLink to="/about" class="font-medium">About</RouterLink></li>
            <li><a href="https://github.com/gaetangr/scytalio/blob/main/README.md">Documentation</a></li>
            <li>
              <a 
                href="https://github.com/gaetangr/scytalio/" 
                target="_blank"
                class="font-medium flex items-center gap-2"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  class="fill-current"
                >
                  <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
                GitHub
              </a>
            </li>
          </ul>
        </div>
      </div>
  
      <main class="flex-grow container mx-auto p-4">
        <router-view></router-view>
      </main>
  
      <footer class="footer bg-base-200 text-base-content p-10">
        <aside>
          <svg
            width="50"
            height="50"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            class="fill-current"
          >
            <path
              d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 2c4.41 0 8 3.59 8 8s-3.59 8-8 8-8-3.59-8-8 3.59-8 8-8zm1 3v4h4v2h-4v4h-2v-4H7v-2h4V7h2z"
            />
          </svg>
          <p>
            Scytalio - Open Source E2EE Message Service
            <br />
            Secure messaging since 2024
          </p>
        </aside>
        <nav>
          <h6 class="footer-title">Project</h6>
          <a href="/docs" class="link link-hover">Documentation</a>
          <a href="/api" class="link link-hover">API Reference</a>
          <a href="/security" class="link link-hover">Security</a>
          <a href="/examples" class="link link-hover">Examples</a>
        </nav>
        <nav>
          <h6 class="footer-title">Community</h6>
          <a href="/about" class="link link-hover">About us</a>
          <a href="https://github.com/yourusername/scytalio" class="link link-hover">GitHub</a>
          <a href="/contribute" class="link link-hover">Contribute</a>
          <a href="/roadmap" class="link link-hover">Roadmap</a>
        </nav>
        <nav>
          <h6 class="footer-title">Legal</h6>
          <a href="/terms" class="link link-hover">Terms of use</a>
          <a href="/privacy" class="link link-hover">Privacy policy</a>
          <a href="/license" class="link link-hover">MIT License</a>
        </nav>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Layout',
  }
  </script>