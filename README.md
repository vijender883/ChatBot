# FastAPI RAG Chatbot with Streamlit

A complete RAG (Retrieval-Augmented Generation) chatbot system that allows users to upload PDF documents and chat with them using Google Gemini and Pinecone vector database.

## Features

- 📄 PDF document processing and indexing
- 🤖 Conversational AI with Google Gemini
- 🔍 Semantic search with Pinecone vector database
- 💬 Chat history and context awareness
- 🖥️ Beautiful Streamlit web interface
- ⚡ Fast and scalable FastAPI backend

## Prerequisites

1. **Google AI API Key**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Pinecone Account**: Sign up at [Pinecone](https://www.pinecone.io/)

## Installation

1. **Clone or create the project structure**:
```bash
mkdir rag-chatbot
cd rag-chatbot
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:
   - Copy the `.env` file and fill in your API keys:
   ```bash
   # .env
   GOOGLE_API_KEY=your_google_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   PINECONE_ENVIRONMENT=your_pinecone_environment_here
   PINECONE_INDEX_NAME=rag-chatbot-index
   ```

## Project Structure

```
rag-chatbot/
├── main.py              # FastAPI backend
├── rag_service.py       # RAG service logic
├── streamlit_app.py     # Streamlit frontend
├── requirements.txt     # Dependencies
├── .env                 # Environment variables
└── README.md           # This file
```

## Running the Application

### 1. Start the FastAPI Backend

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

### 2. Start the Streamlit Frontend

In a new terminal:

```bash
streamlit run streamlit_app.py
```

The web app will open at `http://localhost:8501`

## Usage

1. **Upload PDFs**: Use the sidebar to upload PDF documents
2. **Ask Questions**: Type questions about your documents in the chat
3. **View Sources**: See which document sections were used for answers
4. **Manage Data**: Clear knowledge base or chat history as needed

## API Endpoints

- `POST /upload-pdf` - Upload and process PDF documents
- `POST /chat` - Send chat messages to the RAG system
- `GET /health` - Health check
- `DELETE /clear-knowledge-base` - Clear all documents

## Configuration Options

### Text Splitting
Modify chunk size and overlap in `rag_service.py`:
```python
self.text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # Adjust chunk size
    chunk_overlap=200,    # Adjust overlap
)
```

### Retrieval Settings
Modify search parameters:
```python
search_kwargs={"k": 4}  # Number of chunks to retrieve
```

### LLM Settings
Adjust Gemini parameters:
```python
ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.3,      # Adjust creativity
)
```

## Troubleshooting

### Common Issues

1. **API Connection Error**:
   - Ensure FastAPI server is running on port 8000
   - Check firewall settings

2. **Pinecone Index Error**:
   - Verify API key and environment
   - Check index name spelling

3. **Google API Error**:
   - Verify API key is correct
   - Check API quotas and billing

4. **PDF Processing Error**:
   - Ensure PDF is not password protected
   - Check PDF file is not corrupted

### Environment Variables

Make sure all required environment variables are set:
- `GOOGLE_API_KEY`: Your Google AI API key
- `PINECONE_API_KEY`: Your Pinecone API key  
- `PINECONE_ENVIRONMENT`: Your Pinecone environment
- `PINECONE_INDEX_NAME`: Name for your Pinecone index

### Performance Tips

1. **Chunk Size**: Smaller chunks (500-800 tokens) for precise answers, larger chunks (1000-1500) for context
2. **Retrieval Count**: Start with k=4, increase for complex questions
3. **Temperature**: Lower (0.1-0.3) for factual, higher (0.5-0.8) for creative responses

## Development

### Adding New Features

1. **New Document Types**: Extend `process_pdf` method in `rag_service.py`
2. **Custom Prompts**: Modify the LLM chain initialization
3. **UI Improvements**: Update `streamlit_app.py`

### Testing

Test individual components:
```bash
# Test FastAPI endpoints
curl http://localhost:8000/health

# Test with sample PDF
# Use the Streamlit interface or API directly
```

## License

This project is open source and available under the MIT License.