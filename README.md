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

## Running the Application with Docker and Nginx

1. Ensure Docker and Docker Compose are installed on your machine.

2. Clone the repository:

    ```sh
    git clone https://github.com/gaetangr/scytalio.git
    cd scytalio
    ```

3. Create a `.env` file in the root directory and add the following lines:

    ```sh
    echo "DATABASE_URL=sqlite:///./scytalio.db" > .env
    echo "VITE_API_BASE_URL=http://localhost:8000" >> .env
    ```

4. Build and start the services using Docker Compose:

    ```sh
    docker-compose up --build
    ```

5. The frontend will be available at `http://localhost`, and the API will be available at `http://localhost/api`.

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

## Self-Hosting

Scytalio can be self-hosted, allowing you to run your own instance of the application. This is useful if you want to have full control over your data and the environment in which the application runs.

### Features

- **Self-Hosting**: Run your own instance of Scytalio on your server.
- **Network Sharing**: Share encrypted messages within your network securely.
- **Customizable**: Modify the source code to fit your specific needs.

To get started with self-hosting, follow the instructions in the "Running the Application with Docker and Nginx" section above.

## Development Environment Setup

To set up the development environment for Scytalio, follow these steps:

1. **Clone the Repository**: Start by cloning the repository to your local machine.

    ```sh
    git clone https://github.com/gaetangr/scytalio.git
    cd scytalio
    ```

2. **Create a Virtual Environment**: Create a virtual environment to isolate the project's dependencies.

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Backend Dependencies**: Install the required Python packages for the backend.

    ```sh
    pip install -r requirements.txt
    ```

4. **Install Frontend Dependencies**: Navigate to the frontend directory and install the required Node.js packages.

    ```sh
    cd frontend
    npm install
    ```

5. **Set Up Environment Variables**: Create a `.env` file in the root directory and add the necessary environment variables.

    ```sh
    echo "DATABASE_URL=sqlite:///./scytalio.db" > .env
    echo "VITE_API_BASE_URL=http://localhost:8000" >> .env
    ```

6. **Run the Application**: Start both the backend and frontend applications.

    ```sh
    # Start the backend
    uvicorn app.main:app --reload

    # In a new terminal, start the frontend
    cd frontend
    npm run serve
    ```

7. **Access the Application**: The backend API will be available at `http://127.0.0.1:8000/docs`, and the frontend will be available at `http://localhost:8080`.

## API Endpoints

Here are some examples of how to use the API endpoints:

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

### Delete a Message

To delete a message, send a DELETE request to the `/delete/{message_id}` endpoint, where `{message_id}` is the ID of the encrypted message. You will need to include the HMAC in the Authorization header.

Example using `curl`:

```sh
curl -X DELETE "http://127.0.0.1:8000/delete/{message_id}" -H "Authorization: your_hmac"
```

### Get Website Statistics

To retrieve global statistics about website usage, send a GET request to the `/stats` endpoint.

Example using `curl`:

```sh
curl -X GET "http://127.0.0.1:8000/stats"
```

## Setting Up the Development Environment

To set up the development environment for Scytalio, follow these steps:

1. **Clone the Repository**: Start by cloning the repository to your local machine.

    ```sh
    git clone https://github.com/gaetangr/scytalio.git
    cd scytalio
    ```

2. **Create a Virtual Environment**: Create a virtual environment to isolate the project's dependencies.

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Backend Dependencies**: Install the required Python packages for the backend.

    ```sh
    pip install -r requirements.txt
    ```

4. **Install Frontend Dependencies**: Navigate to the frontend directory and install the required Node.js packages.

    ```sh
    cd frontend
    npm install
    ```

5. **Set Up Environment Variables**: Create a `.env` file in the root directory and add the necessary environment variables.

    ```sh
    echo "DATABASE_URL=sqlite:///./scytalio.db" > .env
    echo "VITE_API_BASE_URL=http://localhost:8000" >> .env
    ```

6. **Run the Application**: Start both the backend and frontend applications.

    ```sh
    # Start the backend
    uvicorn app.main:app --reload

    # In a new terminal, start the frontend
    cd frontend
    npm run serve
    ```

7. **Access the Application**: The backend API will be available at `http://127.0.0.1:8000/docs`, and the frontend will be available at `http://localhost:8080`.

## API Endpoints

Here are some examples of how to use the API endpoints:

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

### Delete a Message

To delete a message, send a DELETE request to the `/delete/{message_id}` endpoint, where `{message_id}` is the ID of the encrypted message. You will need to include the HMAC in the Authorization header.

Example using `curl`:

```sh
curl -X DELETE "http://127.0.0.1:8000/delete/{message_id}" -H "Authorization: your_hmac"
```

### Get Website Statistics

To retrieve global statistics about website usage, send a GET request to the `/stats` endpoint.

Example using `curl`:

```sh
curl -X GET "http://127.0.0.1:8000/stats"
```
