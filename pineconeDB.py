from pinecone import Pinecone, ServerlessSpec
import os

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))


index_name = "rag-initial"  # change if desired

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

index = pc.Index(index_name)
