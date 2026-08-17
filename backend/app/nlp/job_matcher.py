from sklearn.metrics.pairwise import cosine_similarity

from nlp.embeddings import create_embeddings
from nlp.skill_extractor import extract_skills


def calculate_skill_score(resume_skills, job_skills):
    """
    Calculate how many required job skills
    are present in the resume.
    """

    if not job_skills:
        return 0.0

    resume_skills = set(resume_skills)
    job_skills = set(job_skills)

    matched_skills = resume_skills.intersection(job_skills)

    score = len(matched_skills) / len(job_skills)

    return score


def calculate_semantic_score(resume_text, job_text):
    """
    Calculate semantic similarity between
    resume and job description.
    """

    embeddings = create_embeddings([
        resume_text,
        job_text
    ])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return float(similarity)


def calculate_final_score(
    semantic_score,
    skill_score,
    semantic_weight=0.7,
    skill_weight=0.3
):
    """
    Combine semantic similarity and skill matching.
    """

    final_score = (
        semantic_score * semantic_weight
        + skill_score * skill_weight
    )

    return final_score