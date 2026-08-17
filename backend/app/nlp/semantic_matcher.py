from sklearn.metrics.pairwise import cosine_similarity


def calculate_semantic_similarity(embeddings):
    """
    Calculate cosine similarity between all job embeddings.
    """

    similarity_matrix = cosine_similarity(embeddings)

    return similarity_matrix