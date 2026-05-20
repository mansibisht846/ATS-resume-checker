# scorer.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pipeline import run_pipeline
from cleaner import clean_text
import re

def read_jd(jd_path):
    """
    Reads job description from a .txt file and returns cleaned text.
    """
    with open(jd_path, 'r', encoding='utf-8') as f:
        jd_text = f.read()
    return jd_text

def get_ats_score(resume_tokens, jd_text):
    """
    Calculates ATS score using TF-IDF and cosine similarity.
    Input  → resume tokens (list), jd text (string)
    Output → ATS score (0-100)
    """

    # Step 1 — Convert resume tokens list back to a single string
    resume_text = ' '.join(resume_tokens)

    # Step 2 — Clean the JD text same way as resume
    jd_tokens = clean_text(jd_text)
    jd_clean = ' '.join(jd_tokens)

    # Step 3 — TF-IDF vectorization
    # Converts both texts into numerical vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_clean])

    # Step 4 — Cosine similarity between resume and JD vectors
    score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

    # Step 5 — Convert to percentage and round
    ats_score = round(score * 100, 2)

    return ats_score

def get_role_fit(score):
    """
    Returns role fit tier based on ATS score.
    """
    if score >= 75:
        return "Senior level match 🟢"
    elif score >= 50:
        return "Mid level match 🟡"
    elif score >= 30:
        return "Junior level match 🟠"
    else:
        return "Low match — needs improvement 🔴"


# ── Quick test ─────────────────────────────────────────
if __name__ == "__main__":
    # Step 1 — Run pipeline on resume
    result = run_pipeline("Ojasvi_VERMA (3).pdf")
    resume_tokens = result['cleaned_tokens']

    # Step 2 — Read JD
    jd_text = read_jd("jd.txt")

    # Step 3 — Get ATS score
    score = get_ats_score(resume_tokens, jd_text)
    tier  = get_role_fit(score)

    print("--- ATS SCORE RESULTS ---")
    print(f"📄 Resume: Ojasvi_VERMA (3).pdf")
    print(f"📋 JD:     jd.txt")
    print(f"\n🎯 ATS Score:  {score}%")
    print(f"📊 Role Fit:   {tier}")