from sentence_transformers import SentenceTransformer
from app.config import EMBEDDINGS_MODEL_NAME

model = SentenceTransformer(EMBEDDINGS_MODEL_NAME)

def get_embeddings(texts, show_progress_bar=False):
    """Generate embeddings for a list of texts using a pre-trained model."""
    return model.encode(texts, show_progress_bar=show_progress_bar)