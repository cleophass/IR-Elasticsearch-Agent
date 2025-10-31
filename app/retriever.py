from app.elasticsearch_client import search

def retrieve(query):
    return search("articles", query)