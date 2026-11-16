from io import BytesIO
from pypdf import PdfReader
from docx import Document


def extract_text(uploaded_file):
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "pdf":
        reader = PdfReader(BytesIO(uploaded_file.getvalue()))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)

    elif file_type == "docx":
        document = Document(BytesIO(uploaded_file.getvalue()))
        text = "\n".join(paragraph.text for paragraph in document.paragraphs)

    elif file_type == "txt":
        text = uploaded_file.getvalue().decode("utf-8")

    else:
        raise ValueError("Unsupported file type")

    return text
