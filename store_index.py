from dotenv import load_dotenv
import os
from src.help import load_pdf, filter_min_doc, split_text, download_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore



load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

extracted_data = load_pdf("data/")
minim_docs = filter_min_doc(extracted_data)
chunk_text = split_text(minim_docs)
embeddings = download_embeddings()

pinecone_api_key= PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)

index_name = "medbot"
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        spec=ServerlessSpec(cloud="gcp", region="us-central1"),
        dimension=384,
        metric="cosine" 
    )

index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_documents(
    documents=chunk_text,
    embedding=embeddings,
    index_name=index_name
)




