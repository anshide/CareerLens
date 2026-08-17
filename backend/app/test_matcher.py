from nlp.preprocessing import load_jobs, clean_text
from nlp.skill_extractor import extract_skills
from nlp.job_matcher import (
    calculate_skill_score,
    calculate_semantic_score,
    calculate_final_score
)


# --------------------------------------------------
# 1. Load resume
# --------------------------------------------------

with open("data/sample_resume.txt", "r", encoding="utf-8") as file:
    resume_text = file.read()


resume_text = clean_text(resume_text)

resume_skills = extract_skills(resume_text)


print("Resume skills:")
print(resume_skills)


# --------------------------------------------------
# 2. Load jobs
# --------------------------------------------------

jobs = load_jobs("data/jobs.csv")


results = []


# --------------------------------------------------
# 3. Compare resume with every job
# --------------------------------------------------

for _, job in jobs.iterrows():

    job_text = clean_text(job["description"])

    job_skills = extract_skills(job_text)

    # Semantic similarity
    semantic_score = calculate_semantic_score(
        resume_text,
        job_text
    )

    # Skill similarity
    skill_score = calculate_skill_score(
        resume_skills,
        job_skills
    )

    # Final score
    final_score = calculate_final_score(
        semantic_score,
        skill_score
    )

    results.append({
        "title": job["title"],
        "company": job["company"],
        "semantic_score": semantic_score,
        "skill_score": skill_score,
        "final_score": final_score,
        "matched_skills": list(
            set(resume_skills).intersection(job_skills)
        ),
        "missing_skills": list(
            set(job_skills).difference(resume_skills)
        )
    })


# --------------------------------------------------
# 4. Sort jobs by final score
# --------------------------------------------------

results.sort(
    key=lambda x: x["final_score"],
    reverse=True
)


# --------------------------------------------------
# 5. Display results
# --------------------------------------------------

print("\n==============================")
print("TOP JOB MATCHES")
print("==============================\n")


for rank, result in enumerate(results, start=1):

    print(f"{rank}. {result['title']}")
    print(f"   Company: {result['company']}")
    print(
        f"   Semantic Score: "
        f"{result['semantic_score']:.2%}"
    )
    print(
        f"   Skill Score: "
        f"{result['skill_score']:.2%}"
    )
    print(
        f"   Final Score: "
        f"{result['final_score']:.2%}"
    )

    print(
        f"   Matched Skills: "
        f"{result['matched_skills']}"
    )

    print(
        f"   Missing Skills: "
        f"{result['missing_skills']}"
    )

    print()