<template>
  <div class="container mx-auto p-6">
      
  
    <!-- Main Form Section - Highlighted -->
    <div class="mb-10">
    <div class="card bg-base-100 shadow-2xl">
      <div class="card-body p-8">
        <h2 class="card-title text-2xl mb-6 flex items-center gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8 text-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 13l-4-4h8l-4 4z"/>
          </svg>
          Create Encrypted Message
        </h2>
        
        <div class="space-y-6">
          <div class="form-control">
            <textarea 
              v-model="message" 
              rows="8" 
              class="textarea textarea-bordered textarea-lg font-mono text-lg leading-relaxed w-full bg-base-200 focus:border-primary transition-colors duration-200"
              placeholder="Type your secure message here..."
            ></textarea>
          </div>

          <div v-if="errorMessage" 
               class="alert alert-error shadow-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            <span>{{ errorMessage }}</span>
          </div>

          <button 
            @click="encryptMessage" 
            class="btn btn-primary btn-lg w-full text-lg gap-2 hover:shadow-lg transition-shadow duration-200">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
            Encrypt Message
          </button>
        </div>

        <!-- Encrypted Message Result -->
        <div v-if="encryptedMessage" class="mt-8 space-y-6">
          <div class="alert alert-success shadow-lg mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            <span>Message encrypted successfully!</span>
          </div>

          <div class="bg-base-200 p-6 rounded-xl">
            <h3 class="text-xl font-semibold mb-3 flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
              </svg>
              Share this secure link
            </h3>
            <div class="flex gap-2">
              <input 
                type="text" 
                v-model="encryptedLink" 
                class="input input-bordered input-lg flex-1 font-mono text-sm bg-base-100"
                readonly>
              <button 
                @click="copyToClipboard(encryptedLink)" 
                class="btn btn-secondary btn-lg">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                </svg>
                Copy
              </button>
            </div>
          </div>

          <div class="collapse collapse-plus border border-base-300 bg-base-200 rounded-box">
            <input type="checkbox" class="peer" /> 
            <div class="collapse-title text-lg font-medium flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Technical Details
            </div>
            <div class="collapse-content prose">
              <div class="space-y-3 mt-4">
                <p><strong>Key (Base64):</strong> <code class="break-all">{{ generatedKey }}</code></p>
                <p><strong>IV (Base64):</strong> <code class="break-all">{{ iv }}</code></p>
                <p><strong>Encrypted Message (Base64):</strong> <code class="break-all">{{ encryptedMessage }}</code></p>
                
                <div class="alert alert-info mt-4">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-current flex-shrink-0 w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                  <span>The encryption key is never sent to the server for maximum security.</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

    <!-- How It Works Section -->
    <div class="mb-10">
      <h2 class="text-3xl font-bold text-center mb-8">How It Works</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="card bg-base-200 shadow-xl">
          <div class="card-body items-center text-center">
            <div class="w-16 h-16 bg-primary rounded-full flex items-center justify-center mb-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
                <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
              </svg>
            </div>
            <h3 class="card-title mb-2">1. Write Message</h3>
            <p>Enter your sensitive message in the secure text field. All processing happens in your browser.</p>
          </div>
        </div>

        <div class="card bg-base-200 shadow-xl">
          <div class="card-body items-center text-center">
            <div class="w-16 h-16 bg-secondary rounded-full flex items-center justify-center mb-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
              </svg>
            </div>
            <h3 class="card-title mb-2">2. Encryption</h3>
            <p>Your message is encrypted using AES-GCM with a randomly generated key and initialization vector (IV).</p>
          </div>
        </div>

        <div class="card bg-base-200 shadow-xl">
          <div class="card-body items-center text-center">
            <div class="w-16 h-16 bg-accent rounded-full flex items-center justify-center mb-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/>
                <polyline points="16 6 12 2 8 6"/>
                <line x1="12" y1="2" x2="12" y2="15"/>
              </svg>
            </div>
            <h3 class="card-title mb-2">3. Share Link</h3>
            <p>Share the generated link. Only someone with this link can decrypt and read the message once.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Security Features -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-10">
      <div class="card bg-base-200 shadow-xl">
        <div class="card-body">
          <h3 class="card-title">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 mr-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
            </svg>
            Security Guarantees
          </h3>
          <ul class="list-disc list-inside space-y-2">
            <li>End-to-end encryption using AES-GCM 256-bit</li>
            <li>Keys never leave your browser</li>
            <li>Messages are deleted after reading</li>
            <li>No data retention</li>
          </ul>
        </div>
      </div>

      <div class="card bg-base-200 shadow-xl">
        <div class="card-body">
          <h3 class="card-title">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 mr-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="12" y1="16" x2="12" y2="12"/>
              <line x1="12" y1="8" x2="12.01" y2="8"/>
            </svg>
            Important Notes
          </h3>
          <ul class="list-disc list-inside space-y-2">
            <li>Messages can only be read once</li>
            <li>Keep your link secure</li>
            <li>Links expire after reading</li>
            <li>No message recovery possible</li>
          </ul>
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
      generatedKey: null,
      iv: null,
      encryptedMessage: null,
      encryptedLink: null,
      decryptedMessage: null,
      errorMessage: null,
      showCopyAlert: false,
    };
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

// Send encrypted message and IV to the server
const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/encrypt`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: this.encryptedMessage,
    iv: this.iv,
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

this.decryptMessage(key, ivBytes, encrypted);

} catch (error) {
console.error("Error during encryption:", error);
this.errorMessage = error.message || "An error occurred during encryption.";
}},
    
    async decryptMessage(key, ivBytes, encryptedBytes) {
      try {
        const decrypted = await window.crypto.subtle.decrypt(
          { name: "AES-GCM", iv: ivBytes },
          key,
          encryptedBytes
        );
  
        const dec = new TextDecoder();
        this.decryptedMessage = dec.decode(decrypted);
      } catch (error) {
        console.error("Error during decryption:", error);
        this.errorMessage = "An error occurred during decryption.";
      }
    },
    copyToClipboard(text) {
      navigator.clipboard.writeText(text).then(() => {
        this.showCopyAlert = true;
        setTimeout(() => {
          this.showCopyAlert = false;
        }, 3000);
      }).catch(err => {
        console.error("Failed to copy: ", err);
      });
    },
  },
};
</script>
