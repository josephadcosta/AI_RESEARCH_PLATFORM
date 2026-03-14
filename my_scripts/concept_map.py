import networkx as nx
import matplotlib.pyplot as plt

def build_concept_map(keywords):

    G = nx.Graph()

    for k in keywords:
        G.add_node(k)

    for i in range(len(keywords)-1):
        G.add_edge(keywords[i],keywords[i+1])

    nx.draw(G,with_labels=True)

    plt.show()