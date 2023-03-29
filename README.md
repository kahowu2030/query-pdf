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
Set your OpenAI environment variable

```bash
export OPENAI_API_KEY="..."
```

## Usage
Run the python file as follow:
```bash
python query_pdf.py
```
Choose a file from your directory, and start querying the pdf by asking questions about it in natural language!

## License
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
