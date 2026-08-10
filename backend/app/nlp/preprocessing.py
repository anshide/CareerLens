import re
import pandas as pd


def load_jobs(file_path):
    """
    Load job descriptions from a CSV file.
    """
    jobs = pd.read_csv(file_path)

    return jobs


def clean_text(text):
    """
    Clean text before NLP processing.
    """

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text