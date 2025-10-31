from app.embeddings import get_embeddings
import pandas as pd
from app.elasticsearch_client import index_documents, verify_index, create_index

def index_doc(file_path):
    """Index documents from a CSV file into the specified Elasticsearch index."""
    try :
        index = "articles"
        df = pd.read_csv(file_path)
        print(" --> Generating embeddings for documents... \n")
        embeddings = get_embeddings(df["text"], show_progress_bar=True)
        df["embeddings"] = embeddings.tolist()

        if not verify_index : 
            create_index(index, embeddings_shape=embeddings.shape[1])
        
        index_documents(index, df)
        return "Indexing completed successfully. Now you can use the RAG agent to query the indexed documents."

    except (FileNotFoundError) :
        return "The specified file was not found. Please provide a valid file path."
    except Exception as e:
        return "An error occurred during the indexing process:" + str(e)