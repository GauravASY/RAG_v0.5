import os
from dotenv import load_dotenv
from helper import *
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()



brain = define_llm()

# print("loading Documents....")
# docs = load_documents()


# #Splits the pdf into chunks
# print("Splitting Docs") 
# splits_documents(docs)

while True:
    question = input("\n Ques : ")
    if(question == "exit"):
        print("Exiting ....")
        break
    vector_ans = retrieve_docs(question)
    docs_text = "".join(d.page_content for d in vector_ans)


    prompt = ChatPromptTemplate([
        ('system', "You are a helpful assistant who answers the queries of user using the context provided in simple language. If the user asks anything which is not in the context then just say you don't have the information. Context : {context}"),
        ('user', "{question}")
    ])
        
    model_query = prompt.format_messages(context = docs_text, question = question)

    for chunk in brain.stream(model_query):
        print(chunk.content, end="", flush=True)