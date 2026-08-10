from nlp.preprocessing import load_jobs, clean_text
from nlp.tfidf_matcher import create_tfidf_matrix, calculate_similarity


# Load jobs
jobs = load_jobs("data/jobs.csv")


# Clean descriptions
documents = []

for description in jobs["description"]:
    documents.append(clean_text(description))


# Create TF-IDF vectors
vectorizer, tfidf_matrix = create_tfidf_matrix(documents)


# Calculate similarity
similarity_matrix = calculate_similarity(tfidf_matrix)


print("\nMost similar job for each job:\n")


for i in range(len(jobs)):

    # Copy similarity scores for this job
    scores = similarity_matrix[i].copy()

    # Ignore the job itself
    scores[i] = -1

    # Find the most similar job
    most_similar_index = scores.argmax()

    similarity_score = similarity_matrix[
        i,
        most_similar_index
    ]

    print(
        f"{jobs.iloc[i]['title']} "
        f"↔ "
        f"{jobs.iloc[most_similar_index]['title']} "
        f"= "
        f"{similarity_score:.2f}"
    )