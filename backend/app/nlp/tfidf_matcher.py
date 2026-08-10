from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def create_tfidf_matrix(documents):
    """
    Convert text documents into TF-IDF vectors.
    """

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    return vectorizer, tfidf_matrix


def calculate_similarity(tfidf_matrix):
    """
    Calculate cosine similarity between all documents.
    """

    similarity_matrix = cosine_similarity(tfidf_matrix)

    return similarity_matrix