SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "pytorch",
    "tensorflow",
    "scikit-learn",
    "pandas",
    "numpy",
    "nlp",
    "transformers",
    "bert",
    "hugging face",
    "computer vision",
    "opencv",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "postgresql",
    "mysql",
    "fastapi",
    "flask",
    "react",
    "javascript",
    "git",
    "github",
    "excel",
    "power bi",
    "tableau",
    "langchain",
    "llms"
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills