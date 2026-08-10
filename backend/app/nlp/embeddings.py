from sentence_transformers import SentenceTransformer


# Load the pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(documents):
    """
    Convert documents into semantic embeddings.
    """

    embeddings = model.encode(
        documents,
        convert_to_numpy=True
    )

    return embeddings