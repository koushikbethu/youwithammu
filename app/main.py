# from fastapi import FastAPI, UploadFile, File
# from pathlib import Path
# import shutil

# # ✅ Define FastAPI app FIRST
# app = FastAPI(title="AI Prep Coach")

# # ✅ Create uploads folder safely before using it
# UPLOAD_DIR = Path("uploads")
# UPLOAD_DIR.mkdir(exist_ok=True)

# # ✅ Home route
# @app.get("/")
# def home():
#     return {"message": "Welcome to AI Prep Coach 🚀 — FastAPI + Neon Cloud DB Connected Successfully!"}

# # ✅ Upload route
# @app.post("/upload_resume")
# async def upload_resume(file: UploadFile = File(...)):
#     try:
#         file_path = UPLOAD_DIR / file.filename
#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)
#         return {"filename": file.filename, "status": "Uploaded successfully!"}
#     except Exception as e:
#         return {"error": str(e)}


from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import shutil

from app.models.database import Base, engine, SessionLocal, Resume
from app.services.resume_parser import extract_text
from app.services.skill_extractor import extract_skills

app = FastAPI(title="AI Prep Coach")
Base.metadata.create_all(bind=engine)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/healthz")
def health_check():
    return {"status": "ok"}


@app.get("/")
def home():
    return {"message": "Welcome to AI Prep Coach 🚀 — Intelligent Resume Processor Active"}

@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text and skills
    resume_text = extract_text(str(file_path))
    skills = extract_skills(resume_text)

    # Save to Neon DB
    db = SessionLocal()
    new_resume = Resume(filename=file.filename, skills=", ".join(skills))
    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)
    db.close()

    return {
        "filename": file.filename,
        "skills_extracted": skills,
        "status": "Saved in Neon DB successfully!"
    }
