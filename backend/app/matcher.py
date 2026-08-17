from nlp.preprocessing import clean_text, load_jobs
from nlp.skill_extractor import extract_skills
from nlp.embeddings import create_embeddings

from sklearn.metrics.pairwise import cosine_similarity


def load_resume(resume_path):
    """
    Load the resume text from a PDF.
    """

    from utils.pdf_parser import extract_text_from_pdf

    resume_text = extract_text_from_pdf(resume_path)

    return clean_text(resume_text)


def match_resume_to_jobs(resume_text, jobs_path):
    """
    Match a resume against all jobs.
    """

    # -----------------------------------------
    # Resume processing
    # -----------------------------------------

    resume_text = clean_text(resume_text)

    resume_skills = extract_skills(resume_text)

    # -----------------------------------------
    # Load jobs
    # -----------------------------------------

    jobs = load_jobs(jobs_path)

    # -----------------------------------------
    # Create embeddings
    # -----------------------------------------

    documents = [resume_text]

    for description in jobs["description"]:
        documents.append(
            clean_text(description)
        )

    embeddings = create_embeddings(documents)

    resume_embedding = embeddings[0]
    job_embeddings = embeddings[1:]

    # -----------------------------------------
    # Calculate semantic similarity
    # -----------------------------------------

    similarities = cosine_similarity(
        [resume_embedding],
        job_embeddings
    )[0]

    results = []

    # -----------------------------------------
    # Calculate scores
    # -----------------------------------------

    for i, job in jobs.iterrows():

        job_text = clean_text(
            job["description"]
        )

        job_skills = extract_skills(
            job_text
        )

        # Skill matching
        resume_skill_set = set(resume_skills)
        job_skill_set = set(job_skills)

        matched_skills = (
            resume_skill_set.intersection(
                job_skill_set
            )
        )

        missing_skills = (
            job_skill_set.difference(
                resume_skill_set
            )
        )

        if job_skill_set:

            skill_score = (
                len(matched_skills)
                / len(job_skill_set)
            )

        else:

            skill_score = 0

        # Semantic score
        semantic_score = float(
            similarities[i]
        )

        # Final score
        final_score = (
            semantic_score * 0.7
            + skill_score * 0.3
        )

        results.append({
            "job_id": int(job["job_id"]),
            "title": job["title"],
            "company": job["company"],
            "semantic_score": semantic_score,
            "skill_score": skill_score,
            "final_score": final_score,
            "matched_skills": sorted(
                matched_skills
            ),
            "missing_skills": sorted(
                missing_skills
            )
        })

    # -----------------------------------------
    # Sort by final score
    # -----------------------------------------

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return results