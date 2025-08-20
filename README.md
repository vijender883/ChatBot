# FastAPI RAG Chatbot with Streamlit

![Project Banner](https://raw.githubusercontent.com/jules-dot-ai/docs/main/images/rag_chatbot_banner.png)

A complete RAG (Retrieval-Augmented Generation) chatbot system that allows users to upload PDF documents and chat with them using Google Gemini and a Pinecone vector database.

This project is designed to be easy to set up and run, even for beginners. It features a friendly Streamlit web interface and a powerful FastAPI backend.

## ✨ Features

-   📄 **PDF Document Processing**: Upload your PDFs and the system will automatically process and index them.
-   🤖 **Conversational AI**: Chat with your documents using the power of Google Gemini.
-   🔍 **Semantic Search**: Powered by Pinecone vector database for accurate and fast retrieval.
-   💬 **Chat History**: The chatbot remembers the context of your conversation.
-   🖥️ **User-Friendly Interface**: A beautiful and intuitive web interface built with Streamlit.
-   ⚡ **Fast & Scalable Backend**: Built with FastAPI.

## 🚀 Getting Started

Welcome! To get the chatbot running on your local machine, follow these simple steps.

### 1. Prerequisites

Make sure you have the necessary API keys and software.
-   **Google AI API Key**
-   **Pinecone API Key**
-   **Python 3.7+** and **Git**

### 2. Installation

Clone the repository, install the dependencies, and set up your environment variables. For a detailed, step-by-step guide, please see our **[Installation Guide](./docs/INSTALLATION.md)**.

```bash
# Clone the repository
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot

# Install dependencies (preferably in a virtual environment)
pip install -r requirements.txt

# Create a .env file and add your API keys (see installation guide for details)
```

### 3. Run the Application

You'll need to run the backend and frontend in two separate terminals.

1.  **Start the Backend**:
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```

2.  **Start the Frontend**:
    ```bash
    streamlit run streamlit_app.py
    ```

Your application should now be running and accessible in your web browser at `http://localhost:8501`.

## 📚 Documentation

We have comprehensive documentation to help you understand, use, and customize the project.

-   **[Installation Guide](./docs/INSTALLATION.md)**: Detailed setup instructions.
-   **[Configuration Guide](./docs/CONFIGURATION.md)**: How to customize the RAG pipeline.
-   **[API Reference](./docs/API_REFERENCE.md)**: Details on the FastAPI endpoints.
-   **[Troubleshooting Guide](./docs/TROUBLESHOOTING.md)**: Solutions for common issues.

## 🤝 Contributing

We welcome contributions from the community! Whether it's fixing a bug, adding a feature, or improving documentation, your help is appreciated.

Please read our **[Contributing Guidelines](./CONTRIBUTING.md)** to learn how you can get involved.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
