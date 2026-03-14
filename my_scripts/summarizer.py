# my_scripts/summarizer.py
from transformers import pipeline

# Load model once
# Transformers v5 only recognizes 'text-generation', so we use prompt-based summarization
summarizer_model = pipeline("text-generation", model="facebook/bart-large-cnn")

def summarize(text: str) -> str:
    """
    Summarize input text using prompt-based generation.
    """
    prompt = f"summarize: {text}"
    result = summarizer_model(prompt, max_length=120, do_sample=False)
    return result[0]["generated_text"]

# Optional test
if __name__ == "__main__":
    sample_text = (
        "Artificial intelligence is transforming the world, changing industries, "
        "creating new opportunities, and presenting ethical challenges."
    )
    print("Summary:\n", summarize(sample_text))