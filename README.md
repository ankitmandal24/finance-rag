# Streamlit PDF Question Answering System

This is a Streamlit-based application that allows users to upload a PDF file, process its content, and ask questions based on the extracted text. The application uses OpenAI's GPT model and ChromaDB for retrieval-based question answering.

## Features

- **Upload a PDF file and extract text**: Users can upload a PDF, and the text content is extracted for further processing.
- **Use ChromaDB to store and retrieve document chunks**: ChromaDB is used for storing document chunks and retrieving relevant pieces of text.
- **Ask questions about the PDF content**: The system uses OpenAI's GPT model to answer questions based on the uploaded PDF.
- **View sources for each answer**: Each answer will display the source document chunk it was derived from.
- **Maintains chat history**: Users can see the chat history of their questions and answers.

## Technologies Used

- **Python**
- **Streamlit** (for UI)
- **LangChain** (for document processing & retrieval)
- **OpenAI API** (for GPT-based answers)
- **ChromaDB** (for vector storage)
- **Docker** (for containerization)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/streamlit-pdf-qa.git
cd streamlit-pdf-qa

