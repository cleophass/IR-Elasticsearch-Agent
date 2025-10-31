from elasticsearch import Elasticsearch, helpers
import os
from app.config import ES_HOST, ES_PASSWORD, ES_USERNAME
from app.embeddings import get_embeddings
es = Elasticsearch(
    hosts=ES_HOST,
    verify_certs=False 
)

def create_index(index, embeddings_shape):
    """Create an Elasticsearch index with specified mappings."""
    es.indices.create(
        index=index,
        mappings = 
        {
            "properties" : 
            {
                "title" : { "type" : "text"  },
                "content" : { "type" : "text"  },
                "embedding": { "type": "dense_vector", "dims": embeddings_shape }

            }
        }
    )

def verify_index(index):
    """Verify that an index exist in ElasticSearch"""
    return es.indices.exists(index = index)

def index_documents(index, df):
    """Index a list of documents into the specified Elasticsearch index."""
    actions = []
    for i, row in df.iterrows():
        action = {
            "_index": index,
            "_source": {
            "title": row["title"],
            "content": row["text"],
            "embedding": row["embeddings"]
            }
        }
        actions.append(action)

    helpers.bulk(es, actions)

def search(index_name, query):
    query_vec = get_embeddings(query)
    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                "params": {"query_vector": query_vec}
            }
        }
    }
    try :
        response = es.search(index=index_name, query=script_query)
        print("--> Document used by the agent: «", response["hits"]["hits"][0]["_source"]["title"], "»")
        return response['hits']['hits'][0]["_source"]["content"]
    except Exception as e:
        return str(e)