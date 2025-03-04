<template>
<div>
    <Toast :show="showToast" :text="toastText" :type="toastType" />

    <div class="text-center mb-12">
      <h1 class="text-4xl md:text-5xl font-bold mb-4 text-primary shine-effect">
        {{ animatedTitle }}
      </h1>
      <p class="text-lg text-base-content/80">
        {{ animatedDescription }}
      </p>
    </div>


    <!-- Main Form Section -->
    <div class="card bg-base-100 shadow-2xl">
      <div class="card-body p-6 md:p-8">
        <!-- Message Input -->
        <div class="space-y-8">
          <div class="form-control">
            <div class="flex items-center justify-between mb-4">
              <label class="text-lg font-medium flex items-center gap-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-5 h-5 text-primary"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    d="M15.5 2H8.6c-.4 0-.8.2-1.1.5-.3.3-.5.7-.5 1.1v16.8c0 .4.2.8.5 1.1.3.3.7.5 1.1.5h12.8c.4 0 .8-.2 1.1-.5.3-.3.5-.7.5-1.1V7.5L15.5 2z"
                  />
                  <path d="M15 2v6h6" />
                  <path d="M10 13h8" />
                  <path d="M10 17h8" />
                  <path d="M10 9h4" />
                </svg>
                Your Message
              </label>
              <span class="text-sm opacity-70">End-to-end encrypted</span>
            </div>
            <textarea
              v-model="message"
              rows="6"
              class="textarea textarea-bordered font-mono text-lg leading-relaxed w-full bg-base-200 focus:border-primary transition-all duration-200 resize-y min-h-[200px]"
              :class="{ 'textarea-error': errorMessage }"
              placeholder="Type your secure message here..."
            ></textarea>
          </div>

          <!-- Options -->
          <div
            class="flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between bg-base-200 p-4 rounded-lg"
          >
            <div class="flex items-center gap-3">
              <input type="checkbox" v-model="burnAfterReading" class="checkbox checkbox-primary" />
              <div class="flex items-center gap-2">
                <span class="font-medium">Burn after reading</span>
                <div
                  class="tooltip"
                  data-tip="Message will be automatically deleted after being read once"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-base-content/60"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                      clip-rule="evenodd"
                    />
                  </svg>
                </div>
              </div>
            </div>
            <button
              @click="encryptMessage"
              :disabled="!canEncrypt || isEncrypting"
              :class="{
                'btn-disabled': !canEncrypt,
                loading: isEncrypting,
              }"
              class="btn btn-primary w-full sm:w-auto gap-2 min-w-[200px]"
            >
              <svg
                v-if="!isEncrypting"
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
                />
              </svg>
              {{ isEncrypting ? 'Encrypting...' : 'Encrypt Message' }}
            </button>
          </div>

          <!-- Error Message -->
          <div v-if="errorMessage" class="alert alert-error shadow-lg animate-fadeIn">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="stroke-current flex-shrink-0 h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
            <span>{{ errorMessage }}</span>
          </div>
        </div>

        <!-- Encrypted Result -->
        <div v-if="encryptedMessage" class="mt-8 space-y-6 animate-fadeIn">
          <div class="alert alert-success shadow-lg">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="stroke-current flex-shrink-0 h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
            <div>
              <h3 class="font-bold">Success!</h3>
              <div class="text-sm">Your message has been encrypted and is ready to share.</div>
            </div>
          </div>

          <div class="bg-base-200 p-6 rounded-xl space-y-4">
            <h3 class="text-xl font-semibold flex items-center gap-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6 text-primary"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"
                />
              </svg>
              Share this secure link
            </h3>
            <div class="join w-full">
              <input
                type="text"
                v-model="encryptedLink"
                class="join-item input input-bordered flex-1 font-mono text-sm bg-base-100"
                readonly
              />
              <button @click="handleCopy(encryptedLink)" class="join-item btn btn-primary gap-2">
                <svg
                  v-if="!copyButtonClicked"
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"
                  />
                </svg>
                <svg
                  v-else
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M5 13l4 4L19 7"
                  />
                </svg>
                Copy Link
              </button>
            </div>
          </div>

          <!-- Technical Details -->
          <div
            class="collapse collapse-plus border border-base-300 bg-base-200/50 rounded-xl hover:bg-base-200 transition-colors duration-200"
          >
            <input type="checkbox" class="peer" />
            <div class="collapse-title text-lg font-medium flex items-center gap-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                />
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
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    class="stroke-current flex-shrink-0 w-6 h-6"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    ></path>
                  </svg>
                  <div>
                    <h3 class="font-bold">Zero Knowledge Encryption</h3>
                    <div class="text-sm">
                      The encryption key never leaves your browser for maximum security.
                    </div>
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
  import { v4 as uuidv4 } from 'uuid';
  import { toBase64UrlSafe, copyToClipboard } from '../utils';
  import Toast from './Toast.vue';

  export default {
    components: {
      Toast,
    },
    data() {
      return {
        originalTitle: 'Secure Message Sharing',
      originalDescription: 'End-to-end encrypted messages that disappear after reading.',
      animatedTitle: '',
      animatedDescription: '',
      characters: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()',
      showToast: false,
      toastText: '',
      toastType: '',
        message: '',
        lastEncryptedHash: null,
        burnAfterReading: true,
        generatedKey: null,
        iv: null,
        encryptedMessage: null,
        encryptedLink: null,
        errorMessage: null,
        showCopyAlert: false,
        showToast: false,
        copyButtonClicked: false,
        isEncrypting: false,
      };
    },
    computed: {
      canEncrypt() {
        return this.message.trim().length > 0;
      },
      messageHash() {
        return this.message ? btoa(this.message) : null;
      },
      isMessageAlreadyEncrypted() {
        return this.messageHash && this.messageHash === this.lastEncryptedHash;
      },
    },
    methods: {
      scrambleText(text) {
      if (!text) return '';
      return text
        .split('')
        .map(() => this.characters.charAt(Math.floor(Math.random() * this.characters.length)))
        .join('');
    },

    async animateDecryption() {
      // Initialize with original text
      this.animatedTitle = this.originalTitle;
      this.animatedDescription = this.originalDescription;

      const steps = 15;
      const stepDuration = 100;

      // Animation sequence
      for (let i = 0; i < steps; i++) {
        await new Promise(resolve => setTimeout(resolve, stepDuration));
        
        if (i === steps - 1) {
          this.animatedTitle = this.originalTitle;
          this.animatedDescription = this.originalDescription;
        } else {
          this.animatedTitle = this.scrambleText(this.originalTitle);
          this.animatedDescription = this.scrambleText(this.originalDescription);
        }
      }
    }
  ,
      async handleCopy(text) {
        try {
          await copyToClipboard(text);
          this.copyButtonClicked = true;
          this.showToast = true;
          this.toastText = 'Copied to clipboard!';
          this.toastType = 'success';
          setTimeout(() => {
            this.showToast = false;
            this.copyButtonClicked = false;
          }, 3000);
        } catch (err) {
          this.showToast = true;
          this.toastText = 'Failed to copy';
          this.toastType = 'error';
          console.error('Failed to copy:', err);
        }
      },

      validateForm() {
        if (!this.message) {
          this.errorMessage = 'Message is required.';
          return false;
        }
        this.errorMessage = null;
        return true;
      },

      async encryptMessage() {
        if (!this.canEncrypt || this.isEncrypting) return;
        if (this.isMessageAlreadyEncrypted) {
          this.showToast = true;
          this.toastText = 'Message already encrypted';
          this.toastType = 'error';
          return;
        }

        this.isEncrypting = true;
        this.errorMessage = null;
        try {
          const message_uuid = uuidv4();
          console.log('Message UUID:', message_uuid);
          const enc = new TextEncoder();
          const encodedMessage = enc.encode(this.message);

          const key = await window.crypto.subtle.generateKey(
            {
              name: 'AES-GCM',
              length: 256,
            },
            true,
            ['encrypt', 'decrypt']
          );

          const iv = window.crypto.getRandomValues(new Uint8Array(12));
          const encryptedMessage = await window.crypto.subtle.encrypt(
            {
              name: 'AES-GCM',
              iv: iv,
            },
            key,
            encodedMessage
          );

          const exportedKey = await window.crypto.subtle.exportKey('raw', key);
          const base64Key = toBase64UrlSafe(
            btoa(String.fromCharCode(...new Uint8Array(exportedKey)))
          );
          const base64Message = toBase64UrlSafe(
            btoa(String.fromCharCode(...new Uint8Array(encryptedMessage)))
          );
          const base64Iv = toBase64UrlSafe(btoa(String.fromCharCode(...iv)));

          this.generatedKey = base64Key;
          this.iv = base64Iv;
          this.encryptedMessage = base64Message;

          const hmacKey = await window.crypto.subtle.importKey(
            'raw',
            new TextEncoder().encode(this.generatedKey),
            { name: 'HMAC', hash: 'SHA-256' },
            false,
            ['sign']
          );

          const signature = await window.crypto.subtle.sign(
            'HMAC',
            hmacKey,
            new TextEncoder().encode(message_uuid)
          );
          const signatureHex = Array.from(new Uint8Array(signature))
            .map(b => b.toString(16).padStart(2, '0'))
            .join('');

          const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/encrypt`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              message: this.encryptedMessage,
              iv: this.iv,
              id: message_uuid,
              burn_after_reading: this.burnAfterReading,
              hmac: signatureHex,
            }),
          });

          if (response.status === 429) {
            throw new Error('Too many requests. Please try again later.');
          }
          if (!response.ok) {
            const contentType = response.headers.get('content-type');
            if (contentType && contentType.indexOf('application/json') !== -1) {
              const errorData = await response.json();
              throw new Error(
                errorData.detail || `Error ${response.status}: ${response.statusText}`
              );
            } else {
              throw new Error(`Error ${response.status}: ${response.statusText}`);
            }
          }

          const result = await response.json();
          const messageId = result.id;

          this.encryptedLink = `${window.location.origin}/decrypt/${messageId}?key=${this.generatedKey}`;
          this.lastEncryptedHash = this.messageHash;
        } catch (error) {
          console.error('Error during encryption:', error);
          this.errorMessage = error.message || 'An error occurred during encryption.';
        } finally {
          this.isEncrypting = false;
        }
      },
    },
    watch: {
      message() {
        if (this.encryptedMessage && !this.isMessageAlreadyEncrypted) {
          this.encryptedMessage = null;
          this.encryptedLink = null;
        }
      },

    },
    mounted() {
      this.animateDecryption()
  },
  };
</script>

<style scoped>
.shine-effect {
  transition: all 0.3s ease;
}
</style>