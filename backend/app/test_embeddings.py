from nlp.preprocessing import load_jobs, clean_text
from nlp.embeddings import create_embeddings


# Load job data
jobs = load_jobs("data/jobs.csv")


# Clean job descriptions
documents = []

for description in jobs["description"]:
    documents.append(clean_text(description))


# Create semantic embeddings
embeddings = create_embeddings(documents)


print("Embedding shape:")
print(embeddings.shape)


print("\nFirst job embedding:")
print(embeddings[0])