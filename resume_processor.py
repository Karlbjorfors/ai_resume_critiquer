import PyPDF2
import io
from typing import BinaryIO

def extract_text_from_pdf(pdf_file: BinaryIO) -> str:
    """Extract text from a PDF file."""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file) -> str:
    """Extract text from an uploaded file."""
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

def validate_file_content(content: str) -> bool:
    """Validate that the file content is not empty."""
    return bool(content.strip())