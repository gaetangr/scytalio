<template>
    <div>
      <h1>Déchiffrement du message</h1>
      <div v-if="isLoading">
        <p>Chargement en cours...</p>
      </div>
      <div v-else>
        <div v-if="decryptedMessage">
          <h2>Message déchiffré :</h2>
          <p>{{ decryptedMessage }}</p>
        </div>
        <div v-if="errorMessage" style="color: red;">
          <p>{{ errorMessage }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['key', 'messageId'], 
  
    data() {
      return {
        decryptedMessage: null,
        errorMessage: null,
        isLoading: true,
      };
    },
  
    created() {
      if (!this.key || !this.messageId) {
        this.errorMessage = "Données manquantes pour le déchiffrement.";
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
          const response = await fetch(`http://127.0.0.1:8000/decrypt/${this.messageId}`);
          if (!response.ok) {
            throw new Error("Message introuvable.");
          }
          const result = await response.json();
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
        } catch (error) {
          console.error("Erreur lors du déchiffrement :", error);
          this.errorMessage = "Une erreur est survenue lors du déchiffrement.";
        } finally {
          this.isLoading = false;
        }
      },
    },
  };
  </script>
  
