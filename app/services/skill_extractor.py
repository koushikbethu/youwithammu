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
