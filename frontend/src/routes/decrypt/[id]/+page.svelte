<script>
    import { onMount } from "svelte";
    import { writable } from "svelte/store";

    export let data;

    let id = data?.id;
    let key = null;

    let encryptedMessage = writable(null);
    let decryptedMessage = writable(null);
    let errorMessage = writable(null);
    let isLoading = writable(true);

    // Décodage Base64 URL-safe -> Base64 classique
    function fromBase64UrlSafe(base64UrlString) {
        let base64 = base64UrlString.replace(/-/g, '+').replace(/_/g, '/');
        while (base64.length % 4) base64 += '=';
        return atob(base64);
    }

    async function fetchAndDecrypt() {
        try {
            const urlParams = new URLSearchParams(window.location.search);
            key = urlParams.get('key');

            if (!id || !key) {
                throw new Error("Données manquantes pour le déchiffrement.");
            }

            const response = await fetch(`http://127.0.0.1:8000/decrypt/${id}`);
            if (!response.ok) {
                throw new Error("Message introuvable.");
            }
            const result = await response.json();
            encryptedMessage.set(result.message);
            const iv = result.iv;

            const keyBytes = Uint8Array.from(fromBase64UrlSafe(key), c => c.charCodeAt(0));
            const ivBytes = Uint8Array.from(fromBase64UrlSafe(iv), c => c.charCodeAt(0));
            const encryptedBytes = Uint8Array.from(fromBase64UrlSafe(result.message), c => c.charCodeAt(0));

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
            decryptedMessage.set(dec.decode(decrypted));
        } catch (error) {
            console.error("Erreur lors du déchiffrement :", error);
            errorMessage.set("Une erreur est survenue lors du déchiffrement.");
        } finally {
            isLoading.set(false);
        }
    }

    onMount(fetchAndDecrypt);
</script>

<main>
    <h1>Déchiffrement du message</h1>

    {#if $isLoading}
        <p>Chargement en cours...</p>
    {:else if $decryptedMessage}
        <h2>Message déchiffré :</h2>
        <p>{$decryptedMessage}</p>
    {:else if $errorMessage}
        <p>{$errorMessage}</p>
    {/if}
</main>