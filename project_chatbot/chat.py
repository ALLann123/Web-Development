#!/usr/bin/python3
from dotenv import load_dotenv
from llama_index.llms.groq import Groq
import os
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import SimpleDirectoryReader
from llama_index.core.llms import ChatMessage
from llama_index.core import VectorStoreIndex

# Load environment variable
load_dotenv()

# Set environment variable
api_key = os.getenv("GROQ_API_KEY")

# Initialize components
llm = Groq(model="llama3-70b-8192", api_key=api_key)
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Load knowledge base and create index (do this once at startup)
docs_business = SimpleDirectoryReader(input_files=["data/business.txt"]).load_data()
index = VectorStoreIndex.from_documents(docs_business, embed_model=embed_model)
query_engine = index.as_query_engine(similarity_top_k=3, llm=llm)

def get_response(message):
    try:
        response = query_engine.query(message)
        # Extract the response text if it's a complex object
        if hasattr(response, 'response'):
            return response.response
        return str(response)
    except Exception as e:
        print(f"Error in get_response: {str(e)}")
        return f"Sorry, I encountered an error: {str(e)}"