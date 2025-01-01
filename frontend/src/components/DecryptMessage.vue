<template>
  <div class="container mx-auto p-10">
    <div class="text-center mb-6">
      <p class="text-lg text-base-content">Safely sent with Scytalio</p>
    </div>
    <div class="shadow-md rounded-lg p-8 max-w-4xl mx-auto bg-base-100">
      <h1 class="text-3xl font-bold mb-6 text-center text-base-content">Message Decryption</h1>
      
      <div v-if="isLoading" class="flex justify-center items-center">
        <div class="text-center">
          <p class="text-lg text-base-content">Loading...</p>
        </div>
      </div>
      
      <div v-else>
        <div v-if="decryptedMessage" class="bg-base-200 p-6 rounded-lg mb-4">
          <h2 class="text-xl font-semibold mb-2 text-base-content">Decrypted Message:</h2>
          <p class="break-words text-base-content">{{ decryptedMessage }}</p>
          <button 
            @click="copyToClipboard(decryptedMessage)" 
            class="btn btn-secondary mt-4">
            Copy Message
          </button>
          <button 
            @click="downloadMessage" 
            class="btn btn-secondary mt-4 ml-2">
            Download as Text
          </button>
          <div class="alert alert-info mt-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            <span>The decrypted message will be deleted after refreshing the page.</span>
          </div>
        </div>
        
        <div v-if="errorMessage" class="alert alert-error shadow-lg">
          <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          <span>{{ errorMessage }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['messageId'], 
  
  data() {
    return {
      decryptedMessage: null,
      errorMessage: null,
      isLoading: true,
      key: null,
    };
  },

  created() {
    this.key = new URLSearchParams(window.location.search).get('key');
    console.log("Extracted key from URL:", this.key);
    if (!this.key || !this.messageId) {
      this.errorMessage = "Missing data for decryption.";
      this.isLoading = false;
    } else {
      this.fetchAndDecrypt(); 
    }
  },

  methods: {
    fromBase64UrlSafe(base64UrlString) {
      let base64 = base64UrlString.replace(/-/g, '+').replace(/_/g, '/');
      while (base64.length % 4) base64 += '='; 
      return atob(base64);
    },

    async fetchAndDecrypt() {
      try {
        console.log("Fetching message with ID:", this.messageId);
        const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/decrypt/${this.messageId}`);
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.detail || `Error ${response.status}: ${response.statusText}`);
        }
        const result = await response.json();
        console.log("Fetched data:", result);

        this.encryptedMessage = result.message;
        const ivBytes = Uint8Array.from(this.fromBase64UrlSafe(result.iv), c => c.charCodeAt(0));
        const encryptedBytes = Uint8Array.from(this.fromBase64UrlSafe(result.message), c => c.charCodeAt(0));

        const keyBytes = Uint8Array.from(this.fromBase64UrlSafe(this.key), c => c.charCodeAt(0));

        const importedKey = await window.crypto.subtle.importKey(
          "raw",
          keyBytes,
          "AES-GCM",
          true,
          ["decrypt"]
        );

        const decrypted = await window.crypto.subtle.decrypt(
          { name: "AES-GCM", iv: ivBytes },
          importedKey,
          encryptedBytes
        );

        const dec = new TextDecoder();
        this.decryptedMessage = dec.decode(decrypted);
        console.log("Decrypted message:", this.decryptedMessage);
      } catch (error) {
        console.error("Error during decryption:", error);
        this.errorMessage = error.message || "An error occurred during decryption.";
      } finally {
        this.isLoading = false;
      }
    },

    copyToClipboard(text) {
      navigator.clipboard.writeText(text).then(() => {
        console.log("Message copied to clipboard!");
      }).catch(err => {
        console.error("Failed to copy: ", err);
      });
    },

    downloadMessage() {
      const blob = new Blob([this.decryptedMessage], { type: 'text/plain' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.style.display = 'none';
      a.href = url;
      a.download = 'decrypted_message.txt';
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
    },
  },
};
</script>

<style scoped>
/* Add any specific styles if necessary */
</style>