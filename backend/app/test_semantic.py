from nlp.preprocessing import load_jobs, clean_text
from nlp.embeddings import create_embeddings
from nlp.semantic_matcher import calculate_semantic_similarity


# Load jobs
jobs = load_jobs("data/jobs.csv")


# Clean descriptions
documents = []

for description in jobs["description"]:
    documents.append(clean_text(description))


# Create semantic embeddings
embeddings = create_embeddings(documents)


# Calculate similarity
similarity_matrix = calculate_semantic_similarity(embeddings)


print("\nMost similar jobs:\n")


for i in range(len(jobs)):

    # Get similarity scores for current job
    scores = similarity_matrix[i].copy()

    # Remove itself
    scores[i] = -1

    # Find most similar job
    most_similar_index = scores.argmax()

    score = similarity_matrix[i][most_similar_index]

    print(
        f"{jobs.iloc[i]['title']} "
        f"<-> "
        f"{jobs.iloc[most_similar_index]['title']} "
        f"= {score:.2%}"
    )