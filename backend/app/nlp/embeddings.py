from typing import List, Union
from sentence_transformers import SentenceTransformer # type: ignore

# Load the pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(documents: Union[List[str], str]):
    """
    Convert documents into semantic embeddings.
    """

    embeddings = model.encode( # type: ignore
        documents,
        convert_to_numpy=True
    )

    return embeddings