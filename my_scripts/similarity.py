import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def find_similar(query_embedding):

    embeddings = np.load("data/arxiv_embeddings.npy")

    scores = cosine_similarity([query_embedding],embeddings)

    df = pd.read_csv("data/arxiv_processed.csv")

    top = scores[0].argsort()[-10:]

    return df.iloc[top]