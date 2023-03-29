# Document Query System

This Python script allows users to query information from a given PDF document. The system first reads and processes the document, then embeds the text using OpenAI Embeddings, and finally saves the embeddings as a pickle file. Users can continuously query the document until they choose to exit.

## Features

- Read and process PDF documents
- Embed text using OpenAI Embeddings
- Save and load embeddings as a pickle file
- Query the document using natural language queries
- Obtain relevant information based on the document content

## Installation

Before running the script, ensure you have the necessary libraries installed. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Environment Setup

Using Document Query System will usually require integrations with one or more model providers, data stores, apis, etc.

We will then need to set the environment variable in the terminal.

```bash
export OPENAI_API_KEY="..."
```

## Usage
Run the python file as follow:
```bash
python query_pdf.py
```

Choose a pdf file from your computer, and start querying the pdf by asking questions about it in natural language!
