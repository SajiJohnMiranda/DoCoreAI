import streamlit as st
import matplotlib.pyplot as plt
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset from Hugging Face
dataset = load_dataset("DoCoreAI/Dynamic-Temperature-GPT-3.5-Turbo")

# Extract original and generated responses
original_responses = dataset["test"]["Normal-Response"]
generated_responses = dataset["test"]["DoCoreAI-Response"]

# Compute cosine similarity
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(original_responses + generated_responses)
original_vectors = tfidf_matrix[: len(original_responses)]
generated_vectors = tfidf_matrix[len(original_responses) :]

similarity_scores = [
    cosine_similarity(original_vectors[i], generated_vectors[i])[0][0]
    for i in range(len(original_responses))
]

# Streamlit Dashboard
st.title("Cosine Similarity of Responses")
st.write("This graph compares Normal-Response and DoCoreAI-Response.")

# Matplotlib Plot
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(similarity_scores, marker="o", linestyle="-", color="blue")
ax.set_xlabel("Response Index")
ax.set_ylabel("Cosine Similarity Score")
ax.set_title("Cosine Similarity of Normal vs. DoCoreAI Responses")
ax.grid(True)

# Show in Streamlit
st.pyplot(fig)
