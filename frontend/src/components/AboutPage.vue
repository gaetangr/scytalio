<template>
  <div class="container mx-auto p-6">
    <h2 class="text-3xl font-bold mb-4">About Scytalio</h2>
    <p class="mb-4">
      Scytalio is an open-source API designed for storing and retrieving encrypted messages with
      end-to-end encryption (E2EE). The project name "Scytalio" is derived from the
      <em>scytale</em>, an ancient encryption device used by the Greeks to transmit secret messages
      securely. This project takes inspiration from that historical method to provide a modern
      platform for confidential message sharing.
    </p>
    <p class="mb-4">
      The goal of Scytalio is to facilitate secure sharing of sensitive content—such as passwords,
      private notes, or any other personal information—between users or computers. It ensures that
      only the sender and the recipient can read the content, protecting against data breaches,
      man-in-the-middle attacks, and other security risks. The project is designed to be easy to use
      and is an excellent example of building a secure system with FastAPI.
    </p>

    <h3 class="text-2xl font-semibold mt-6 mb-2">Project Goals</h3>
    <ul class="list-disc list-inside mb-4">
      <li>
        <strong>Secure Sharing</strong>: Scytalio aims to facilitate secure, private communication
        between users, enabling the sharing of sensitive data such as passwords and private notes,
        with the guarantee that only the intended recipient can decrypt the information.
      </li>
      <li>
        <strong>Avoid Data Breaches</strong>: By encrypting the content and using secure protocols,
        Scytalio ensures that even if the data is intercepted, it cannot be read by unauthorized
        parties.
      </li>
      <li>
        <strong>Open-source Contribution</strong>: This project is open for contributions. If you'd
        like to help improve Scytalio or add new features, feel free to fork the project, create an
        issue, or submit a pull request.
      </li>
      <li>
        <strong>Burn After Reading</strong>: Messages are automatically deleted after being read to
        ensure that sensitive data doesn’t linger.
      </li>
    </ul>

    <h3 class="text-2xl font-semibold mt-6 mb-2">Why Scytalio?</h3>
    <p class="mb-4">
      In today's digital age, the need for secure communication is more critical than ever. Scytalio
      provides a robust solution for anyone looking to share sensitive information securely. Whether
      you're a developer looking to integrate secure messaging into your application or an
      individual needing a reliable way to send private messages, Scytalio has you covered.
    </p>

    <h3 class="text-2xl font-semibold mt-6 mb-2">Get Involved</h3>
    <p class="mb-4">
      Scytalio is an open-source project and we welcome contributions! If you're passionate about
      security and want to help make Scytalio even better, we'd love to have you on board. Check out
      our GitHub repository to see how you can contribute.
    </p>

    <h3 class="text-2xl font-semibold mt-6 mb-2">License</h3>
    <p class="mb-4">
      This project is licensed under the MIT License - see the
      <a href="LICENSE" class="text-blue-600 hover:underline">LICENSE</a> file for details.
    </p>
  </div>
</template>

<script>
  export default {
    name: 'AboutPage',
  };
</script>

<style scoped>
  /* Ajoutez ici vos styles spécifiques si nécessaire */
</style>
