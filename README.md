# Medical-Chatbot-Llama2

# Medical Chatbot using LLama 2 and Pinecone

A specialized medical chatbot built with Llama 2, Pinecone vector database, and LangChain, designed to provide medical information and answers based on uploaded medical documents.

## Features

- **Medical Knowledge Base**: Processes and stores medical documents for accurate responses
- **Vector Search**: Utilizes Pinecone for efficient similarity search
- **LLM Integration**: Powered by Llama 2 for natural language understanding
- **Web Interface**: Flask-based chat interface for easy interaction
- **Document Processing**: Handles PDF documents for knowledge base creation

## Tech Stack

- **LLM**: Llama 2 (7B-chat quantized model)
- **Vector Database**: Pinecone
- **Embeddings**: HuggingFace Sentence Transformers (all-MiniLM-L6-v2)
- **Framework**: LangChain
- **Web Framework**: Flask
- **PDF Processing**: PyPDF

## Prerequisites

- Python 3.8 or higher
- Pinecone API Key
- Llama 2 7B chat model (quantized version)
- Sufficient RAM for running the LLM (minimum 8GB recommended)

##Project Structure

```bash
medical-chatbot/
├── app.py
├── requirements.txt
├── model/
│   └── llama-2-7b-chat.ggmlv3.q4_1.bin
├── src/
│   ├── __init__.py
│   ├── helper.py
│   └── prompt.py
├── Data/
│   └── [your PDF files]
└── templates/
    └── chat.html
```
## Installation

1. Clone the repository:
```bash
git clone https://github.com/PrathamAhuja1/Medical-Chatbot-Llama2.git
cd medical-chatbot
python app.py
