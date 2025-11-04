# import fitz  # PyMuPDF
# import docx2txt

# def extract_text(file_path: str):
#     if file_path.endswith(".pdf"):
#         text = ""
#         with fitz.open(file_path) as pdf:
#             for page in pdf:
#                 text += page.get_text()
#         return text
#     elif file_path.endswith(".docx"):
#         return docx2txt.process(file_path)
#     else:
#         raise ValueError("Unsupported file format")


import fitz  # PyMuPDF
import docx2txt

def extract_text(file_path: str) -> str:
    text = ""
    if file_path.endswith(".pdf"):
        with fitz.open(file_path) as pdf:
            for page in pdf:
                text += page.get_text()
    elif file_path.endswith(".docx"):
        text = docx2txt.process(file_path)
    return text.strip()
