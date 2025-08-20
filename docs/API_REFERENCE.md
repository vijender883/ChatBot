# API Reference

The FastAPI backend provides several endpoints to interact with the RAG service.

**Base URL**: `http://localhost:8000`

For detailed, interactive documentation, please visit the Swagger UI at [`/docs`](http://localhost:8000/docs) while the backend server is running.

## Endpoints

### `POST /upload-pdf`

Uploads and processes one or more PDF documents, extracts text, creates embeddings, and stores them in the vector database.

- **Request Body**: `multipart/form-data` with one or more files.
- **Response**:
  - `200 OK`: `{"message": "PDFs processed and indexed successfully"}`
  - `400 Bad Request`: If no files are uploaded.

### `POST /chat`

Sends a user's message to the RAG system and gets a response.

- **Request Body** (JSON):
  ```json
  {
    "message": "What is this document about?",
    "history": [
      ["user", "Previous question"],
      ["assistant", "Previous answer"]
    ]
  }
  ```
- **Response** (JSON):
  ```json
  {
    "answer": "The document is about...",
    "sources": ["source_chunk_1", "source_chunk_2"]
  }
  ```

### `GET /health`

A simple health check endpoint to verify if the server is running.

- **Response**: `{"status": "ok"}`

### `DELETE /clear-knowledge-base`

Deletes all vectors from the Pinecone index, effectively clearing all ingested document knowledge.

- **Response**: `{"message": "Knowledge base cleared successfully"}`
