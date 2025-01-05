<template>
  <div class="container mx-auto p-4 md:p-8 lg:p-12 max-w-4xl">
    <!-- Hero Section -->
    <div class="text-center mb-12">
      <h1 class="text-4xl md:text-5xl font-bold mb-4 text-primary">Secure Message Sharing</h1>
      <p class="text-lg text-base-content/80">End-to-end encrypted messages that disappear after reading.</p>
    </div>

    <!-- Main Form Section -->
    <div class="card bg-base-100 shadow-2xl">
      <div class="card-body p-6 md:p-8">
        <!-- Message Input -->
        <div class="space-y-8">
          <div class="form-control">
            <div class="flex items-center justify-between mb-4">
              <label class="text-lg font-medium flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M15.5 2H8.6c-.4 0-.8.2-1.1.5-.3.3-.5.7-.5 1.1v16.8c0 .4.2.8.5 1.1.3.3.7.5 1.1.5h12.8c.4 0 .8-.2 1.1-.5.3-.3.5-.7.5-1.1V7.5L15.5 2z"/>
                  <path d="M15 2v6h6"/>
                  <path d="M10 13h8"/>
                  <path d="M10 17h8"/>
                  <path d="M10 9h4"/>
                </svg>
                Your Message
              </label>
              <span class="text-sm opacity-70">End-to-end encrypted</span>
            </div>
            <textarea 
              v-model="message" 
              rows="6"
              class="textarea textarea-bordered font-mono text-lg leading-relaxed w-full bg-base-200 focus:border-primary transition-all duration-200 resize-y min-h-[200px]"
              :class="{'textarea-error': errorMessage}"
              placeholder="Type your secure message here..."
            ></textarea>
          </div>

          <!-- Options -->
          <div class="flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between bg-base-200 p-4 rounded-lg">
            <div class="flex items-center gap-3">
              <input
                type="checkbox"
                v-model="burnAfterReading"
                class="checkbox checkbox-primary"
              />
              <div class="flex items-center gap-2">
                <span class="font-medium">Burn after reading</span>
                <div class="tooltip" data-tip="Message will be automatically deleted after being read once">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-base-content/60" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
                  </svg>
                </div>
              </div>
            </div>
            <button 
              @click="encryptMessage" 
              class="btn btn-primary w-full sm:w-auto gap-2 min-w-[200px]">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
              Encrypt Message
            </button>
          </div>

          <!-- Error Message -->
          <div v-if="errorMessage" 
               class="alert alert-error shadow-lg animate-fadeIn">
            <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>{{ errorMessage }}</span>
          </div>
        </div>

        <!-- Encrypted Result -->
        <div v-if="encryptedMessage" 
             class="mt-8 space-y-6 animate-fadeIn">
          <div class="alert alert-success shadow-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <div>
              <h3 class="font-bold">Success!</h3>
              <div class="text-sm">Your message has been encrypted and is ready to share.</div>
            </div>
          </div>

          <div class="bg-base-200 p-6 rounded-xl space-y-4">
            <h3 class="text-xl font-semibold flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
              </svg>
              Share this secure link
            </h3>
            <div class="join w-full">
              <input 
                type="text" 
                v-model="encryptedLink" 
                class="join-item input input-bordered flex-1 font-mono text-sm bg-base-100"
                readonly
              >
              <button 
                @click="copyToClipboard(encryptedLink)" 
                class="join-item btn btn-primary gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                </svg>
                Copy Link
              </button>
            </div>
          </div>

          <!-- Technical Details -->
          <div class="collapse collapse-plus border border-base-300 bg-base-200/50 rounded-xl hover:bg-base-200 transition-colors duration-200">
            <input type="checkbox" class="peer" /> 
            <div class="collapse-title text-lg font-medium flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Technical Details
            </div>
            <div class="collapse-content prose">
              <div class="space-y-4 mt-4">
                <div class="bg-base-100 p-4 rounded-lg">
                  <p class="font-semibold text-sm mb-1">Key (Base64)</p>
                  <code class="break-all text-xs">{{ generatedKey }}</code>
                </div>
                <div class="bg-base-100 p-4 rounded-lg">
                  <p class="font-semibold text-sm mb-1">IV (Base64)</p>
                  <code class="break-all text-xs">{{ iv }}</code>
                </div>
                <div class="bg-base-100 p-4 rounded-lg">
                  <p class="font-semibold text-sm mb-1">Encrypted Message (Base64)</p>
                  <code class="break-all text-xs">{{ encryptedMessage }}</code>
                </div>
                
                <div class="alert alert-info mt-6 shadow-lg">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-current flex-shrink-0 w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                  <div>
                    <h3 class="font-bold">Zero Knowledge Encryption</h3>
                    <div class="text-sm">The encryption key never leaves your browser for maximum security.</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      message: '',
      burnAfterReading: true,
      generatedKey: null,
      iv: null,
      encryptedMessage: null,
      encryptedLink: null,
      decryptedMessage: null,
      errorMessage: null,
      showCopyAlert: false,
    }
  },
  methods: {
    toBase64UrlSafe(base64String) {
      return base64String.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
    },
    
    validateForm() {
      if (!this.message) {
        this.errorMessage = "Message is required.";
        return false;
      }
      this.errorMessage = null;
      return true;
    },
    
    async encryptMessage() {
      if (!this.validateForm()) {
        return;
      }
  
      try {
        const enc = new TextEncoder();
        const encodedMessage = enc.encode(this.message);

        const key = await window.crypto.subtle.generateKey(
          {
            name: "AES-GCM",
            length: 256,
          },
          true,
          ["encrypt", "decrypt"]
        );

        const exportedKey = await window.crypto.subtle.exportKey("raw", key);
        this.generatedKey = this.toBase64UrlSafe(btoa(String.fromCharCode(...new Uint8Array(exportedKey))));

        const ivBytes = window.crypto.getRandomValues(new Uint8Array(12)); 
        this.iv = this.toBase64UrlSafe(btoa(String.fromCharCode(...ivBytes)));

        const encrypted = await window.crypto.subtle.encrypt(
          {
            name: "AES-GCM",
            iv: ivBytes,
          },
          key,
          encodedMessage
        );

        this.encryptedMessage = this.toBase64UrlSafe(btoa(String.fromCharCode(...new Uint8Array(encrypted))));

        const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/encrypt`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            message: this.encryptedMessage,
            iv: this.iv,
            burn_after_reading: this.burnAfterReading
          }),
        });

        if (response.status === 429) {
          throw new Error("Too many requests. Please try again later.");
        }
        if (!response.ok) {
          const contentType = response.headers.get("content-type");
          if (contentType && contentType.indexOf("application/json") !== -1) {
            const errorData = await response.json();
            throw new Error(errorData.detail || `Error ${response.status}: ${response.statusText}`);
          } else {
            throw new Error(`Error ${response.status}: ${response.statusText}`);
          }
        }

        const result = await response.json();
        const messageId = result.id;

        this.encryptedLink = `${window.location.origin}/decrypt/${messageId}?key=${this.generatedKey}`;
      } catch (error) {
        console.error("Error during encryption:", error);
        this.errorMessage = error.message || "An error occurred during encryption.";
      }
    },
    
    async copyToClipboard(text) {
      try {
        await navigator.clipboard.writeText(text);
        this.showCopyAlert = true;
        setTimeout(() => {
          this.showCopyAlert = false;
        }, 3000);
      } catch (err) {
        console.error("Failed to copy: ", err);
      }
    },
  },
}
</script>