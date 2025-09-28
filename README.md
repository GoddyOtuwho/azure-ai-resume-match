# 🧠 Azure AI Resume ↔ Job Match (POC)

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io/)
![Status](https://img.shields.io/badge/Status-POC-green)

**Live demo:** https://azure-ai-resume-match-ht7dzzezdh6bwagzdez7hf.streamlit.app/

A hands-on **proof of concept** that:
- Parses **job descriptions** and **resumes** (TXT/PDF)
- Extracts skills/years with lightweight NLP
- Computes a **fit score** (cosine similarity + skill overlap + experience alignment)
- Generates an **explainable summary** (strengths & gaps)

---

## 🚀 Quickstart (Local)

```bash
git clone https://github.com/GoddyOtuwho/azure-ai-resume-match.git
cd azure-ai-resume-match
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
