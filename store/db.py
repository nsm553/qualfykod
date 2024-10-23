import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

EMBEDDING_DIMENSION = 1536
INDEX_NAME = ""

def init_db():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    if pc.has_index(INDEX_NAME):
        pc.delete_index (INDEX_NAME)
    
    pc.create_index (
        name=INDEX_NAME,
        dimension=EMBEDDING_DIMENSION,
        metric="cosine",
        spec=ServerlessSpec(cloud= 'aws', region='us-east-1')
    )
    return pc.Index(INDEX_NAME)


def get_db():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    if not pc.has_index(INDEX_NAME):
        current_app.logger.error ("DB Connection is not established")
        return Exception("DB Connection is not established")
    else:
        pc.Index(INDEX_NAME)

def query_db(query_vector):
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    indx = pc.Index(INDEX_NAME)

    results = indx.query(
        namespace="kod-space",
        top_k=3,
        include_values=True,
        include_metadata=True,
    )

    return results