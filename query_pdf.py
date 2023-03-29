import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import pickle

root = Tk()
root.withdraw()
pdf_path = askopenfilename(filetypes=[("PDF Files", "*.pdf")])
root.destroy()

# # Ask user for the data_name
# data_name = input("Please enter the pdf file name, without the extension: ")
# data_path = "pdf/"
data_name = pdf_name = os.path.splitext(os.path.basename(pdf_path))[0].replace(" ", "")
embeddings_path = "embeddings/"

reader = PdfReader(pdf_path)

raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

text_splitter = CharacterTextSplitter(        
    separator = "\n",
    chunk_size = 2000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

embeddings = OpenAIEmbeddings()

pickle_file_path = embeddings_path + data_name + ".pkl"

if os.path.exists(pickle_file_path):
    print ("Loading the embeddings...")
    with open(pickle_file_path, 'rb') as f:
         new_docsearch = pickle.load(f)
else:
    print ("Calculating the embeddings...")
    with open(pickle_file_path, 'wb') as f: 
        pickle.dump(embeddings, f)
        new_docsearch = embeddings

docsearch = FAISS.from_texts(texts, new_docsearch)

chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")

print ("Type exit to exit...")

while True:
    
    query = input("Please enter your query about the pdf: ")

    if query.lower() == "exit":
        break

    docs = docsearch.similarity_search(query)
    response = chain.run(input_documents=docs, question=query)
    print(response)