# 🧠 Azure AI Resume ↔ Job Match (POC)

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io/)
![Status](https://img.shields.io/badge/Status-POC-green)

**Live demo:** https://azure-ai-resume-match-ht7dzzezdh6bwagzdez7hf.streamlit.app/  
**Repo:** https://github.com/GoddyOtuwho/azure-ai-resume-match

A hands-on **proof of concept** that:
- Reads **Job Descriptions** and **Resumes** in **TXT/PDF**
- Extracts skills & years with lightweight NLP
- Computes a **Fit score** (cosine similarity + skill overlap + experience alignment)
- Produces an **explainable summary** (strengths, gaps)

> ⚠️ This is a demo POC. Embeddings & explanations are placeholders so it runs offline and in Streamlit Cloud. See **Roadmap** to plug in Azure OpenAI + Cognitive Search.

---

## 🚀 Quickstart (Local)

```bash
git clone https://github.com/GoddyOtuwho/azure-ai-resume-match.git
cd azure-ai-resume-match
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
