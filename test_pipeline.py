# test_pipeline.py
# Day 7 — Full integration test
# Runs all Week 1 modules together and checks outputs

from pipeline import run_pipeline
from scorer import get_ats_score, get_role_fit, read_jd
from keyword_gap import get_keyword_gap

print("=" * 50)
print("   ATS ANALYSER — FULL INTEGRATION TEST")
print("=" * 50)

# Step 1 — Pipeline
print("\n📄 STEP 1: Running pipeline...")
result = run_pipeline("Ojasvi_VERMA (3).pdf")
print(f"   Raw characters : {len(result['raw_text'])}")
print(f"   Clean tokens   : {len(result['cleaned_tokens'])}")

# Step 2 — Read JD
print("\n📋 STEP 2: Reading job description...")
jd_text = read_jd("jd.txt")
print(f"   JD characters  : {len(jd_text)}")

# Step 3 — ATS Score
print("\n🎯 STEP 3: Calculating ATS score...")
score = get_ats_score(result['cleaned_tokens'], jd_text)
tier  = get_role_fit(score)
print(f"   ATS Score      : {score}%")
print(f"   Role Fit       : {tier}")

# Step 4 — Keyword Gap
print("\n🔍 STEP 4: Keyword gap analysis...")
gap = get_keyword_gap(result['cleaned_tokens'], jd_text)
print(f"   Matched        : {gap['total_matched']}")
print(f"   Missing        : {gap['total_missing']}")
print(f"   Match %        : {gap['match_percentage']}%")

# Step 5 — Final summary
print("\n" + "=" * 50)
print("   WEEK 1 COMPLETE — ALL MODULES WORKING ✅")
print("=" * 50)
print(f"\n   Resume    : Ojasvi_VERMA (3).pdf")
print(f"   ATS Score : {score}%")
print(f"   Role Fit  : {tier}")
print(f"   Matched   : {gap['total_matched']} keywords")
print(f"   Missing   : {gap['total_missing']} keywords")
print("\n   Ready for Week 2 — Visualisations + Streamlit! 🚀")
