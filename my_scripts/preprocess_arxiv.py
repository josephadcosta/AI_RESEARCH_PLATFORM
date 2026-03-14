import json
import pandas as pd

def convert_arxiv():

    papers = []

    with open("data/arxiv-metadata-oai-snapshot.json","r") as f:

        for i,line in enumerate(f):

            paper = json.loads(line)

            papers.append({

                "title": paper.get("title",""),
                "abstract": paper.get("abstract",""),
                "authors": paper.get("authors",""),
                "categories": paper.get("categories",""),
                "year": paper.get("update_date","")[:4]

            })

            if i > 200000:
                break

    df = pd.DataFrame(papers)

    df.to_csv("data/arxiv_processed.csv",index=False)

convert_arxiv()