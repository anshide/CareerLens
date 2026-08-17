# pyrefly: ignore [missing-import]
from fastapi import FastAPI, UploadFile, File
import shutil

from app.matcher import match_resume_to_jobs
from app.utils.pdf_parser import extract_text_from_pdf


app = FastAPI(
    title="CareerLens API",
    description="AI-powered job matching API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "CareerLens API is running"
    }


@app.post("/match")
async def match_resume(
    file: UploadFile = File(...)
):

    if not file.filename:
        return {
            "error": "No file uploaded"
        }

    file_path = f"data/{file.filename}"

    try:

        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        print(f"Resume saved: {file_path}")

        # Extract text
        resume_text = extract_text_from_pdf(
            file_path
        )

        print("Resume text extracted")
        print(f"Characters: {len(resume_text)}")

        if not resume_text.strip():
            return {
                "error": "Could not extract text from PDF"
            }

        # Match against jobs
        results = match_resume_to_jobs(
            resume_text,
            "data/jobs.csv"
        )

        print("Job matching completed")

        return {
            "filename": file.filename,
            "matches": results[:5]
        }

    finally:

        await file.close()

        print("Request completed")