import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import os, json
import streamlit as st
from dotenv import load_dotenv
from src.search_match import ensure_index, embed_text, blended_score, explain_match
from src.ingest_resume import parse_resume_text
from src.ingest_job import parse_job_text

load_dotenv()

st.set_page_config(page_title='Azure AI Resume ↔ Job Match', page_icon='🧠')
st.title('🧠 Talentox AI Resume ↔ Job Match (POC)')

with st.expander('ℹ️ About this demo'):
    st.write('Minimal proof-of-concept to demonstrate Azure Cognitive Search + Azure OpenAI for resume ↔ job matching with explainability.')

job_file = st.file_uploader('Upload a Job Description (TXT)', type=['txt'])
resume_files = st.file_uploader('Upload Resumes (TXT for demo)', type=['txt'], accept_multiple_files=True)

if st.button('Analyze') and job_file and resume_files:
    st.info('Building/validating index...')
    ensure_index()

    job_text = job_file.read().decode('utf-8', errors='ignore')
    job_doc = parse_job_text(job_text)
    job_vec = embed_text(job_doc['rawText'])

    st.success('Index ready. Searching top candidates...')

    candidates = []
    import numpy as np
    for rf in resume_files:
        rtext = rf.read().decode('utf-8', errors='ignore')
        rdoc = parse_resume_text(rtext)
        rvec = embed_text(rdoc['rawText'])

        # cosine similarity
        sim = float(np.dot(rvec, job_vec) / (np.linalg.norm(rvec) * np.linalg.norm(job_vec) + 1e-9))
        cand_score = blended_score(sim, rdoc.get('skills', []), job_doc.get('skills', []), rdoc.get('experienceYears', 0), job_doc.get('required_years', 0))
        summary_json = explain_match(job_doc, rdoc, cand_score)

        candidates.append({
            'title': rdoc.get('title','Candidate'),
            'fit_score': summary_json.get('fit_score', int(cand_score)),
            'strengths': summary_json.get('strengths', []),
            'gaps': summary_json.get('gaps', []),
            'summary': summary_json.get('summary', ''),
        })

    candidates = sorted(candidates, key=lambda c: c['fit_score'], reverse=True)
    for c in candidates:
        st.subheader(f"{c['title']} — Fit: {c['fit_score']}")
        st.write('**Strengths:** ' + (', '.join(c['strengths']) or '—'))
        st.write('**Gaps:** ' + (', '.join(c['gaps']) or '—'))
        st.write(c['summary'] or '—')
