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
```

### 2. Set Up Environment Variables
Create a .env file in the project root and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key
```
### 3. Build and Run with Docker
Build the Docker Image:
```bash
docker build -t streamlit-pdf-qa .
```
Run the Container:
```bash
docker run -p 8501:8501 --env-file .env streamlit-pdf-qa
```
### 4. Access the Application
Open your browser and visit:

```bash
http://localhost:8501
```


## Running Locally Without Docker
If you want to run the application without Docker:

### 1.Install the required dependencies:
```bash
pip install -r requirements.txt
```
### 2.Run the application:
```bash
streamlit run app.py
```
### Troubleshooting
Container Doesn't Start
Check logs using:

```bash
docker logs <container_id>
```
### Application Not Accessible
Try using http://127.0.0.1:8501 instead of http://localhost:8501.

Error: File Does Not Exist
Make sure app.py exists in your project root before building the Docker image.

### Future Improvements
Add support for multiple file formats
Implement authentication
Enhance search with better retrieval algorithms
