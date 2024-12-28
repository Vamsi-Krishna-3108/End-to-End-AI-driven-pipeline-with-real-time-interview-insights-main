import os
import pinecone
from pinecone import Pinecone, ServerlessSpec

# Load Pinecone API key from environment variables
PINECONE_API_KEY = "pcsk_622QE6_GnfmM3Pg86QbxSkfX4bMknDwg6pndgxwHEQnVJtqFDwyD2AHngi11MnYPU9LEBk"
# Ensure the required directory exists
os.makedirs("data/vector_store", exist_ok=True)

# Initialize the Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

def upsert_to_pinecone(index_name, embeddings, ids, texts):
    """
    Upserts vectors to a Pinecone index.

    Args:
        index_name (str): The name of the Pinecone index.
        embeddings (list): A list of embeddings.
        ids (list): A list of IDs corresponding to the embeddings.
        texts (list): A list of metadata text fields for each embedding.

    Returns:
        dict: A dictionary indicating success or failure.
    """
    try:
        # Check if the index exists
        if index_name not in pc.list_indexes().names():
            # Create the index
            pc.create_index(
                name=index_name,
                dimension=len(embeddings[0]),
                metric="euclidean",  # Adjust metric as needed (e.g., cosine)
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-west-2"  # Adjust the region as needed
                )
            )

        # Get the index instance
        index = pc.index(index_name)

        # Prepare the vectors for upsert
        vectors = [{"id": str(id_), "vector": embedding, "metadata": {"text_field": text}}
                   for id_, embedding, text in zip(ids, embeddings, texts)]

        # Upsert the vectors into Pinecone
        index.upsert(vectors)

        return {"message": f"Upserted {len(embeddings)} vectors to Pinecone index '{index_name}'"}
    except Exception as e:
        print(f"Error upserting to Pinecone: {str(e)}")
        return {"error": str(e)}
