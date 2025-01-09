<template>
  <div class="flex flex-col min-h-screen" data-theme="night">
    <div class="navbar bg-base-100">
      <div class="flex-1">
        <a class="btn btn-ghost normal-case text-xl flex items-center gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="32" height="32">
            <g
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
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
          <li>
            <a href="https://github.com/gaetangr/scytalio/blob/main/README.md">Documentation</a>
          </li>
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
                <path
                  d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
                />
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
  </div>
  <footer class="footer footer-center p-4 bg-base-200 text-base-content">
    <div class="tooltip tooltip-top" data-tip="Total encrypted messages created">
      <div class="badge badge-lg gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
        </svg>
        <span>{{ totalLinks || '...' }} messages encrypted</span>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Layout',
  data() {
    return {
      totalLinks: 0,
      statsInterval: null
    }
  },
  async mounted() {
    await this.fetchStats();
    this.statsInterval = setInterval(this.fetchStats, 30000); // Refresh every 30s
  },
  beforeUnmount() {
    if (this.statsInterval) {
      clearInterval(this.statsInterval);
    }
  },
  methods: {
    async fetchStats() {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/stats`);
        if (response.ok) {
          const data = await response.json();
          this.totalLinks = data.total_links_generated;
        }
      } catch (error) {
        console.error('Failed to fetch stats:', error);
      }
    }
  }
};
</script>