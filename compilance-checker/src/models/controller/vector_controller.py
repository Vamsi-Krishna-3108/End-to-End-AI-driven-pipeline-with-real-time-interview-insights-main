import faiss
import os
#vector_controller.py
def create_faiss_index(embeddings):
    """
    Creates a FAISS index from embeddings.

    Args:
        embeddings (list): List of embeddings to store in the index.
    Returns:
        faiss.Index: The created FAISS index.
    """
    dim = embeddings[0].shape[0]  # Dimension of embeddings
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings.cpu().numpy())  # Convert PyTorch tensor to NumPy
    return index

def save_faiss_index(index, path):
    """
    Saves a FAISS index to a file.

    Args:
        index (faiss.Index): The FAISS index to save.
        path (str): File path to save the index.
    """
    faiss.write_index(index, path)

def load_faiss_index(path):
    """
    Loads a FAISS index from a file.

    Args:
        path (str): File path to load the index.
    Returns:
        faiss.Index: The loaded FAISS index.
    """
    if os.path.exists(path):
        return faiss.read_index(path)
    else:
        raise FileNotFoundError(f"Index file not found at {path}")
