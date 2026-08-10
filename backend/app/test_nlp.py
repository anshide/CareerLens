from nlp.preprocessing import load_jobs, clean_text
from nlp.skill_extractor import extract_skills


jobs = load_jobs("data/jobs.csv")

description = jobs.iloc[0]["description"]

cleaned_description = clean_text(description)

skills = extract_skills(cleaned_description)

print("Job:")
print(jobs.iloc[0]["title"])

print("\nOriginal description:")
print(description)

print("\nCleaned description:")
print(cleaned_description)

print("\nSkills found:")
print(skills)