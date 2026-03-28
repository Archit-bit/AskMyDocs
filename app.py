import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
loader = TextLoader("data/sample.txt")
documents =loader.load()
text_splitter = RecursiveCharacterTextSplitter( chunk_size = 300, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

embeddings= OpenAIEmbeddings()
vectorstore= FAISS.from_documents(docs,embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3}) 
llm = ChatOpenAI(model = "gpt-4.1-nano")
prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the context below.
Context:
{context}

Question:
{question}""")
print("Ask questions about your document. Type 'exit' to quit.\n")
while True:
    question = input ("You: ")
    if question.lower()=="exit":
        break
    relevant_docs = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    messages= prompt.format_messages(context=context, question=question)
    response = llm.invoke(messages)
    print("\nBot:", response.content, "\n")
