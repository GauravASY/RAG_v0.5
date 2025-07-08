from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFaceEndpointEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pineconeDB import *
from langchain_pinecone import PineconeVectorStore

#Specification of the model used
def define_llm():
    model = HuggingFaceEndpoint(
       repo_id="deepseek-ai/DeepSeek-R1-0528",
        task="text-generation",
        max_new_tokens=100,
    )
    
    llm = ChatHuggingFace(llm = model)
    return llm

embedding_model = HuggingFaceEndpointEmbeddings(model= "sentence-transformers/all-MiniLM-L6-v2", task="feature-extraction")
vector_store = PineconeVectorStore(index=index, embedding=embedding_model)

#Loads the pdf 
def load_documents():
    loader = PyPDFLoader("./assets/RAG_CLIENT_FILE.pdf")
    docs = loader.load()
    print("Documents loaded.")
    return docs


#Splits PDF
def splits_documents(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 250, separators=["\n\n", "\n", ' ', ''])
    document = text_splitter.split_documents(docs)
    print("Splitting done.")
    embedding_docs(document)
    print("Embeddings Created")
    

def embedding_docs(documents):
    print("Embeddings in Process....")
    vector_store.add_documents(documents=documents)
    

   
def retrieve_docs(query):
    retriever = vector_store.as_retriever(search_type = "mmr")
    result = retriever.invoke(query)
    return result