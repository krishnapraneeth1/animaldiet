
import os
from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index import ServiceContext
import os, streamlit as st



#Class RAG take query and return response
class RAG:
    def __init__(self):
        os.environ['OPENAI_API_KEY']='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'
        self.api_key=os.environ['OPENAI_API_KEY']
        self.documents = SimpleDirectoryReader("petData").load_data()
        self.llm = OpenAI(openai_api_key=self.api_key,model="gpt-3.5-turbo", temperature=0, max_tokens=256)
        self.service_context = ServiceContext.from_defaults(llm=self.llm, chunk_size=800, chunk_overlap=20)
        self.index = VectorStoreIndex.from_documents(self.documents, service_context=self.service_context)
        self.query_engine = self.index.as_query_engine(streaming=True)
        self.response = None

    def query(self, query):
        try:
            self.response = self.query_engine.query(query)
            return self.response
        except Exception as e:
            return f"An error occurred: {e}"
        

    #get dogDetails
    def getDogDetails(self, dogName):
        try:
            self.response = self.query_engine.query(f" tell me about the dog, {dogName}")
            return self.response
        except Exception as e:
            return f"An error occurred: {e}"
        
    #get catDetails
    def getCatDetails(self, catName):
        try:
            self.response = self.query_engine.query(f" tell me about the cat, {catName}")
            return self.response
        except Exception as e:
            return f"An error occurred: {e}"
        
    #get answer
    def getAnswer(self,pet, question):
        try:
            self.response = self.query_engine.query("for pet"+str(pet)+question)
            return self.response
        except Exception as e:
            return f"An error occurred: {e}"
        

        
