# AI Research Platform

An interactive **AI-powered research exploration platform** built with **Python, Streamlit, and Hugging Face Transformers**.
The platform allows users to explore research papers, search topics, upload PDFs, and generate AI summaries of academic content.

This project is designed as a **research-support tool** that helps users quickly analyze academic material and discover relevant research topics through an intuitive dashboard.

---

# Key Features

### 1. Research Paper Topic Explorer

Users can search through a processed research dataset and discover papers related to specific topics.

* Keyword search for research papers
* View titles, abstracts, and metadata
* Quickly identify relevant research directions

### 2. AI-Powered Text Summarization

The platform integrates a **Transformer-based language model** to generate concise summaries.

Users can:

* Paste text
* Upload research PDFs
* Generate short summaries automatically

This helps users **quickly understand long academic documents**.

### 3. PDF Research Analysis

Users can upload research papers in PDF format and automatically extract text for analysis and summarization.

### 4. Interactive Dashboard

The entire platform is built with **Streamlit**, providing:

* Interactive UI
* Fast search functionality
* Real-time summarization
* Simple navigation

---

# Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* Pandas
* PyPDF
* Machine Learning / NLP

---

# Project Structure

```
AI_RESEARCH_PLATFORM
│
├── app/
│   └── streamlit_app.py        # Main Streamlit application
│
├── my_scripts/
│   └── summarizer.py           # AI summarization module
│
├── data/
│   └── arxiv_processed.csv     # Research dataset (NOT included in repo)
│
├── static/                     # Static resources
│
├── requirements.txt            # Python dependencies
│
└── README.md
```

---

# Important Note About Large Files

To keep the repository lightweight and compatible with GitHub limits, the following items **are NOT included in this repository**:

### 1. Dataset

The research dataset (`arxiv_processed.csv`) has **not been uploaded** because of its large size.

Users must download or generate this dataset separately and place it inside the **data/** folder.

Example location:

```
data/arxiv_processed.csv
```

---

### 2. Python Virtual Environment

The **`venv/` folder is not included** because virtual environments contain thousands of large dependency files.

Users should create their own virtual environment when running the project.

---

# Installation and Setup

Follow these steps to run the project locally.

---

## 1. Clone the Repository

```
git clone https://github.com/your-username/AI_RESEARCH_PLATFORM.git
cd AI_RESEARCH_PLATFORM
```

---

## 2. Create a Virtual Environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Add the Dataset

Download or prepare the dataset and place it in:

```
data/arxiv_processed.csv
```

Without this file, the research search functionality will not work.

---

## 5. Run the Streamlit App

```
streamlit run app/streamlit_app.py
```

The application will open in your browser.

---

Project Sample Output (Screenshots)


# Future Improvements

Possible extensions for this platform include:

* AI-based research recommendation system
* Topic clustering and visualization
* Citation network graphs
* Research trend analysis
* Integration with online research APIs (arXiv, Semantic Scholar)

---

# Purpose of This Project

This project demonstrates:

* AI/NLP integration
* Real-world research tools
* full-stack Python application development
* dataset-driven interactive dashboards

Licensed Project
- Joseph Albert D Costa

