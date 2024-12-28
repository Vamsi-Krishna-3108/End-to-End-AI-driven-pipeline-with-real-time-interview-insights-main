from sentence_transformers import SentenceTransformer
#embedding_controller.py
model = SentenceTransformer('all-MiniLM-L6-v2')  # You can replace this with another Sentence Transformers model

def generate_embeddings(chunks):
    """
    Generates embeddings for a list of text chunks.

    Args:
        chunks (list): List of text chunks.
    Returns:
        list: A list of embeddings.
    """
    embeddings = model.encode(chunks, convert_to_tensor=True)
    return embeddings
