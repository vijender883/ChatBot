import os
from typing import List, Tuple, Optional
from dotenv import load_dotenv

# LangChain imports
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import Document

# PDF processing
from pypdf import PdfReader

# Pinecone
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

class RAGService:
    def __init__(self):
        self.embeddings = None
        self.vectorstore = None
        self.llm = None
        self.retrieval_chain = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        
    async def initialize(self):
        """Initialize all components"""
        # Initialize embeddings
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        
        # Initialize LLM
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.3,
            convert_system_message_to_human=True
        )
        
        # Initialize Pinecone
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        
        index_name = os.getenv("PINECONE_INDEX_NAME", "rag-chatbot-index")
        
        # Check if index exists, create if not
        existing_indexes = [index.name for index in pc.list_indexes()]
        
        if index_name not in existing_indexes:
            pc.create_index(
                name=index_name,
                dimension=768,  # Dimension for Google's embedding-001 model
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )
        
        # Initialize vector store
        self.vectorstore = PineconeVectorStore(
            index_name=index_name,
            embedding=self.embeddings,
            pinecone_api_key=os.getenv("PINECONE_API_KEY")
        )
        
        # Initialize retrieval chain
        self.retrieval_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 4}
            ),
            return_source_documents=True,
            verbose=True
        )
    
    async def process_pdf(self, file_path: str, filename: str) -> int:
        """Process PDF and add to vector store"""
        try:
            # Read PDF
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            # Split text into chunks
            chunks = self.text_splitter.split_text(text)
            
            # Create documents with metadata
            documents = []
            for i, chunk in enumerate(chunks):
                doc = Document(
                    page_content=chunk,
                    metadata={
                        "source": filename,
                        "chunk": i,
                        "total_chunks": len(chunks)
                    }
                )
                documents.append(doc)
            
            # Add documents to vector store
            self.vectorstore.add_documents(documents)
            
            return len(documents)
            
        except Exception as e:
            raise Exception(f"Error processing PDF: {str(e)}")
    
    async def query(self, query: str, chat_history: List[dict] = None) -> Tuple[str, List[str]]:
        """Query the RAG system"""
        try:
            # Convert chat history to the expected format
            formatted_history = []
            if chat_history:
                for item in chat_history:
                    if item.get("role") == "user":
                        formatted_history.append(("human", item.get("content", "")))
                    elif item.get("role") == "assistant":
                        formatted_history.append(("ai", item.get("content", "")))
            
            # Query the retrieval chain
            result = self.retrieval_chain({
                "question": query,
                "chat_history": formatted_history
            })
            
            # Extract sources
            sources = []
            if "source_documents" in result:
                for doc in result["source_documents"]:
                    source = doc.metadata.get("source", "Unknown")
                    chunk = doc.metadata.get("chunk", 0)
                    sources.append(f"{source} (chunk {chunk + 1})")
            
            return result["answer"], sources
            
        except Exception as e:
            raise Exception(f"Error querying RAG system: {str(e)}")
    
    async def clear_knowledge_base(self):
        """Clear all documents from the vector store"""
        try:
            # Get all document IDs and delete them
            # Note: This is a simplified approach. For production, you might want
            # to implement a more sophisticated cleanup mechanism
            index_name = os.getenv("PINECONE_INDEX_NAME", "rag-chatbot-index")
            pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
            index = pc.Index(index_name)
            
            # Delete all vectors (this will clear the entire index)
            index.delete(delete_all=True)
            
        except Exception as e:
            raise Exception(f"Error clearing knowledge base: {str(e)}")