"""from src.models.controllers.ingestion_controller import extract_text_from_pdf
from src.models.controllers.chunk_controller import chunk_text
from src.models.controllers.embedding_controller import generate_embeddings
from src.models.controllers.vector_controller import create_faiss_index, save_faiss_index
from src.models.controllers.pinecone_controller import upsert_to_pinecone"""

def process_pdf_pipeline(filepath, use_pinecone=False):
    """
    Orchestrates the PDF processing pipeline.

    Args:
        filepath (str): Path to the PDF file.
        use_pinecone (bool): Whether to store embeddings in Pinecone. Defaults to False.
    """
    print("--- Starting PDF Processing Pipeline ---")
    print()

    # Step 1: Extract text
    print("[1/4] Extracting text from PDF...")
    text = extract_text_from_pdf(filepath)
    print("Text extraction completed.")

    # Step 2: Chunk the text
    print("[2/4] Splitting text into chunks...")
    chunks = chunk_text(text)
    print(f"Text split into {len(chunks)} chunks.")

    # Step 3: Generate embeddings
    print("[3/4] Generating embeddings for chunks...")
    embeddings = generate_embeddings(chunks)
    print("Embeddings generation completed.")

    # Step 4: Store embeddings
    if use_pinecone:
        print("[4/4] Uploading embeddings to Pinecone...")
        upsert_to_pinecone("pdf-compliance-index", embeddings, ids=range(len(chunks)))
        print("Embeddings uploaded to Pinecone.")
    else:
        print("[4/4] Storing embeddings in a FAISS index...")
        index = create_faiss_index(embeddings)
        save_faiss_index(index, 'data/vector_store/index.faiss')
        print("FAISS index saved locally.")
    print()
    print("--- PDF Processing Pipeline Completed ---")
    print()



process_pdf_pipeline("/content/drive/MyDrive/214M1A3108.pdf")