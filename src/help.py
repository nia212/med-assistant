from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List
from langchain.schema import Document

# extract text from pdf file
def load_pdf(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True
        )
    documents = loader.load()
    return documents

def filter_min_doc(docs: List[Document]) -> List[Document]:
    minim_docs = []
    for doc in docs:
        src = doc.metadata.get("source")
        minim_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
        )

    )
    return minim_docs

#split the text into chunks
def split_text(minim_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, 
        chunk_overlap=20,
        length_function=len
    )
    chunk_text = text_splitter.split_documents(minim_docs)
    return chunk_text

def download_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name
    )
    return embeddings

