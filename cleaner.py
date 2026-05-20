# cleaner.py
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data — only runs once
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    """
    Takes raw text and returns a list of clean, meaningful words.
    Pipeline: lowercase → remove punctuation → tokenize → stopwords → lemmatize
    """

    # Step 1 — Lowercase everything
    text = text.lower()

    # Step 2 — Remove punctuation and special characters
    text = re.sub(r'[^a-z\s]', ' ', text)

    # Step 3 — Tokenize (split into individual words)
    tokens = word_tokenize(text)

    # Step 4 — Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Step 5 — Lemmatize (reduce to root form)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Step 6 — Remove very short words
    tokens = [word for word in tokens if len(word) > 2]

    return tokens


# ── Quick test ────────────────────────────────────────────
if __name__ == "__main__":
    from extractor import extract_text          # ← your actual function name

    raw_text = extract_text("Ojasvi_VERMA (3).pdf")   # ← your actual function name
    cleaned = clean_text(raw_text)

    print("--- CLEANED TOKENS ---")
    print(cleaned[:50])
    print(f"\n✅ Total meaningful words: {len(cleaned)}")

# Lemmatization check
test_words = ["projects", "analytics", "building", "completed", "technologies"]
lemmatizer = WordNetLemmatizer()
for word in test_words:
    print(f"{word} → {lemmatizer.lemmatize(word)}")