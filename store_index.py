from pinecone import Pinecone
from dotenv import load_dotenv
import os
from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_community.vectorstores import Pinecone as LangChainPinecone

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')


pc = Pinecone(api_key=PINECONE_API_KEY)



index = pc.Index(
    name="medicalchat",
    dimension=384,
    metric='cosine'
)


extracted_data = load_pdf("Data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


docsearch = LangChainPinecone.from_texts([t.page_content for t in text_chunks],
                                           index_name="medicalchat",
                                            embedding=embeddings)