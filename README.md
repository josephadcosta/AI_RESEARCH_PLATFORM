# AI Research Paper Discovery & Summarization Platform

## Overview

This project is an **AI-powered research paper discovery and summarization platform** built using modern Natural Language Processing (NLP) tools. The system allows users to search for research papers based on semantic similarity, retrieve the most relevant papers from a dataset, and generate concise summaries of the selected research content.

The platform is designed as a **local AI research assistant** that demonstrates how embeddings, semantic search, and transformer-based summarization models can be integrated into a research workflow.

The application uses **semantic embeddings to understand research paper abstracts**, enabling it to retrieve papers based on meaning rather than simple keyword matching. Once relevant papers are found, the system can generate **AI-generated summaries** to help users quickly understand the core ideas of the research.

A lightweight **Streamlit interface** is used to provide an interactive front-end for exploring the dataset and testing the AI features.

---

# Features

* Semantic search over research paper abstracts
* AI-generated research summaries
* Embedding-based similarity matching
* Streamlit interactive interface
* Modular Python architecture for easy extension
* Designed for experimentation with **AI-assisted research tools**

---

# Project Architecture

```
AI_RESEARCH_PLATFORM
│
├── app
│   └── streamlit_app.py
│
├── scripts
│   ├── summarizer.py
│   ├── embeddings.py
│   └── similarity.py
│
├── data
│   ├── arxiv_processed.csv
│   └── arxiv_embeddings.npy
│
├── requirements.txt
└── README.md
```

### Main Components

**1. Embedding Generator (`embeddings.py`)**

This script converts research paper abstracts into **vector embeddings** using a sentence-transformer model. These embeddings allow semantic comparison between research papers.

Model used:

```
all-MiniLM-L6-v2
```

The embeddings are stored as:

```
arxiv_embeddings.npy
```

---

**2. Similarity Search (`similarity.py`)**

This module performs **cosine similarity search** between a user query and the stored embeddings to find the most relevant research papers.

The system returns the **top 10 most similar research papers**.

---

**3. Summarization Engine (`summarizer.py`)**

The summarizer uses a transformer model to generate concise summaries of research abstracts.

Model used:

```
facebook/bart-large-cnn
```

This model is widely used for **abstractive text summarization**.

---

**4. Streamlit Application (`streamlit_app.py`)**

The Streamlit interface allows users to:

* Enter research queries
* Retrieve similar research papers
* Generate summaries of selected papers

---

# Dataset

This project uses research metadata from the **ArXiv dataset**.

Because the dataset and embeddings are **very large**, they are **NOT included in this repository**.

Users must download the dataset manually before running the project.

### Dataset Source

Primary dataset:

[https://www.kaggle.com/datasets/Cornell-University/arxiv](https://www.kaggle.com/datasets/Cornell-University/arxiv)

Alternative dataset:

[https://www.kaggle.com/datasets/tarunpaparaju/arxiv-metadata-oai-snapshot](https://www.kaggle.com/datasets/tarunpaparaju/arxiv-metadata-oai-snapshot)

---

# Large Files Notice

The following files are **not uploaded to GitHub** because they exceed GitHub's size limits:

* `data/arxiv_processed.csv`
* `data/arxiv_embeddings.npy`
* the entire `venv/` environment

These files must be recreated locally.

---

# Setup Instructions

## 1. Clone the Repository

```
git clone https://github.com/your-username/AI_RESEARCH_PLATFORM.git
cd AI_RESEARCH_PLATFORM
```

---

## 2. Create a Python Environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install streamlit
pip install transformers
pip install sentence-transformers
pip install faiss-cpu
pip install pandas
pip install scikit-learn
```

Alternatively install from:

```
pip install -r requirements.txt
```

---

## 4. Download the Dataset

Download the ArXiv metadata dataset and place the processed CSV file inside:

```
data/arxiv_processed.csv
```

The CSV should contain at least:

* title
* abstract
* categories

---

## 5. Generate Embeddings

Run the embedding script:

```
python scripts/embeddings.py
```

This will generate:

```
data/arxiv_embeddings.npy
```

This step may take several minutes depending on dataset size.

---

## 6. Run the Application

Start the Streamlit interface:

```
streamlit run app/streamlit_app.py
```

Then open the browser at:

```
http://localhost:8501
```

---

# Technologies Used

* Python
* Streamlit
* Transformers
* Sentence Transformers
* NumPy
* Pandas
* Scikit-learn
* HuggingFace Models

---

# Future Improvements

Potential improvements for this project include:

* Integration with the ArXiv API
* Vector database using FAISS or Chroma
* Retrieval-Augmented Generation (RAG)
* Full paper PDF retrieval
* Research question answering system
* AI research recommendation engine

---

# Educational Purpose

This project was created as a **learning project for AI-powered research tools**. It demonstrates how modern NLP models can be used to build systems that assist researchers in discovering and understanding scientific literature.

---

# License
Joseph Albert D Costa

This project is open-source and intended for educational and research purposes.


Those improvements can make the project look **3–5× stronger on GitHub.**
