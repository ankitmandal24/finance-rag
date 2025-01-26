
import os
import PyPDF2
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.schema import Document


# Set OpenAI API key securely
api_key = "Openai api key"
os.environ["OPENAI_API_KEY"] = api_key

# Define the directory where ChromaDB will persist data
persist_directory = "./chroma_db"

# Function to extract text from a PDF
def extract_pdf_text(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

# Function to process PDF and set up the Q&A system
def prepare_qa_system(pdf_text, chunk_size):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=200)
    chunks = text_splitter.split_text(pdf_text)

    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vector_store = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    documents = [Document(page_content=chunk, metadata={"source": f"chunk_{i}"}) for i, chunk in enumerate(chunks)]
    vector_store.add_documents(documents)
    vector_store.persist()
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4o", temperature=0.75),
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

# Streamlit UI
st.subheader("📄 PDF Question Answering System")

# Sidebar for file upload and chunk size setting
with st.sidebar:
    uploaded_file = st.file_uploader("Upload a PDF file:", type=['pdf'])
    chunk_size = st.number_input("Chunk Size:", min_value=500, max_value=10000, value=1000)
    process_file = st.button("Process File")

# Process file if uploaded
if uploaded_file and process_file:
    with st.spinner("Processing the PDF..."):
        pdf_text = extract_pdf_text(uploaded_file)
        st.session_state.qa_chain = prepare_qa_system(pdf_text, chunk_size)
        st.success("PDF processed successfully!")

# Ensure QA chain is available
if "qa_chain" not in st.session_state:
    st.warning("Please upload and process a PDF first.")
    st.stop()

# User input for questions
q = st.text_input("Ask a question about the PDF:")
if q:
    qa_chain = st.session_state.qa_chain
    with st.spinner("Retrieving answer..."):
        result = qa_chain.invoke({"query": q})
        answer = result.get("result", "No answer found.")
        st.text_area("Answer:", value=answer, height=200)

        # Display sources
        if "source_documents" in result:
            st.write("### Sources:")
            for doc in result["source_documents"]:
                st.write(f"- {doc.metadata.get('source', 'No source')}")

st.divider()

# Maintain chat history
if "history" not in st.session_state:
    st.session_state.history = ""

if q and answer:
    new_entry = f"**Q:** {q}\n**A:** {answer}\n{'-'*100}\n"
    st.session_state.history = new_entry + st.session_state.history

st.text_area("Chat History:", value=st.session_state.history, height=400, key="history")
