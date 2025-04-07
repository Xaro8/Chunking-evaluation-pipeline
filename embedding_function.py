from sentence_transformers import SentenceTransformer

def embed_texts(texts):
    """
    Compute embeddings for a batch of texts using all-MiniLM-L6-v2.

    Args:
        texts (List[str]): A list of text strings to embed.

    Returns:
        np.ndarray: A 2D numpy array where each row is the embedding for a text.
    """
    
    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings
