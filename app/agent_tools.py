from langchain.tools import tool
from app.retriever import retrieve
from app.indexer import index_doc

@tool
def retrieve_documents(query: str):
    """Retrieve relevant documents based on a user query."""
    print("\n--> Tool 'retrieve_documents(," + query + ")' called... \n")
    result = retrieve(query)
    return "result: " + result

@tool
def index_documents(filepath: str):
    """Index relevant documents based on a file path."""
    print("\n--> Tool 'index_documents('" + filepath + "')' called... \n")
    result = index_doc(filepath)
    return "result: " + result