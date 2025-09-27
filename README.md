# 🧠 Azure AI Resume ↔ Job Match

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io/)
[![Azure](https://img.shields.io/badge/Azure-OpenAI%20%7C%20Cognitive%20Search-0089D6)](https://azure.microsoft.com)

AI-powered **proof of concept (POC)** showing how to:
- Parse resumes & job descriptions automatically
- Match candidates to jobs with **semantic search + scoring**
- Generate explainable results (strengths, gaps, and summary) using Azure OpenAI

---

## 🚀 Quickstart (Local)

Clone the repo and run the Streamlit demo:

```bash
git clone https://github.com/GoddyOtuwho/azure-ai-resume-match.git
cd azure-ai-resume-match
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
