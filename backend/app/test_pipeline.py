from matcher import load_resume, match_resume_to_jobs


# Resume
resume_path = "data/resume.pdf"


# Load and process resume
resume_text = load_resume(
    resume_path
)


# Match against jobs
results = match_resume_to_jobs(
    resume_text,
    "data/jobs.csv"
)


# Display results
print("\n")
print("=" * 60)
print("CAREERLENS — JOB RECOMMENDATIONS")
print("=" * 60)


for rank, result in enumerate(
    results[:5],
    start=1
):

    print(f"\n#{rank}")
    print(
        f"Job: {result['title']}"
    )

    print(
        f"Company: {result['company']}"
    )

    print(
        f"Final Score: "
        f"{result['final_score']:.2%}"
    )

    print(
        f"Semantic Score: "
        f"{result['semantic_score']:.2%}"
    )

    print(
        f"Skill Score: "
        f"{result['skill_score']:.2%}"
    )

    print(
        f"Matched Skills: "
        f"{result['matched_skills']}"
    )

    print(
        f"Missing Skills: "
        f"{result['missing_skills']}"
    )