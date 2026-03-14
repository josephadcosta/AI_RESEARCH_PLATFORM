import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_embeddings():

    df = pd.read_csv("data/arxiv_processed.csv")

    texts = df["abstract"].fillna("").tolist()

    embeddings = model.encode(texts)

    np.save("data/arxiv_embeddings.npy",embeddings)

build_embeddings()