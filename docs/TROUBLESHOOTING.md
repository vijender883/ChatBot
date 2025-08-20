# Troubleshooting Guide

This guide helps you resolve common issues you might encounter while running the application.

## Common Issues

1.  **API Connection Error in Streamlit App**:
    - **Symptom**: The Streamlit frontend shows an error message about not being able to connect to the backend API.
    - **Solution**:
        - Ensure the FastAPI backend server is running in a separate terminal on port 8000.
        - Check your system's firewall settings to make sure they are not blocking the connection between the Streamlit app and the FastAPI server.

2.  **Pinecone Index Error**:
    - **Symptom**: Errors related to creating, connecting to, or writing to the Pinecone index.
    - **Solution**:
        - Double-check your `PINECONE_API_KEY` and `PINECONE_ENVIRONMENT` in your `.env` file.
        - Verify that the `PINECONE_INDEX_NAME` matches the index you intend to use in your Pinecone account.
        - Ensure your internet connection is stable.

3.  **Google API Error**:
    - **Symptom**: Errors related to the Google Gemini model.
    - **Solution**:
        - Verify that your `GOOGLE_API_KEY` in the `.env` file is correct and has the necessary permissions.
        - Check your Google AI Platform account for any API usage quotas or billing issues.

4.  **PDF Processing Error**:
    - **Symptom**: The application fails to process an uploaded PDF.
    - **Solution**:
        - Ensure the PDF is not password-protected or encrypted.
        - Check that the PDF file is not corrupted and can be opened by a standard PDF viewer.

## Verifying Environment Variables

A common source of errors is incorrect or missing environment variables. Make sure your `.env` file is in the project root and contains all the required variables:

-   `GOOGLE_API_KEY`: Your Google AI API key.
-   `PINECONE_API_KEY`: Your Pinecone API key.
-   `PINECONE_ENVIRONMENT`: Your Pinecone environment name.
-   `PINECONE_INDEX_NAME`: The name for your Pinecone index.

## Performance Tips

If the application is running but the quality of answers is not as expected, consider these performance tuning tips.

1.  **Chunk Size**: The size of text chunks affects the context sent to the model.
    -   **Smaller chunks** (e.g., 500-800 characters) can provide more precise, focused answers.
    -   **Larger chunks** (e.g., 1000-1500 characters) provide more context, which can be better for broader questions.
    -   Adjust `chunk_size` in `rag_service.py`.

2.  **Retrieval Count (k)**: This is the number of document chunks retrieved from the vector database to answer a question.
    -   Start with `k=4`. If answers lack detail, try increasing it to `k=5` or `k=6`.
    -   Adjust the `search_kwargs` in `rag_service.py`.

3.  **LLM Temperature**: This parameter controls the randomness of the model's output.
    -   **Lower values** (e.g., 0.1-0.3) produce more factual, deterministic responses.
    -   **Higher values** (e.g., 0.5-0.8) generate more creative or diverse responses.
    -   Adjust the `temperature` in `rag_service.py`.
