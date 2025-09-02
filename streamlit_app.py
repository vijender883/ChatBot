import streamlit as st
import requests
import time

# --- Configuration ---
API_URL = "http://127.0.0.1:8000"
st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="wide")

# --- Helper Functions ---


def check_api_health():
    """Checks if the backend API is running."""
    try:
        response = requests.get(f"{API_URL}/health")
        return response.status_code == 200
    except requests.ConnectionError:
        return False


# --- Main App UI ---
st.title("📄 RAG Chatbot")
st.write("Upload a PDF and ask questions about its content.")

# --- Sidebar for Knowledge Base Management ---
with st.sidebar:
    st.header("Knowledge Base")

    # PDF Uploader
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file is not None:
        with st.spinner(f"Processing `{uploaded_file.name}`..."):
            try:
                files = {"file": (uploaded_file.name,
                                  uploaded_file.getvalue(), "application/pdf")}
                response = requests.post(f"{API_URL}/upload-pdf", files=files)

                if response.status_code == 200:
                    st.success(f"✅ Successfully processed `{uploaded_file.name}`. "
                               f"Added {response.json().get('chunks', 0)} chunks to the knowledge base.")
                else:
                    st.error(
                        f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    st.divider()

    # Clear Knowledge Base Button
    if st.button("Clear Knowledge Base", type="primary"):
        with st.spinner("Clearing all documents..."):
            try:
                response = requests.delete(f"{API_URL}/clear-knowledge-base")
                if response.status_code == 200:
                    st.success("🗑️ Knowledge base cleared successfully!")
                    # Clear chat history as well
                    st.session_state.messages = []
                else:
                    st.error(
                        f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")


# --- Chat Interface ---

# Check API status before proceeding
if not check_api_health():
    st.error("🔴 Backend API is not running. Please start the FastAPI server.")
else:
    st.info("🟢 Backend is connected. You can start chatting.")

    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "sources" in message and message["sources"]:
                with st.expander("View Sources"):
                    for source in message["sources"]:
                        st.info(source)

    # Accept user input
    if prompt := st.chat_input("Ask a question about your documents..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response_content = ""

            with st.spinner("Thinking..."):
                try:
                    payload = {
                        "query": prompt,
                        "chat_history": [
                            msg for msg in st.session_state.messages if msg["role"] in ["user", "assistant"]
                        ]
                    }
                    response = requests.post(f"{API_URL}/chat", json=payload)

                    if response.status_code == 200:
                        response_data = response.json()
                        full_response_content = response_data.get(
                            "response", "Sorry, I couldn't find an answer.")
                        sources = response_data.get("sources", [])

                        message_placeholder.markdown(full_response_content)
                        if sources:
                            with st.expander("View Sources"):
                                for source in sources:
                                    st.info(source)

                        # Add assistant response and sources to chat history
                        assistant_message = {
                            "role": "assistant",
                            "content": full_response_content,
                            "sources": sources
                        }
                        st.session_state.messages.append(assistant_message)

                    else:
                        error_msg = f"Error from API: {response.status_code} - {response.text}"
                        message_placeholder.error(error_msg)
                        st.session_state.messages.append(
                            {"role": "assistant", "content": error_msg})

                except Exception as e:
                    error_msg = f"An error occurred while connecting to the API: {e}"
                    message_placeholder.error(error_msg)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": error_msg})