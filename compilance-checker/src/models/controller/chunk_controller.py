def chunk_text(text, chunk_size=500, overlap=50):

    """
    Splits text into smaller chunks with optional overlaps.
    chunk_controller.py
    Args:
        text (str): The input text to split.
        chunk_size (int): The maximum size of each chunk.
        overlap (int): The number of overlapping characters between chunks.
    Returns:
        list: A list of text chunks.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks
