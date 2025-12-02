# Installation and Setup

This guide will walk you through setting up and running the FastAPI RAG Chatbot on your local machine.

## Prerequisites

Before you begin, ensure you have the following:

1. **Python 3.7+**: You can download it from [python.org](https://www.python.org/downloads/).
2. **Git**: You'll need Git to clone the repository. You can download it from [git-scm.com](https://git-scm.com/downloads).
3. **Google AI API Key**: Get your key from [Google AI Studio](https://makersuite.google.com/app/apikey).
4. **Pinecone Account**: Sign up for a free account at [Pinecone.io](https://www.pinecone.io/). You will need your API key and environment name from your Pinecone dashboard.

## Installation Steps

1. **Fork the Repository and then Clone the Repository**:
   Firstly, fork the repository from https://github.com/vijender883/ChatBot.
   
   Secondly, open your terminal or command prompt and clone the repository to your local machine using Git:

    ```bash
        git clone https://github.com/your-username/Chatbot.git
        cd Chatbot
    ```

    *(Note: If you plan to contribute, we recommend forking the repository first. See our [Contributing Guide](../CONTRIBUTING.md) for more details.)*

3. **Install Dependencies**:
    Install the required Python packages using `pip`. It's a good practice to do this in a virtual environment.

    ```bash
        # Create and activate a virtual environment (optional but recommended)
        python -m venv venv
        source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

        # Install dependencies
        pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    The application uses a `.env` file to manage secret keys. Create a file named `.env` in the root of the project directory.
    Copy the following into your `.env` file and replace the placeholders with your actual credentials:

    ```env
        # .env - Store your secret keys here
        GOOGLE_API_KEY="your_google_api_key_here"
        PINECONE_API_KEY="your_pinecone_api_key_here"
        PINECONE_INDEX_NAME="rag-chatbot-index"
    ```

## Running the Application

The application consists of two main components: a FastAPI backend and a Streamlit frontend. You need to run them in separate terminals. Make sure you are in the project's root directory and your virtual environment is activated.

### 1. Start the FastAPI Backend

In your first terminal, run the following command to start the Uvicorn server for the FastAPI backend:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

- You should see output indicating the server is running.
- The API will be available at `http://localhost:8000`.
- Interactive API documentation (Swagger UI) will be at `http://localhost:8000/docs`.

### 2. Start the Streamlit Frontend

Open a **new** terminal (leaving the first one running). In this second terminal, run the following command to start the Streamlit web application:

```bash
streamlit run streamlit_app.py
```

- Your web browser should automatically open a new tab with the application running at `http://localhost:8501`.

You are now ready to use the application! You can start uploading PDF documents and chatting with them.
