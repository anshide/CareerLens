# CareerLens — Job Recommendations

CareerLens is an AI-powered job matching system that recommends jobs based on your resume. It analyzes both semantic meaning and specific skills to provide accurate job recommendations.


## Features

- **Semantic Matching**: Uses Natural Language Processing (NLP) and embeddings to match the meaning of the resume against job descriptions.
- **Skill Extraction**: Evaluates specific skills matched and missing compared to the job requirements.
- **Scoring System**: Combines semantic and skill scores for a comprehensive final ranking.

## Project Structure

- `backend/app/`: Core application logic, including matching pipelines and NLP utilities.
  - `matcher.py`: Main logic to process resumes and match with jobs.
  - `nlp/`: NLP and embedding modules.
- `backend/data/`: Data folder containing resumes and job listings (e.g., CSV, PDF).
- `frontend/`: React frontend application built with Vite.

## Usage

### Running the Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:5173`.

### Running the API

```bash
cd backend
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. You can also access the interactive API documentation at `http://127.0.0.1:8000/docs`.

### Testing the Pipeline

You can test the pipeline locally by running the provided script:

```bash
cd backend
python app/test_pipeline.py
```

This will load a sample resume, compare it with available jobs, and output a ranked list with detailed score breakdown (Semantic Score, Skill Score, Matched Skills, Missing Skills).
