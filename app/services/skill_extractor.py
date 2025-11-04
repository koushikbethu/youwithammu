# import spacy

# nlp = spacy.load("en_core_web_sm")
# SKILLS = ["Python", "Machine Learning", "Deep Learning", "FastAPI",
#           "Flask", "React", "Java", "SQL", "C++", "NLP", "Data Science"]

# def extract_skills(text: str):
#     doc = nlp(text)
#     found = []
#     for token in doc:
#         if token.text in SKILLS:
#             found.append(token.text)
#     return list(set(found))


import spacy
import subprocess

# 🧠 Try to load the spaCy model safely; if it's missing, auto-download it
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("⚠️ spaCy model 'en_core_web_sm' not found. Downloading now...")
    subprocess.run(
        ["python", "-m", "spacy", "download", "en_core_web_sm"], check=True
    )
    nlp = spacy.load("en_core_web_sm")


COMMON_SKILLS = [
    "python", "java", "javascript", "html", "css", "sql",
    "machine learning", "deep learning", "fastapi", "flask",
    "django", "pandas", "numpy", "tensorflow", "pytorch",
    "communication", "leadership", "data analysis", "git"
]

def extract_skills(text: str):
    doc = nlp(text.lower())
    found = {skill for skill in COMMON_SKILLS if skill in doc.text}
    return list(found)
