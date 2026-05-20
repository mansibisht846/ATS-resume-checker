# pipeline.py
from extractor import extract_text
from cleaner import clean_text

def run_pipeline(pdf_path):
    """
    Connects extractor and cleaner into one function.
    Input  → path to a PDF file
    Output → dictionary with raw text and cleaned tokens
    """

    print(f"📄 Reading: {pdf_path}")

    # Step 1 — Extract raw text from PDF
    raw_text = extract_text(pdf_path)
    print(f"✅ Extracted: {len(raw_text)} characters")

    # Step 2 — Clean the raw text
    cleaned_tokens = clean_text(raw_text)
    print(f"✅ Cleaned: {len(cleaned_tokens)} meaningful words")

    # Step 3 — Return both as a dictionary
    result = {
        "pdf_path":       pdf_path,
        "raw_text":       raw_text,
        "cleaned_tokens": cleaned_tokens
    }

    return result


# ── Quick test ────────────────────────────────────────
if __name__ == "__main__":
    result = run_pipeline("Ojasvi_VERMA (3).pdf")

    print("\n--- PIPELINE OUTPUT ---")
    print(f"PDF:            {result['pdf_path']}")
    print(f"Raw characters: {len(result['raw_text'])}")
    print(f"Clean tokens:   {len(result['cleaned_tokens'])}")
    print(f"\nFirst 20 tokens: {result['cleaned_tokens'][:20]}")