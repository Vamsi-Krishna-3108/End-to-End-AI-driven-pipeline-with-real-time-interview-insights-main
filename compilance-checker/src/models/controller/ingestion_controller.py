#ingestion_controller.py
from PyPDF2 import PdfReader

def extract_text_from_pdf(filepath):
    """
    Extracts text from a PDF file.

    Args:
        filepath (str): Path to the PDF file.
    Returns:
        str: Extracted text from the PDF.
    """
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
