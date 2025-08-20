# Configuration Options

You can customize the behavior of the RAG service by modifying the parameters in `rag_service.py`.

### Text Splitting
Modify the chunk size and overlap for text splitting. Smaller chunks can provide more specific context, while larger chunks retain more surrounding information.

```python
# In rag_service.py
self.text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # Adjust chunk size (number of characters)
    chunk_overlap=200,    # Adjust overlap between chunks
)
```

### Retrieval Settings
Modify the search parameters for the vector database retrieval. This controls how many matching document chunks are returned to the language model.

```python
# In rag_service.py
search_kwargs={"k": 4}  # Number of chunks to retrieve
```

### LLM Settings
Adjust the parameters for the Google Gemini language model to control its behavior.

```python
# In rag_service.py
ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.3,      # Adjust creativity (0.0 for deterministic, 1.0 for highly creative)
)
```
