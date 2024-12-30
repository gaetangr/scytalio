<script>
    import { onMount } from "svelte";
    import { goto } from "$app/navigation";
    import { writable } from "svelte/store";

    let message = "";
    let generatedKey = null;
    let iv = null;
    let encryptedMessage = null;
    let errors = writable({});

    function toBase64UrlSafe(base64String) {
        return base64String.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
    }

    function validateForm() {
        let newErrors = {};

        if (!message) {
            newErrors.message = "Le message est requis.";
        }
        errors.set(newErrors);

        return Object.keys(newErrors).length === 0;
    }

    async function encryptMessage() {
        if (!validateForm()) {
            return;
        }

        try {
            const enc = new TextEncoder();
            const encodedMessage = enc.encode(message);

            // Générer une clé aléatoire
            const key = await window.crypto.subtle.generateKey(
                {
                    name: "AES-GCM",
                    length: 256,
                },
                true,
                ["encrypt", "decrypt"]
            );

            // Exporter la clé en Base64 URL-safe
            const exportedKey = await window.crypto.subtle.exportKey("raw", key);
            generatedKey = toBase64UrlSafe(btoa(String.fromCharCode(...new Uint8Array(exportedKey))));

            // Générer un IV aléatoire
            const ivBytes = window.crypto.getRandomValues(new Uint8Array(12));
            iv = toBase64UrlSafe(btoa(String.fromCharCode(...ivBytes)));

            // Chiffrer le message
            const encrypted = await window.crypto.subtle.encrypt(
                {
                    name: "AES-GCM",
                    iv: ivBytes,
                },
                key,
                encodedMessage
            );

            encryptedMessage = toBase64UrlSafe(btoa(String.fromCharCode(...new Uint8Array(encrypted))));

            // Envoyer le message chiffré au serveur
            const response = await fetch("http://127.0.0.1:8000/encrypt", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: encryptedMessage, iv }),
            });

            if (!response.ok) {
                throw new Error("Erreur lors de l'envoi du message chiffré.");
            }

            const result = await response.json();

            // Naviguer vers la page de déchiffrement
            const url = `/decrypt/${result.id}?key=${generatedKey}`;
            goto(url);
        } catch (error) {
            console.error("Erreur lors du chiffrement :", error);
        }
    }
</script>

<main>
    <h1>Chiffrement de messages</h1>
    <textarea bind:value={message} rows="4" cols="50" placeholder="Tapez votre message ici..."></textarea>
    {#if $errors.message}
        <p style="color: red;">{$errors.message}</p>
    {/if}
    <button on:click={encryptMessage}>Chiffrer</button>
</main>