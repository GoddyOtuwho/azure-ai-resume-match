import numpy as np

# ---- Embeddings (placeholder) ----
def embed_text(text: str):
    # WARNING: Placeholder random vector for offline demo.
    # Replace with real call to Azure OpenAI embeddings.
    np.random.seed(abs(hash(text)) % (2**32))
    v = np.random.normal(size=3072).astype('float32')
    v /= (np.linalg.norm(v) + 1e-9)
    return v

def ensure_index():
    # In production, create/verify Azure Cognitive Search vector index here.
    return True

def skill_overlap(resume_skills, job_skills):
    if not job_skills:
        return 0.0
    inter = len(set([s.lower() for s in resume_skills]) & set([s.lower() for s in job_skills]))
    return inter / max(1, len(job_skills))

def experience_alignment(req, have):
    if req <= 0:
        return 1.0
    return max(0.0, min(1.0, have / req))

def blended_score(cos_sim, resume_skills, job_skills, cand_years, req_years):
    return int(
        0.70 * (max(0.0, min(1.0, float(cos_sim))) * 100) +
        0.20 * (skill_overlap(resume_skills, job_skills) * 100) +
        0.10 * (experience_alignment(req_years, cand_years) * 100)
    )

def explain_match(job_doc, resume_doc, pre_score):
    strengths = []
    gaps = []
    rs = set([s.lower() for s in resume_doc.get('skills', [])])
    js = set([s.lower() for s in job_doc.get('skills', [])])
    for s in (rs & js):
        strengths.append(f'Skill match: {s}')
    for s in (js - rs):
        gaps.append(f'Missing skill: {s}')

    return {
        'fit_score': int(pre_score),
        'strengths': strengths[:3],
        'gaps': gaps[:3],
        'summary': f"Candidate shows overlap in {len(strengths)} required skills with {len(gaps)} notable gaps. Pre-score {int(pre_score)}.",
    }
