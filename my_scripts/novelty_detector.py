import numpy as np

def novelty_score(similarity_scores):

    max_sim = np.max(similarity_scores)

    novelty = 1 - max_sim

    return novelty