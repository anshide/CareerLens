from utils.pdf_parser import extract_text_from_pdf
from nlp.preprocessing import clean_text
from nlp.skill_extractor import extract_skills


# PDF location
pdf_path = "data/resume.pdf"


# Extract text
resume_text = extract_text_from_pdf(pdf_path)


print("========== RAW RESUME TEXT ==========\n")
print(resume_text)


# Clean text
cleaned_text = clean_text(resume_text)


print("\n========== CLEANED TEXT ==========\n")
print(cleaned_text)


# Extract skills
skills = extract_skills(cleaned_text)


print("\n========== SKILLS ==========\n")
print(skills)