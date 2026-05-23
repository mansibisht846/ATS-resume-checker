# keyword_gap.py
from pipeline import run_pipeline
from cleaner import clean_text
from scorer import read_jd

def get_keyword_gap(resume_tokens, jd_text):
    """
    Finds keywords present in JD but missing from resume.
    Returns missing keywords sorted by importance.
    """
    # Step 1 — Clean JD and get its tokens
    jd_tokens = clean_text(jd_text)

    # Step 2 — Convert both to sets for comparison
    resume_set = set(resume_tokens)
    jd_set     = set(jd_tokens)

    # Step 3 — Find missing keywords (in JD but not in resume)
    missing = jd_set - resume_set

    # Step 4 — Remove very short words
    missing = {word for word in missing if len(word) > 2}

    # Step 5 — Sort alphabetically
    missing_sorted = sorted(list(missing))

    # Step 6 — Find matched keywords
    matched = resume_set & jd_set
    matched = {word for word in matched if len(word) > 2}

    return {
        "missing_keywords": missing_sorted,
        "matched_keywords": sorted(list(matched)),
        "total_jd_keywords": len(jd_set),
        "total_matched":     len(matched),
        "total_missing":     len(missing),
        "match_percentage":  round(len(matched) / len(jd_set) * 100, 2)
    }


if __name__ == "__main__":
    result        = run_pipeline("Ojasvi_VERMA (3).pdf")
    resume_tokens = result['cleaned_tokens']
    jd_text       = read_jd("jd.txt")

    gap = get_keyword_gap(resume_tokens, jd_text)

    print("--- KEYWORD GAP ANALYSIS ---\n")
    print(f"Total JD keywords:  {gap['total_jd_keywords']}")
    print(f"Matched keywords:   {gap['total_matched']}")
    print(f"Missing keywords:   {gap['total_missing']}")
    print(f"Match percentage:   {gap['match_percentage']}%")

    print(f"\n✅ MATCHED ({gap['total_matched']}):")
    print(gap['matched_keywords'])

    print(f"\n❌ MISSING ({gap['total_missing']}):")
    print(gap['missing_keywords'])