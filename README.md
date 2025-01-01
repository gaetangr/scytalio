# Scytalio - Securely send, safely receive.

Scytalio is an open-source API designed for storing and retrieving encrypted messages with end-to-end encryption (E2EE). The project name "Scytalio" is derived from the *scytale*, an ancient encryption device used by the Greeks to transmit secret messages securely. This project takes inspiration from that historical method to provide a modern platform for confidential message sharing. 

The goal of Scytalio is to facilitate secure sharing of sensitive content—such as passwords, private notes, or any other personal information—between users or computers. It ensures that only the sender and the recipient can read the content, protecting against data breaches, man-in-the-middle attacks, and other security risks. The project is designed to be easy to use and is an excellent example of building a secure system with FastAPI.

## Project Goals

- **Secure Sharing**: Scytalio aims to facilitate secure, private communication between users, enabling the sharing of sensitive data such as passwords and private notes, with the guarantee that only the intended recipient can decrypt the information.
- **Avoid Data Breaches**: By encrypting the content and using secure protocols, Scytalio ensures that even if the data is intercepted, it cannot be read by unauthorized parties.
- **Open-source Contribution**: This project is open for contributions. If you'd like to help improve Scytalio or add new features, feel free to fork the project, create an issue, or submit a pull request.
- **Burn After Reading**: Messages are automatically deleted after being read to ensure that sensitive data doesn’t linger.

## Installation

### Backend

1. Clone the repository:

    ```sh
    git clone https://github.com/gaetangr/scytalio.git
    cd scytalio
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Frontend

1. Navigate to the frontend directory:

    ```sh
    cd frontend
    ```

2. Install the dependencies:

    ```sh
    npm install
    ```

3. Create a `.env` file in the root of the frontend directory and add the following line:

    ```sh
    echo "VITE_API_BASE_URL=http://127.0.0.1:8000" > .env
    ```

## Running the Application

### Backend

1. Start the FastAPI application:

    ```sh
    uvicorn app.main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000/docs`.

### Frontend

1. Start the Vue.js application:

    ```sh
    npm run serve
    ```

2. The frontend will be available at `http://localhost:8080`.

## Running the Application with Docker

### Prerequisites

- Docker installed on your system
- Docker Compose installed on your system

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/gaetangr/scytalio.git
    cd scytalio
    ```

2. Build and start the services:

    ```sh
    docker-compose up --build
    ```

3. The backend API will be available at `http://127.0.0.1:8000/docs` and the frontend will be available at `http://localhost:3000`.

## Running Tests

### Backend

1. Run the tests:
    ```sh
    pytest app/tests
    ```

### Frontend

1. Run the tests:
    ```sh
    npm run test
    ```

## API Usage

### Encrypt a Message

To encrypt a message, send a POST request to the `/encrypt` endpoint with the following JSON payload:

```json
{
  "message": "your_base64_encoded_message",
  "iv": "your_initialization_vector"
}
```

Example using `curl`:

```sh
curl -X POST "http://127.0.0.1:8000/encrypt" -H "Content-Type: application/json" -d '{"message": "dGVzdCBtZXNzYWdl", "iv": "dGVzdF9pdg=="}'
```

### Decrypt a Message

To decrypt a message, send a GET request to the `/decrypt/{message_id}` endpoint, where `{message_id}` is the ID of the encrypted message.

Example using `curl`:

```sh
curl -X GET "http://127.0.0.1:8000/decrypt/{message_id}"
```

## Self-Hosting in CasaOS or Any Other OS Using Docker

### Prerequisites

- Docker installed on your system
- Docker Compose installed on your system

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/gaetangr/scytalio.git
    cd scytalio
    ```

2. Build and start the services:

    ```sh
    docker-compose up --build
    ```

3. The backend API will be available at `http://127.0.0.1:8000/docs` and the frontend will be available at `http://localhost:3000`.

## Contributing

Scytalio is an open-source project and we welcome contributions! To get started, fork the repository and submit a pull request. Whether you want to fix bugs, improve features, or add new ones, your help is appreciated.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](http://_vscodecontentref_/1) file for details.
