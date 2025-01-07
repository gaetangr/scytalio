<template>
  <div class="container mx-auto p-4 md:p-10">
    <div class="shadow-xl rounded-xl p-6 md:p-10 max-w-5xl mx-auto bg-base-100">
      <h1 class="text-4xl font-bold mb-8 text-center text-base-content">Message Decryption</h1>
      
      <div v-if="isLoading" class="flex justify-center items-center py-12">
        <div class="text-center">
          <p class="text-xl text-base-content">Loading...</p>
        </div>
      </div>
      
      <div v-else>
        <div v-if="decryptedMessage" class="space-y-6">
          <div class="bg-base-200 p-8 rounded-xl">
            <h2 class="text-2xl font-semibold mb-4 text-base-content">Decrypted Message:</h2>
            <p class="text-lg break-words text-base-content leading-relaxed min-h-[100px]">
              <a 
                v-if="isUrl(decryptedMessage)" 
                :href="decryptedMessage" 
                target="_blank" 
                class="text-primary hover:underline"
              >
                {{ decryptedMessage }}
              </a>
              <span v-else>{{ decryptedMessage }}</span>
            </p>
          </div>

          <div class="flex flex-wrap gap-4 justify-start mt-6">
            <button @click="copyToClipboard(decryptedMessage)" class="btn btn-primary">Copy Message</button>
            <button @click="downloadMessage" class="btn btn-secondary">Download as Text</button>
            <button v-if="!messageData?.burn_after_reading" @click="deleteMessage" class="btn btn-error">Delete Message</button>
          </div>
     
          <div class="alert alert-info shadow-lg mt-8">
            <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <div class="flex flex-col gap-1">
              <span class="font-medium">Security Notice</span>
              <span class="text-sm opacity-90">The decrypted message will be deleted after refreshing the page for your security.</span>
            </div>
          </div>
        </div>
        
        <div v-if="errorMessage" class="alert alert-error shadow-lg mt-6">
          <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <div class="flex flex-col gap-1">
            <span class="font-medium">Error</span>
            <span class="text-sm">{{ errorMessage }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid';

export default {
  props: ['messageId'], 
  
  data() {
    return {
      decryptedMessage: null,
      errorMessage: null,
      isLoading: true,
      key: null,
      messageData: null,
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
        const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/decrypt/${this.messageId}`);
        if (response.status === 429) {
          throw new Error("Too many requests. Please try again later.");
        }
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.detail || `Error ${response.status}: ${response.statusText}`);
        }
        const result = await response.json();
   

        this.messageData = result;
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
      } catch (error) {
        this.errorMessage = error.message || "An error occurred during decryption.";
      } finally {
        this.isLoading = false;
      }
    },

    async generateHMAC(key, uuid) {
      const cryptoKey = await crypto.subtle.importKey(
        'raw',
        new TextEncoder().encode(key),
        { name: 'HMAC', hash: 'SHA-256' },
        false,
        ['sign']
      );

      const signature = await crypto.subtle.sign(
        'HMAC',
        cryptoKey,
        new TextEncoder().encode(uuid)
      );

      return Array.from(new Uint8Array(signature))
        .map(b => b.toString(16).padStart(2, '0'))
        .join('');
    },

    async deleteMessage() {
      try {
        const uuid = this.messageId;
        const key = this.key;
        const signatureHex = await this.generateHMAC(key, uuid);

        const headers = new Headers();
        headers.append('Authorization', signatureHex);

        const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/delete/${this.messageId}`, {
          method: 'DELETE',
          headers: headers
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.detail || `Error ${response.status}: ${response.statusText}`);
        }

        this.decryptedMessage = null;
        console.log("Message deleted successfully");
        this.$router.push('/');
      } catch (error) {
        console.error("Error during deletion:", error);
        this.errorMessage = error.message || "An error occurred during deletion.";
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

    isUrl(text) {
      try {
        new URL(text);
        return true;
      } catch (_) {
        return false;
      }
    },
  },
};
</script>