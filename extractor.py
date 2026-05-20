import fitz

def extract_text(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

if __name__ == "__main__":
    result = extract_text("Ojasvi_VERMA (3).pdf")
    print(result[:500])
    print(f"\n✅ Total characters: {len(result)}")